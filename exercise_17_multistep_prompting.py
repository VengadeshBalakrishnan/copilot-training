"""Example for multi-step prompting with interest validation and error handling."""


def calculate_simple_interest(principal, annual_rate, years):
    if principal < 0:
        raise ValueError("Principal cannot be negative.")
    if annual_rate < 0:
        raise ValueError("Annual rate cannot be negative.")
    if years < 0:
        raise ValueError("Years cannot be negative.")
    return principal * (annual_rate / 100) * years


if __name__ == "__main__":
    try:
        print(calculate_simple_interest(2000, 5, 2))
        print(calculate_simple_interest(-5, 5, 2))
    except ValueError as error:
        print(f"Error: {error}")
