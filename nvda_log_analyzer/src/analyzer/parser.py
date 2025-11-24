from collections import Counter

def parse_log(path):
    with open(path, "r", encoding="utf8") as f:
        lines = f.readlines()

    filtered = []
    for line in lines:
        lower = line.lower()
        if "error" in lower or "exception" in lower or "failed" in lower:
            filtered.append(line.strip())

    counter = Counter(filtered)
    compressed = [f"{count} occurences of: {text}" for text, count in counter.items() ]

    return {
        "raw": filtered,
        "compressed": compressed
    }