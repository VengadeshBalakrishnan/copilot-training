"""Example for bug-fix practice with bank transfer validation."""


def calculate_transfer_share(amount, account_count):
    if account_count <= 0:
        raise ValueError("Account count must be greater than zero.")
    return amount / account_count


if __name__ == "__main__":
    try:
        print(calculate_transfer_share(100, 2))
        print(calculate_transfer_share(80, 0))
    except ValueError as error:
        print(f"Handled error: {error}")
