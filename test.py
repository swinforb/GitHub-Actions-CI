import unittest
import example


class TestCase(unittest.TestCase):

    def test_add_1(self):
        self.assertEqual(example.add(1, 2), 3)

    def test_subtract_1(self):
        self.assertEqual(example.subtract(1, 1), 0)

    def test_multiply_1(self):
        self.assertEqual(example.division(4, 2), 8)

    def test_divde_1(self):
        self.assertEqual(example.divide(6, 3), 2)


if __name__ == '__main__':
    unittest.main()
