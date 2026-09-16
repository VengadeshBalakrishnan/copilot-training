"""Example for generating a new banking feature."""


def validate_account_holder(account_holder, account_number):
    if not account_holder or len(account_holder.strip()) < 3:
        return False
    return account_number.isdigit() and len(account_number) == 10


if __name__ == "__main__":
    for account_holder, account_number in [("Ali", "1234567890"), ("A", "bad-account"), ("Sara", "9876543210")]:
        print(f"{account_holder} -> {validate_account_holder(account_holder, account_number)}")
