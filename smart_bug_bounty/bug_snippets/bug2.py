"""Bug 2: calculate average of valid numeric scores."""


def average_score(scores):
    if not scores:
        return 0.0

    total = 0.0
    count = 0
    for score in scores:
        if isinstance(score, (int, float)) and not isinstance(score, bool):
            if 0 <= score <= 100:
                total += score
                count += 1

    if count == 0:
        return 0.0
    return round(total / len(scores), 2)


if __name__ == "__main__":
    print(average_score([80, 90, None]))
    print(average_score([70, 80, 90]))
    print(average_score(["absent", None]))
