import unittest
from Palindrome import checkPalindrome_1


class MyTestCase(unittest.TestCase):
    def test_example1(self):
        input_string = "abcba"
        input_number = 3
        self.assertEqual(True, checkPalindrome_1(input_string, input_number))


if __name__ == '__main__':
    unittest.main()
