"""Compare two approaches for calculating total deposits."""


def approach_one(deposit_amounts):
    total = 0
    for amount in deposit_amounts:
        total += amount
    return total


def approach_two(deposit_amounts):
    return sum(deposit_amounts)


if __name__ == "__main__":
    sample = [100, 200, 300, 400, 500]
    print("Approach 1:", approach_one(sample))
    print("Approach 2:", approach_two(sample))
