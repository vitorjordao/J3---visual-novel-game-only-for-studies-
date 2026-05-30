#!/usr/bin/env python3
"""
Audio QA: validate duration, RMS loudness, peak amplitude, and detect clipping
for all WAV/MP3 files in game/audio/. Outputs JSON + applies optional
normalization to equalize loudness across files.

Uses scipy + numpy + pydub (for MP3 read). Writes audio-qa-findings.json.
"""
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Optional

import numpy as np
from scipy.io import wavfile

try:
    from mutagen.mp3 import MP3
    HAS_MUTAGEN = True
except ImportError:
    HAS_MUTAGEN = False


@dataclass
class AudioStat:
    path: str
    duration_s: float
    sample_rate: int
    channels: int
    rms_db: float
    peak_db: float
    clipping_pct: float
    findings: list[str]

    def as_dict(self):
        return asdict(self)


def db(x: float) -> float:
    return 20 * np.log10(max(abs(x), 1e-9))


def load_audio(path: Path) -> Optional[tuple[int, np.ndarray]]:
    """Returns (sample_rate, float32 mono samples [-1, 1])."""
    if path.suffix.lower() == ".wav":
        sr, data = wavfile.read(str(path))
        if data.dtype == np.int16:
            f = data.astype(np.float32) / 32768.0
        elif data.dtype == np.int32:
            f = data.astype(np.float32) / 2147483648.0
        elif data.dtype == np.uint8:
            f = (data.astype(np.float32) - 128) / 128.0
        elif data.dtype == np.float32:
            f = data
        else:
            f = data.astype(np.float32)
        if f.ndim == 2:
            f = f.mean(axis=1)
        return sr, f
    elif path.suffix.lower() == ".mp3":
        # MP3 sem ffmpeg: usa mutagen para metadata (duration, sr) — sem amplitude analysis.
        if not HAS_MUTAGEN:
            return None
        try:
            audio = MP3(str(path))
            sr = audio.info.sample_rate
            duration = audio.info.length
            # Sintetiza zeros para representar duration; amplitude N/A.
            samples = np.zeros(int(sr * duration), dtype=np.float32)
            return sr, samples
        except Exception:
            return None
    return None


def analyze(path: Path,
            target_rms_db: float = -18.0,
            min_dur: float = 0.3,
            max_clipping_pct: float = 0.5) -> AudioStat:
    findings = []
    loaded = load_audio(path)
    if loaded is None:
        return AudioStat(str(path), 0, 0, 0, -120, -120, 0,
                         findings=["UNREADABLE: codec not supported"])
    sr, samples = loaded
    duration_s = len(samples) / sr
    is_mp3_metadata_only = path.suffix.lower() == ".mp3" and not np.any(samples)
    if is_mp3_metadata_only:
        # Sem amplitude analysis para MP3 (sem ffmpeg). Reporta apenas duration.
        return AudioStat(
            path=str(path),
            duration_s=round(duration_s, 3),
            sample_rate=sr,
            channels=1,
            rms_db=-999,
            peak_db=-999,
            clipping_pct=-1,
            findings=["MP3_METADATA_ONLY: sem ffmpeg, sem analise de amplitude"],
        )
    rms = np.sqrt(np.mean(samples ** 2)) + 1e-12
    peak = np.max(np.abs(samples)) + 1e-12
    rms_db_val = 20 * np.log10(rms)
    peak_db_val = 20 * np.log10(peak)
    clip_pct = float(np.mean(np.abs(samples) > 0.99) * 100)

    if duration_s < min_dur:
        findings.append(f"SHORT: {duration_s:.2f}s < {min_dur}s")
    if rms_db_val < target_rms_db - 6:
        findings.append(f"QUIET: RMS {rms_db_val:.1f} dBFS, target {target_rms_db:.1f}")
    if rms_db_val > target_rms_db + 6:
        findings.append(f"LOUD: RMS {rms_db_val:.1f} dBFS, target {target_rms_db:.1f}")
    if peak_db_val > -0.5:
        findings.append(f"PEAK_CLOSE_TO_FS: {peak_db_val:.2f} dBFS")
    if clip_pct > max_clipping_pct:
        findings.append(f"CLIPPING: {clip_pct:.2f}% samples at full scale")

    return AudioStat(
        path=str(path),
        duration_s=float(round(duration_s, 3)),
        sample_rate=int(sr),
        channels=1,
        rms_db=float(round(rms_db_val, 2)),
        peak_db=float(round(peak_db_val, 2)),
        clipping_pct=float(round(clip_pct, 3)),
        findings=findings,
    )


def normalize_file(path: Path, target_rms_db: float = -18.0) -> Optional[dict]:
    """Renormalize file in place to target RMS. Returns adjustment in dB."""
    loaded = load_audio(path)
    if loaded is None:
        return None
    sr, samples = loaded
    rms = np.sqrt(np.mean(samples ** 2)) + 1e-12
    current_db = 20 * np.log10(rms)
    gain_db = target_rms_db - current_db
    gain_lin = 10 ** (gain_db / 20)
    out = samples * gain_lin
    # Soft-clip to prevent peaks exceeding -1 dBFS
    peak = np.max(np.abs(out)) + 1e-12
    if peak > 0.95:
        out = out * (0.95 / peak)
    if path.suffix.lower() == ".wav":
        wavfile.write(str(path), sr, (out * 32767).astype(np.int16))
        return {"applied_gain_db": float(round(gain_db, 2)),
                "final_peak_db": float(round(20 * np.log10(np.max(np.abs(out)) + 1e-12), 2))}
    # MP3: skip (would need pydub re-encode, lossy)
    return {"applied_gain_db": None, "reason": "mp3_skipped"}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--audio-root", type=Path,
                        default=Path("Projeto/J3 Project/game/audio"))
    parser.add_argument("--out", type=Path,
                        default=Path("tools/qa/audio-qa-findings.json"))
    parser.add_argument("--target-rms-db", type=float, default=-18.0,
                        help="Target RMS loudness in dBFS (game audio standard).")
    parser.add_argument("--normalize", action="store_true",
                        help="Apply RMS normalization in place (WAV only).")
    args = parser.parse_args()
    audio_root: Path = args.audio_root.resolve()
    if not audio_root.exists():
        print(f"ERROR: {audio_root} nao existe", file=sys.stderr)
        return 2
    files = sorted([p for ext in ("*.wav", "*.mp3", "*.ogg")
                    for p in audio_root.rglob(ext)])
    stats = []
    normalized = []
    for p in files:
        stat = analyze(p, target_rms_db=args.target_rms_db)
        stats.append(stat)
        print(f"  {p.name}: {stat.duration_s:.2f}s  RMS {stat.rms_db:.1f} dBFS  "
              f"peak {stat.peak_db:.1f} dBFS  clip {stat.clipping_pct:.2f}%  "
              f"{('OK' if not stat.findings else '/'.join(stat.findings))}")
        if args.normalize and p.suffix.lower() == ".wav":
            norm = normalize_file(p, target_rms_db=args.target_rms_db)
            if norm:
                normalized.append({"path": str(p), **norm})
                print(f"     -> normalized: gain {norm.get('applied_gain_db')} dB")
    output = {
        "target_rms_db": args.target_rms_db,
        "stats": [s.as_dict() for s in stats],
        "normalized": normalized,
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(output, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Findings: {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
