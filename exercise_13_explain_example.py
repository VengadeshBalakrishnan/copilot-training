"""Example used for /explain prompts about banking transactions."""


def count_even_transactions(transaction_amounts):
    return sum(1 for amount in transaction_amounts if amount % 2 == 0)


if __name__ == "__main__":
    print(f"Even transactions: {count_even_transactions([101, 202, 303, 404, 505, 606])}")
