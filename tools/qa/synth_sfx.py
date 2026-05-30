#!/usr/bin/env python3
"""
Synthesize cyberpunk-style SFX as WAV files. Royalty-free (generated locally).

Each function returns numpy array of float32 samples [-1, 1]; main() writes them
to a target dir as int16 WAV at 44.1kHz mono.

Outputs (10 files to satisfy game/scripts/day*.rpy references):
  crowd_noise.wav
  alert.wav
  alarm.wav
  sirens.wav
  sirens_close.wav
  news_broadcast.wav
  explosions.wav
  emp_blasts.wav
  memory_glitch.wav
  battle.wav
"""
from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
from scipy.io import wavfile
from scipy.signal import butter, sosfilt

SR = 44100  # sample rate

rng = np.random.default_rng(42)


def t(duration: float) -> np.ndarray:
    return np.linspace(0, duration, int(SR * duration), endpoint=False)


def normalize(x: np.ndarray, target_peak: float = 0.85) -> np.ndarray:
    peak = np.max(np.abs(x)) + 1e-9
    return (x / peak) * target_peak


def fade(x: np.ndarray, fade_in: float = 0.02, fade_out: float = 0.05) -> np.ndarray:
    n = len(x)
    fi = int(SR * fade_in)
    fo = int(SR * fade_out)
    env = np.ones(n)
    if fi > 0:
        env[:fi] = np.linspace(0, 1, fi)
    if fo > 0:
        env[-fo:] = np.linspace(1, 0, fo)
    return x * env


def bandpass(x: np.ndarray, low: float, high: float, order: int = 4) -> np.ndarray:
    sos = butter(order, [low / (SR / 2), high / (SR / 2)], btype="band", output="sos")
    return sosfilt(sos, x)


def lowpass(x: np.ndarray, cutoff: float, order: int = 4) -> np.ndarray:
    sos = butter(order, cutoff / (SR / 2), btype="low", output="sos")
    return sosfilt(sos, x)


def highpass(x: np.ndarray, cutoff: float, order: int = 4) -> np.ndarray:
    sos = butter(order, cutoff / (SR / 2), btype="high", output="sos")
    return sosfilt(sos, x)


def pink_noise(duration: float) -> np.ndarray:
    n = int(SR * duration)
    white = rng.standard_normal(n)
    # Voss-McCartney approximation: cumulative sum filtered
    p = np.cumsum(white) / np.sqrt(np.arange(1, n + 1))
    return p - np.mean(p)


def crowd_noise(duration: float = 8.0) -> np.ndarray:
    """Urban crowd: filtered pink noise + sparse low murmurs + occasional shouts."""
    base = pink_noise(duration)
    base = bandpass(base, 200, 3000)
    # Murmurs: amplitude modulated low noise
    n = int(SR * duration)
    murmur_env = 0.3 + 0.4 * np.abs(np.sin(2 * np.pi * 0.5 * t(duration)))
    base = base * murmur_env
    # Sparse shouts: 4 short noise bursts pitched higher
    out = base * 0.5
    for _ in range(4):
        start = rng.uniform(0.5, duration - 0.5)
        dur = rng.uniform(0.15, 0.4)
        burst = bandpass(rng.standard_normal(int(SR * dur)), 600, 2200)
        burst = fade(burst, 0.02, 0.1) * 0.4
        i0 = int(SR * start)
        i1 = min(n, i0 + len(burst))
        out[i0:i1] += burst[:i1 - i0]
    return normalize(fade(out, 0.3, 0.5))


def alert(duration: float = 0.6) -> np.ndarray:
    """Sci-fi alert: rising beep then short pause then second beep."""
    samples = []
    beep_dur = 0.18
    pause = 0.08
    for freq in (880, 1320):
        x = np.sin(2 * np.pi * freq * t(beep_dur))
        x = fade(x, 0.005, 0.02)
        samples.append(x)
        samples.append(np.zeros(int(SR * pause)))
    out = np.concatenate(samples)
    # Pad to requested duration
    if len(out) < int(SR * duration):
        out = np.pad(out, (0, int(SR * duration) - len(out)))
    return normalize(out)


def alarm(duration: float = 2.5) -> np.ndarray:
    """Industrial alarm: repeating square wave 1kHz at ~3Hz on/off."""
    n = int(SR * duration)
    carrier = np.sign(np.sin(2 * np.pi * 1000 * t(duration)))
    gate = (np.sin(2 * np.pi * 3 * t(duration)) > 0).astype(float)
    out = carrier * gate * 0.7
    # Add slight pitch warble
    warble = 0.05 * np.sin(2 * np.pi * 5 * t(duration))
    out = out + warble * gate
    return normalize(fade(out, 0.01, 0.1))


def siren(duration: float = 3.0, f_low: float = 700, f_high: float = 1300,
          sweep_period: float = 1.2) -> np.ndarray:
    """Police siren: sinusoidally swept frequency."""
    n = int(SR * duration)
    sweep = (f_low + f_high) / 2 + (f_high - f_low) / 2 * np.sin(2 * np.pi * (1 / sweep_period) * t(duration))
    phase = np.cumsum(2 * np.pi * sweep / SR)
    out = np.sin(phase) * 0.8
    # Doppler-like volume mod
    vol = 0.7 + 0.3 * np.sin(2 * np.pi * 0.4 * t(duration))
    out = out * vol
    return normalize(fade(out, 0.05, 0.2))


def news_broadcast(duration: float = 4.0) -> np.ndarray:
    """Radio static + voice-band hum + intermittent bleeps."""
    static = bandpass(rng.standard_normal(int(SR * duration)), 300, 4000) * 0.3
    hum = 0.15 * np.sin(2 * np.pi * 120 * t(duration))
    # Bleeps
    out = static + hum
    for i in range(int(duration * 1.5)):
        pos = i / 1.5 + rng.uniform(0, 0.3)
        if pos >= duration - 0.1:
            continue
        freq = rng.choice([800, 1200, 1500])
        dur = 0.05
        bleep = np.sin(2 * np.pi * freq * t(dur)) * 0.4
        bleep = fade(bleep, 0.005, 0.01)
        i0 = int(SR * pos)
        i1 = min(len(out), i0 + len(bleep))
        out[i0:i1] += bleep[:i1 - i0]
    return normalize(fade(out, 0.1, 0.2))


def explosion(duration: float = 1.8) -> np.ndarray:
    """Low-freq pulse + filtered noise burst with decaying envelope."""
    n = int(SR * duration)
    noise = rng.standard_normal(n)
    low = lowpass(noise, 250)
    mid = bandpass(noise, 300, 1500)
    high = bandpass(noise, 1500, 4000) * 0.3
    # Decay envelope
    env = np.exp(-3 * np.linspace(0, 1, n))
    out = (low * 1.0 + mid * 0.6 + high) * env
    # Initial pulse
    pulse_dur = 0.05
    pulse = np.sin(2 * np.pi * 60 * t(pulse_dur)) * np.exp(-30 * t(pulse_dur))
    out[:len(pulse)] += pulse
    return normalize(fade(out, 0.001, 0.3))


def emp_blast(duration: float = 1.5) -> np.ndarray:
    """Frequency sweep downward + electric noise crackle."""
    n = int(SR * duration)
    # Sweep 3kHz -> 80Hz over duration
    freq = 3000 * np.exp(-3 * np.linspace(0, 1, n))
    phase = np.cumsum(2 * np.pi * freq / SR)
    sweep = np.sin(phase) * np.exp(-2 * np.linspace(0, 1, n))
    # Crackle
    crackle = bandpass(rng.standard_normal(n), 2000, 5000) * np.exp(-5 * np.linspace(0, 1, n)) * 0.4
    out = sweep + crackle
    return normalize(fade(out, 0.01, 0.2))


def memory_glitch(duration: float = 1.2) -> np.ndarray:
    """Short bit-crushed bursts: bursts of sample-rate-reduced sine + noise."""
    n = int(SR * duration)
    out = np.zeros(n)
    for i in range(8):
        pos = rng.uniform(0, duration - 0.1)
        burst_dur = rng.uniform(0.05, 0.15)
        burst_n = int(SR * burst_dur)
        freq = rng.choice([220, 330, 440, 660, 880])
        burst = np.sin(2 * np.pi * freq * np.arange(burst_n) / SR)
        # Bit-crush: reduce effective sample rate by holding every Nth sample
        hold = 8
        crushed = np.repeat(burst[::hold], hold)[:burst_n]
        # Quantize amplitude
        crushed = np.round(crushed * 4) / 4
        # Add noise
        crushed = crushed * 0.6 + rng.standard_normal(burst_n) * 0.15
        crushed = fade(crushed, 0.005, 0.02)
        i0 = int(SR * pos)
        i1 = min(n, i0 + burst_n)
        out[i0:i1] += crushed[:i1 - i0]
    return normalize(fade(out, 0.05, 0.1))


def battle(duration: float = 6.0) -> np.ndarray:
    """Low rumble + intermittent impacts."""
    n = int(SR * duration)
    rumble = lowpass(rng.standard_normal(n), 200) * 0.4
    rumble_mod = 0.5 + 0.5 * np.sin(2 * np.pi * 0.7 * t(duration))
    rumble = rumble * rumble_mod
    out = rumble
    # Impacts: bandpassed noise bursts
    impact_count = int(duration * 1.5)
    for _ in range(impact_count):
        pos = rng.uniform(0, duration - 0.2)
        burst_dur = rng.uniform(0.08, 0.25)
        burst_n = int(SR * burst_dur)
        burst = bandpass(rng.standard_normal(burst_n), 100, 2000)
        burst = burst * np.exp(-5 * np.linspace(0, 1, burst_n)) * 0.8
        i0 = int(SR * pos)
        i1 = min(n, i0 + burst_n)
        out[i0:i1] += burst[:i1 - i0]
    return normalize(fade(out, 0.2, 0.5))


SFX_SPECS = {
    "crowd_noise.wav":   crowd_noise,
    "alert.wav":         alert,
    "alarm.wav":         alarm,
    "sirens.wav":        siren,
    "sirens_close.wav":  lambda: siren(duration=3.5, f_low=900, f_high=1600, sweep_period=0.8),
    "news_broadcast.wav": news_broadcast,
    "explosions.wav":    explosion,
    "emp_blasts.wav":    emp_blast,
    "memory_glitch.wav": memory_glitch,
    "battle.wav":        battle,
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, default=Path("Projeto/J3 Project/game/audio/sfx"))
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    for name, fn in SFX_SPECS.items():
        x = fn()
        # Apply consistent loudness target (~-14 LUFS approximation via RMS)
        rms = np.sqrt(np.mean(x ** 2)) + 1e-9
        target_rms = 0.2
        x = x * (target_rms / rms)
        x = np.clip(x, -0.95, 0.95)
        out_path = args.out / name
        wavfile.write(str(out_path), SR, (x * 32767).astype(np.int16))
        dur = len(x) / SR
        print(f"  {name}: {dur:.2f}s rms->{target_rms} peak={np.max(np.abs(x)):.2f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
