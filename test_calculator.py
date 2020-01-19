import unittest
import calculator


class TestCalculator(unittest.TestCase):
    def test_addition(self):
        assert 4 == calculator.add(2, 2)

    def test_subtraction(self):
        assert 2 == calculator.subtract(4, 2)

    def test_multiplication(self):
        assert 20 == calculator.multiply(4, 5)


if __name__ == '__main__':
    unittest.main()
