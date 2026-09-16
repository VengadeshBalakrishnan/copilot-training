"""Version 2: pattern-based bank authentication with validation and reuse."""


class BankAuthenticator:
    _VALID_USERS = {"Aisha": "4826", "Ravi": "7319"}

    def authenticate(self, account_holder, pin):
        if not account_holder or not pin:
            raise ValueError("Account holder and PIN are required.")
        if account_holder not in self._VALID_USERS:
            return False
        return self._VALID_USERS[account_holder] == pin


if __name__ == "__main__":
    authenticator = BankAuthenticator()
    print(authenticator.authenticate("Aisha", "4826"))
    print(authenticator.authenticate("Ravi", "7319"))
