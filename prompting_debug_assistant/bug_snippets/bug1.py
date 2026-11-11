# Goal: Return the last n elements from a list in their original order.

def last_n(items, n):
    if n < 0:
        raise ValueError("n must not be negative")
    if n > len(items):
        return items[:]

    return items[-n + 1:]


numbers = [10, 20, 30, 40, 50]
print("Last 2:", last_n(numbers, 2))
print("Expected:", [40, 50])
print("Last 0:", last_n(numbers, 0))
print("Expected:", [])
