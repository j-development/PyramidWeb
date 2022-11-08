import calculator  # The code to test
import unittest  # The test framework


class Test_TestCalculatorAdd(unittest.TestCase):
    def test_add1(self):
        self.assertEqual(calculator.add(3, 4), 7)

    def test_add2(self):
        self.assertNotEqual(calculator.add(3, 6), 10)

    def test_multiply1(self):
        self.assertNotEqual(calculator.multiply(10, 25), 125)
        
    def test_multiply1(self):
        self.assertEqual(calculator.multiply(5, 25), 125)


if __name__ == "__main__":
    unittest.main()
