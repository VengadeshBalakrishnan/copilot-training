"""Version 1: improved bank login readability and validation."""


def authenticate_account(account_holder, pin):
    if not account_holder or not pin:
        raise ValueError("Account holder and PIN are required.")
    return account_holder == "Aisha" and pin == "4826"


if __name__ == "__main__":
    print(authenticate_account("Aisha", "4826"))
