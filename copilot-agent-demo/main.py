"""Simple command-line calculator."""


def validate_numeric_input(value):
    """Return a number when value is numeric, otherwise raise ValueError."""
    try:
        return float(value)
    except (TypeError, ValueError) as error:
        raise ValueError(f"Invalid numeric input: {value}") from error


def add(first, second):
    return first + second


def subtract(first, second):
    return first - second


def multiply(first, second):
    return first * second


def divide(first, second):
    if second == 0:
        raise ValueError("Cannot divide by zero")
    return first / second


def main():
    operations = {"+": add, "-": subtract, "*": multiply, "/": divide}
    print("Simple Calculator")
    print("Supported operations: +, -, *, /")
    try:
        first = validate_numeric_input(input("First number: "))
        operation = input("Operation: ").strip()
        second = validate_numeric_input(input("Second number: "))
        if operation not in operations:
            print("Error: unsupported operation")
            return
        print(f"Result: {operations[operation](first, second)}")
    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
