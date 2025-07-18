from collections import Counter

def firstNonRepeating(s: str) -> int:
    freq = Counter(s)
    return next((i for i, c in enumerate(s) if freq[c] == 1), -1)
