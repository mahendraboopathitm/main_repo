# test_math_functions.py
import unittest
import functions   # import the file you want to test

class testing(unittest.TestCase):

    def test_add(self):
        self.assertEqual(functions.add(2, 3), 5)
        self.assertEqual(functions.add(-1, 1), 0)

    def test_multiply(self):
        self.assertEqual(functions.multiply(3, 4), 12)
        self.assertEqual(functions.multiply(0, 5), 0)

if __name__ == '__main__':
    unittest.main()
