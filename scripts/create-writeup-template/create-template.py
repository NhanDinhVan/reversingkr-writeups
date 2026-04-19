#!/usr/bin/env python3

from __future__ import annotations

import argparse
import sys
from pathlib import Path


TEMPLATE = """# [Challenge Name] - Write-up

## 1. Overview
- **Platform:** reverse.kr
- **Category:** Reverse Engineering
- **Difficulty:** (Easy / Medium / Hard)
- **Link:** (if available)

**Short Description:**
> Briefly describe the challenge in 1-2 sentences.

---

## 2. Initial Analysis

### File Information
- File type:
- Tools used:
  - `file`
  - `strings`
  - `checksec` (if applicable)

### First Observations
- Packed?
- Obfuscation?
- Interesting strings:

```
(paste relevant strings here)
```

---

## 3. Static Analysis

### Tools
- IDA / Ghidra / Binary Ninja

### Structure Analysis
- Entry point:
- Main function:
- Important functions:

### Notes
- What does the program do?
- Where is the core logic?

---

## 4. Dynamic Analysis

### Tools
- x64dbg / gdb

### Observations
- Breakpoints:
- Register values:
- Memory behavior:
- Execution flow:

---

## 5. Reversing Logic

### Algorithm Analysis
- Password validation logic:
- Any encoding/encryption:

```python
# example
def check(input):
    return input ^ 0x1234 == 0x5678
```

---

## 6. Solution

### Steps
1. ...
2. ...
3. ...

### Script (if any)
```python
# solve script
```

---

## 7. Result

- **Flag / Password:**

```
FLAG{...}
```
"""


def slugify(name: str) -> str:
    cleaned = name.strip().lower().replace(" ", "-")
    return "".join(char for char in cleaned if char.isalnum() or char in {"-", "_"})


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create a reversing write-up template.")
    parser.add_argument("challenge_name", help="Challenge name used for the folder and title.")
    parser.add_argument(
        "output_directory",
        help="Directory where the challenge folder will be created.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite write-up.md if it already exists.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    base_path = Path(args.output_directory)
    challenge_dir = base_path / slugify(args.challenge_name)
    evidence_dir = challenge_dir / "image-evidences"
    writeup_path = challenge_dir / "write-up.md"

    challenge_dir.mkdir(parents=True, exist_ok=True)
    evidence_dir.mkdir(parents=True, exist_ok=True)

    if writeup_path.exists() and not args.force:
        print(f"write-up already exists: {writeup_path}", file=sys.stderr)
        return 1

    writeup_path.write_text(
        TEMPLATE.replace("[Challenge Name]", args.challenge_name.strip()),
        encoding="utf-8",
    )

    print(f"created: {challenge_dir}")
    print(f"created: {evidence_dir}")
    print(f"created: {writeup_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
