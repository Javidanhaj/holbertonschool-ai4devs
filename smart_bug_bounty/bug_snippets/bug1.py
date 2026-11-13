"""Bug 1: return the last n items without modifying the input."""


def last_items(items, n):
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must not be negative")
    if n == 0:
        return []
    if n > len(items):
        return items[:]
    return items[-n + 1:]


if __name__ == "__main__":
    examples = [
        ([10, 20, 30, 40], 2),
        ([1, 2, 3], 1),
        ([1, 2, 3], 0),
    ]
    for values, count in examples:
        print(last_items(values, count))
