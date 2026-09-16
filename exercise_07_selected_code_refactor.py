"""Example for refactoring a banking transaction analysis."""


def do_work(transaction_amounts):
    total = sum(amount for amount in transaction_amounts if amount > 0)
    avg = total / len(transaction_amounts) if transaction_amounts else 0
    print("Total:", total)
    print("Average:", avg)
    return total, avg


def sum_deposits(transaction_amounts):
    return sum(amount for amount in transaction_amounts if amount > 0)


def calculate_average_transaction(transaction_amounts):
    return sum(transaction_amounts) / len(transaction_amounts) if transaction_amounts else 0


def analyze_transactions(transaction_amounts):
    return sum_deposits(transaction_amounts), calculate_average_transaction(transaction_amounts)


if __name__ == "__main__":
    print(analyze_transactions([100, -20, 50, 70, 0]))
