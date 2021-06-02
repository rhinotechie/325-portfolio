import unittest
from Patternmatch import patternmatch


class MyTestCase(unittest.TestCase):
    def test_example1(self):
        input_string = "abcde"
        input_p = "*"
        self.assertEqual(True, patternmatch(input_string, input_p))

    def test_example2(self):
        input_string = "abcde"
        input_p = "*a?c*"
        self.assertEqual(True, patternmatch(input_string, input_p))

    def test_example3(self):
        input_string = "abcde"
        input_p = "ad"
        self.assertEqual(False, patternmatch(input_string, input_p))

    def test_example4(self):
        input_string = "abcde"
        input_p = "ad?"
        self.assertEqual(False, patternmatch(input_string, input_p))


if __name__ == '__main__':
    unittest.main()
