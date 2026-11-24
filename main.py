"""Write one funny developer excuse to entry.txt.

Deterministic: the line is fixed, written as a single line with no
trailing newline, as the bounty gate requires (1-200 characters).
"""

import os

# The winning excuse (86 chars, one line, no trailing newline).
LINE = "The bug only happens in production because staging is too polite to tell me the truth."


def write_entry(out_dir):
    """Write the excuse to entry.txt in out_dir."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    return path


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    write_entry(out_dir)


if __name__ == "__main__":
    main()
