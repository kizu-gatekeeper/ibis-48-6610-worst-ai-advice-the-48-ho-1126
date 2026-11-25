"""Entry for make.fun: Worst AI Advice: The 48-Hour Tight Line Open.

One confident, tidy, terrible tip in a single tight line.
"""
import os

LINE = "Pro tip: if your code will not compile, just delete the error messages - no errors means it works, and standup gets much shorter."
MAX_CHARS = 140


def write_entry(out_dir):
    if not LINE.strip() or "\n" in LINE or len(LINE) > MAX_CHARS:
        raise ValueError("entry must be one non-empty line within the limit")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


def main():
    write_entry(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


if __name__ == "__main__":
    main()
