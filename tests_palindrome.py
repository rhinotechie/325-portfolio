import unittest
from Palindrome import checkPalindrome_2


class MyTestCase(unittest.TestCase):
    def test_example1(self):
        input_string = "abcba"
        input_number = 3
        self.assertEqual(True, checkPalindrome_2(input_string, input_number))

    def test_example2(self):
        input_string = "abcdeba"
        input_number = 2
        self.assertEqual(True, checkPalindrome_2(input_string, input_number))

    def test_personal1(self):
        input_string = ""
        input_number = 10
        self.assertEqual(False, checkPalindrome_2(input_string, input_number))

    def test_personal2(self):
        input_string = "a"
        input_number = 10
        self.assertEqual(True, checkPalindrome_2(input_string, input_number))

    def test_personal3(self):
        input_string = "ab"
        input_number = 0
        self.assertEqual(False, checkPalindrome_2(input_string, input_number))

    def test_personal4(self):
        input_string = "ab"
        input_number = 1
        self.assertEqual(True, checkPalindrome_2(input_string, input_number))

    def test_personal5(self):
        input_string = "cbba"
        input_number = 1
        self.assertEqual(False, checkPalindrome_2(input_string, input_number))

    def test_personal6(self):
        input_string = "eabcdeecba"
        input_number = 3
        self.assertEqual(True, checkPalindrome_2(input_string, input_number))

    def test_personal7(self):
        input_string = "eabcdeecba"
        input_number = 2
        self.assertEqual(True, checkPalindrome_2(input_string, input_number))

    def test_personal8(self):
        input_string = "abcd"
        input_number = 2
        self.assertEqual(False, checkPalindrome_2(input_string, input_number))


if __name__ == '__main__':
    unittest.main()
