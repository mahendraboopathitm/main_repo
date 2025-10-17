# test_math_functions.py
import unittest
import functions   # import the file you want to test

class testing(unittest.TestCase):

    def test_add(self):
        self.assertEqual(math_functions.add(2, 3), 5)
        self.assertEqual(math_functions.add(-1, 1), 0)

    def test_multiply(self):
        self.assertEqual(math_functions.multiply(3, 4), 12)
        self.assertEqual(math_functions.multiply(0, 5), 0)

if __name__ == '__main__':
    unittest.main()
