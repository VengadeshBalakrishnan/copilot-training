"""Example for documenting banking security validation."""


def validate_pin(pin):
    """Validate a four-digit debit card PIN that is not four identical digits."""
    if len(pin) != 4 or not pin.isdigit():
        return False
    return len(set(pin)) > 1


if __name__ == "__main__":
    print(validate_pin("4826"))
