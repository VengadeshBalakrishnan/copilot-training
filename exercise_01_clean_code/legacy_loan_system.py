"""Loan calculator with cleaner naming and validation."""


def calculate_monthly_payment(principal, years, annual_rate):
    if principal <= 0:
        raise ValueError("Principal amount must be greater than zero.")
    if years <= 0:
        raise ValueError("Loan term in years must be greater than zero.")
    if annual_rate < 0:
        raise ValueError("Annual rate cannot be negative.")
    total_interest = principal * (annual_rate / 100) * years
    return (principal + total_interest) / (years * 12)


if __name__ == "__main__":
    print(f"Estimated monthly payment: ${calculate_monthly_payment(50000, 5, 8.5):.2f}")
