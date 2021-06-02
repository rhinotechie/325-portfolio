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

    def test_personal1(self):
        input_string = ""
        input_p = ""
        self.assertEqual(True, patternmatch(input_string, input_p))

    def test_personal2(self):
        input_string = ""
        input_p = "**"
        self.assertEqual(True, patternmatch(input_string, input_p))

    def test_personal3(self):
        input_string = "abc"
        input_p = "*bc"
        self.assertEqual(True, patternmatch(input_string, input_p))

    def test_personal4(self):
        input_string = "abcdedf"
        input_p = "a*df"
        self.assertEqual(True, patternmatch(input_string, input_p))

    def test_personal5(self):
        input_string = "a"
        input_p = "?"
        self.assertEqual(True, patternmatch(input_string, input_p))

    def test_personal6(self):
        input_string = "abc"
        input_p = "???"
        self.assertEqual(True, patternmatch(input_string, input_p))

    def test_personal7(self):
        input_string = "abcde"
        input_p = "?b?d?"
        self.assertEqual(True, patternmatch(input_string, input_p))

    def test_personal8(self):
        input_string = "abcde"
        input_p = "a*?e"
        self.assertEqual(True, patternmatch(input_string, input_p))

    def test_personal9(self):
        input_string = "abcde"
        input_p = "a?*?e"
        self.assertEqual(True, patternmatch(input_string, input_p))

    def test_personal10(self):
        input_string = "ababab"
        input_p = "?*?*b"
        self.assertEqual(True, patternmatch(input_string, input_p))

    def test_personal11(self):
        input_string = "abcde"
        input_p = "??????"
        self.assertEqual(False, patternmatch(input_string, input_p))

    def test_personal12(self):
        input_string = "abcdeffffffcd"
        input_p = "a*cd"
        self.assertEqual(True, patternmatch(input_string, input_p))

    def test_personal13(self):
        input_string = ""
        input_p = "*?*"
        self.assertEqual(False, patternmatch(input_string, input_p))

    def test_personal14(self):
        input_string = "abcdefgh"
        input_p = "*???"
        self.assertEqual(True, patternmatch(input_string, input_p))

    def test_personal15(self):
        input_string = "abcdef"
        input_p = "a*b?**?f"
        self.assertEqual(True, patternmatch(input_string, input_p))


if __name__ == '__main__':
    unittest.main()
