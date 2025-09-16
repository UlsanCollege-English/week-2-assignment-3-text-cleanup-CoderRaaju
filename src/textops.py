from typing import List


def unique_words_preserve_order(words: List[str]) -> List[str]:
    """Return first occurrences only (case-sensitive)."""
    seen = set()
    result = []
    for w in words:
        if w not in seen:
            seen.add(w)
            result.append(w)
    return result


def top_k_frequent_first_tie(words: List[str], k: int) -> List[str]:
    """Return up to k words ordered by frequency (high to low).

    For ties, earlier first-appearance wins.
    If k <= 0, raise ValueError.
    """
    if k <= 0:
        raise ValueError("k must be > 0")

    # count frequencies
    freq = {}
    first_seen = {}
    for i, w in enumerate(words):
        freq[w] = freq.get(w, 0) + 1
        if w not in first_seen:
            first_seen[w] = i

    # sort by (-frequency, first_seen index)
    sorted_words = sorted(freq.keys(), key=lambda w: (-freq[w], first_seen[w]))

    return sorted_words[:k]


def redact_words(words: List[str], banned: List[str]) -> List[str]:
    """Return a new list where every word in `banned` is replaced by "***".

    Exact matches only; case-sensitive.
    """
    banned_set = set(banned)
    return ["***" if w in banned_set else w for w in words]
