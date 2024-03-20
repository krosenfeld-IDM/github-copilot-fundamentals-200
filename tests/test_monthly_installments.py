import unittest
from project import calculate_amortization  # replace 'your_module' with the actual module name

class TestAmortizationCalculation(unittest.TestCase):
    def test_zero_interest_rate(self):
        self.assertAlmostEqual(calculate_amortization(100000, 0, 10), 833.33, places=2)

    def test_zero_years(self):
        with self.assertRaises(ValueError):  # assuming the function raises ValueError for invalid input
            calculate_amortization(100000, 5, 0)

    def test_zero_principal(self):
        self.assertEqual(calculate_amortization(0, 5, 10), 0)

    def test_typical_case(self):
        self.assertAlmostEqual(calculate_amortization(100000, 5, 10), 1054.61, places=2)

    def test_high_interest_rate(self):
        self.assertAlmostEqual(calculate_amortization(100000, 20, 10), 1321.51, places=2)

    def test_non_integer_loan_term(self):
        with self.assertRaises(ValueError):
            calculate_amortization(100000, 5, 10.5)

    def test_negative_values(self):
        with self.assertRaises(ValueError):
            calculate_amortization(-100000, 5, 10)
        with self.assertRaises(ValueError):
            calculate_amortization(100000, -5, 10)
        with self.assertRaises(ValueError):
            calculate_amortization(100000, 5, -10)

            
if __name__ == '__main__':
    unittest.main()