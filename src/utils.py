
from pathlib import Path
def count_lines(path):
    total = 0
    for p in Path(path).rglob("*.py"):
        with open(p, "r", encoding="utf-8") as f:
            total += sum(1 for _ in f)
    return total
