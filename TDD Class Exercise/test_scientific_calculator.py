import unittest
import math
from scientific_calculator import sin, cos, tan, sqrt, log, exp

class TestScientificCalculator(unittest.TestCase):

    # Tests for sin function
    def test_sin_positive_input(self):
        """Test sin with positive input (e.g., sin(90))"""
        self.assertAlmostEqual(sin(90), math.sin(math.radians(90)), places=7)

    def test_sin_negative_input(self):
        """Test sin with negative input (e.g., sin(-90))"""
        self.assertAlmostEqual(sin(-90), math.sin(math.radians(-90)), places=7)

    def test_sin_zero_input(self):
        """Test sin with zero input (e.g., sin(0))"""
        self.assertAlmostEqual(sin(0), math.sin(0), places=7)

    def test_sin_error_non_numeric_input(self):
        """Test sin with non-numeric input"""
        with self.assertRaises(TypeError):
            sin("hello")

    # Tests for cos function
    def test_cos_positive_input(self):
        """Test cos with positive input (e.g., cos(0))"""
        self.assertAlmostEqual(cos(0), math.cos(math.radians(0)), places=7)

    def test_cos_negative_input(self):
        """Test cos with negative input (e.g., cos(-90))"""
        self.assertAlmostEqual(cos(-90), math.cos(math.radians(-90)), places=7)

    def test_cos_zero_input(self):
        """Test cos with zero input (e.g., cos(0))"""
        self.assertAlmostEqual(cos(0), math.cos(0), places=7)

    def test_cos_error_non_numeric_input(self):
        """Test cos with non-numeric input"""
        with self.assertRaises(TypeError):
            cos("hello")

    # Tests for tan function
    def test_tan_positive_input(self):
        """Test tan with positive input (e.g., tan(45))"""
        self.assertAlmostEqual(tan(45), math.tan(math.radians(45)), places=7)

    def test_tan_negative_input(self):
        """Test tan with negative input (e.g., tan(-45))"""
        self.assertAlmostEqual(tan(-45), math.tan(math.radians(-45)), places=7)

    def test_tan_zero_input(self):
        """Test tan with zero input (e.g., tan(0))"""
        self.assertAlmostEqual(tan(0), math.tan(0), places=7)

    def test_tan_error_non_numeric_input(self):
        """Test tan with non-numeric input"""
        with self.assertRaises(TypeError):
            tan("hello")

    def test_tan_error_undefined_value(self):
        """Test tan for undefined values (e.g., tan(90))"""
        with self.assertRaises(ValueError):
            tan(90)

    # Tests for sqrt function
    def test_sqrt_positive_input(self):
        """Test sqrt with positive input (e.g., sqrt(4))"""
        self.assertAlmostEqual(sqrt(4), math.sqrt(4), places=7)

    def test_sqrt_zero_input(self):
        """Test sqrt with zero input (e.g., sqrt(0))"""
        self.assertAlmostEqual(sqrt(0), math.sqrt(0), places=7)

    def test_sqrt_error_negative_input(self):
        """Test sqrt with negative input"""
        with self.assertRaises(ValueError):
            sqrt(-1)

    def test_sqrt_error_non_numeric_input(self):
        """Test sqrt with non-numeric input"""
        with self.assertRaises(TypeError):
            sqrt("hello")

    # Tests for log function
    def test_log_positive_input(self):
        """Test log with positive input (e.g., log(10))"""
        self.assertAlmostEqual(log(10), math.log10(10), places=7)

    def test_log_error_zero_input(self):
        """Test log with zero input"""
        with self.assertRaises(ValueError):
            log(0)

    def test_log_error_negative_input(self):
        """Test log with negative input"""
        with self.assertRaises(ValueError):
            log(-1)

    def test_log_error_non_numeric_input(self):
        """Test log with non-numeric input"""
        with self.assertRaises(TypeError):
            log("hello")

    # Tests for exp function
    def test_exp_positive_input(self):
        """Test exp with positive input (e.g., exp(1))"""
        self.assertAlmostEqual(exp(1), math.exp(1), places=7)

    def test_exp_negative_input(self):
        """Test exp with negative input (e.g., exp(-1))"""
        self.assertAlmostEqual(exp(-1), math.exp(-1), places=7)

    def test_exp_zero_input(self):
        """Test exp with zero input (e.g., exp(0))"""
        self.assertAlmostEqual(exp(0), math.exp(0), places=7)

    def test_exp_error_non_numeric_input(self):
        """Test exp with non-numeric input"""
        with self.assertRaises(TypeError):
            exp("hello")

if __name__ == '__main__':
    unittest.main()
