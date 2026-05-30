#!/usr/bin/env python3
"""
Auto-fix: adiciona 'call atualizar_status' ao final de opcoes de menu que
modificam estado mas nao chamam atualizar_status nem jump/return.

Le findings de menu-validation-findings.json (check=missing_atualizar_status),
edita arquivos em-place. Backup .bak por arquivo.
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
from collections import defaultdict
from pathlib import Path

RE_OPTION = re.compile(r'^(\s+)"((?:[^"\\]|\\.)*)":\s*$')


def fix_file(file_path: Path, opt_lines: set[int]) -> int:
    """Add 'call atualizar_status' at end of body of each option starting at opt_lines."""
    text = file_path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=False)
    # Find body end for each opt_line
    insertions = []  # (line_index_to_insert_after, indent_str_for_body)
    for opt_line in opt_lines:
        # opt_line is 1-indexed; lines[opt_line-1] is the option header
        if opt_line - 1 >= len(lines):
            continue
        header = lines[opt_line - 1]
        m = RE_OPTION.match(header)
        if not m:
            continue
        opt_indent = len(m.group(1))
        body_indent = opt_indent + 4
        # Find last non-empty body line
        last_body_idx = opt_line - 1  # will be > if body exists
        j = opt_line  # next line after header (0-indexed = opt_line)
        last_non_empty = -1
        while j < len(lines):
            ln = lines[j]
            if not ln.strip():
                j += 1
                continue
            cur_indent = len(ln) - len(ln.lstrip())
            if cur_indent <= opt_indent:
                break
            last_non_empty = j
            j += 1
        if last_non_empty < 0:
            continue
        # Skip if already ends with atualizar_status (sanity)
        if "atualizar_status" in lines[last_non_empty]:
            continue
        # Skip if ends with jump/return
        if re.search(r"\b(jump|return)\b", lines[last_non_empty]):
            continue
        insertions.append((last_non_empty, " " * body_indent + "call atualizar_status"))

    if not insertions:
        return 0
    # Apply insertions in reverse order
    insertions.sort(key=lambda x: x[0], reverse=True)
    backup = file_path.with_suffix(file_path.suffix + ".bak")
    shutil.copy2(file_path, backup)
    new_lines = list(lines)
    for idx, insert_text in insertions:
        new_lines.insert(idx + 1, insert_text)
    file_path.write_text("\n".join(new_lines) + ("\n" if text.endswith("\n") else ""),
                         encoding="utf-8")
    return len(insertions)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--findings", type=Path,
                        default=Path("tools/qa/menu-validation-findings.json"))
    parser.add_argument("--root", type=Path,
                        default=Path("Projeto/J3 Project/game"))
    args = parser.parse_args()
    data = json.loads(args.findings.read_text(encoding="utf-8"))
    targets = defaultdict(set)
    for f in data["findings"]:
        if f["check"] != "missing_atualizar_status":
            continue
        targets[f["file"]].add(f["line"])

    total = 0
    for file_rel, opt_lines in sorted(targets.items()):
        file_path = args.root / file_rel.replace("\\", "/")
        if not file_path.exists():
            print(f"  SKIP: {file_path} nao encontrado")
            continue
        n = fix_file(file_path, opt_lines)
        print(f"  {file_rel}: +{n} inserts")
        total += n
    print(f"Total insertions: {total}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
