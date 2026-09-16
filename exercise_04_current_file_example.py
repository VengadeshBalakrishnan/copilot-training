"""Bank account example for Exercise 4: Understand Current File (#file)."""


def process_account_names(account_names):
    """Return a cleaned list of account holder names."""
    cleaned = []
    for item in account_names:
        name = str(item).strip()
        if name:
            cleaned.append(name.lower())
    return cleaned


def find_high_balance_accounts(accounts, threshold):
    """Return accounts whose balance is above the given threshold."""
    return [account for account in accounts if account["balance"] > threshold]


if __name__ == "__main__":
    account_list = [{"holder": "Aisha", "balance": 1200}, {"holder": "Ravi", "balance": 25}, {"holder": "Mina", "balance": 75}]
    names = process_account_names([" Aisha ", "Ravi", "  ", "Mina "])
    print(names)
    print(find_high_balance_accounts(account_list, 100))
