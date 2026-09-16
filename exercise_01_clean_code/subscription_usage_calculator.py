"""Bank account fee example for usage-based transaction pricing."""


def calculate_account_fee(monthly_fee, included_transactions, transaction_count, transaction_rate):
    if monthly_fee < 0:
        raise ValueError("Monthly fee cannot be negative.")
    if included_transactions < 0:
        raise ValueError("Included transactions cannot be negative.")
    if transaction_count < 0:
        raise ValueError("Transaction count cannot be negative.")
    if transaction_rate < 0:
        raise ValueError("Transaction rate cannot be negative.")
    extra_transactions = max(0, transaction_count - included_transactions)
    return monthly_fee + extra_transactions * transaction_rate


if __name__ == "__main__":
    print(f"Monthly account fee: ${calculate_account_fee(25, 100, 140, 1.5):.2f}")
