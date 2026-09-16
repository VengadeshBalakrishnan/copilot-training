import unittest
from unittest.mock import patch

import main


class TestCalculator(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(main.add(2, 3), 5)

    def test_subtract_positive_numbers(self):
        self.assertEqual(main.subtract(8, 3), 5)

    def test_multiply_positive_numbers(self):
        self.assertEqual(main.multiply(4, 5), 20)

    def test_divide_positive_numbers(self):
        self.assertEqual(main.divide(8, 2), 4)

    def test_divide_by_zero(self):
        with self.assertRaisesRegex(ValueError, "Cannot divide by zero"):
            main.divide(8, 0)

    def test_valid_numeric_input(self):
        self.assertEqual(main.validate_numeric_input("4.5"), 4.5)

    def test_invalid_numeric_input(self):
        with self.assertRaisesRegex(ValueError, "Invalid numeric input"):
            main.validate_numeric_input("not-a-number")

    @patch("builtins.input", side_effect=["8", "/", "0"])
    def test_main_reports_division_by_zero(self, mock_input):
        with patch("builtins.print") as mock_print:
            main.main()
        mock_print.assert_any_call("Error: Cannot divide by zero")


if __name__ == "__main__":
    unittest.main()
