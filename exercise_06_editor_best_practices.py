"""Example for banking validation and labeling improvements."""


def validate_account_number(account_number):
    return account_number.isdigit() and len(account_number) == 10


def get_customer_label(name, account_type):
    if account_type == "premium":
        return "Premium customer: " + name
    return "Standard customer: " + name


if __name__ == "__main__":
    print(validate_account_number("1234567890"))
    print(get_customer_label("Aisha", "premium"))
