# This function assumes that 'string' does not have '?' or '*' inside of it, only 'p'
def patternmatch(string, p):
    # Base case: a matching pattern is found
    if p == "" and string == "":
        return True

    # Case where p possibly has only '*'s left while string is empty.
    if string == "" and p[0] == "*":
        return patternmatch("", p[1:])

    # If string still has remaining characters or there are leftover '?' in 'p'.
    if p == "" or (p[0] == '?' and string == ""):
        return False

    # Do the first characters match?
    if p[0] == string[0] or p[0] == '?':
        return patternmatch(string[1:], p[1:])

    # The wildcard is (1) "", (2) ends on sub-string's first char, (3) ends after sub-string's first char
    if p[0] == '*':
        return patternmatch(string, p[1:]) or patternmatch(string[1:], p[1:]) or patternmatch(string[1:], p)

    return False


if __name__ == "__main__":
    input_string = "abcde"
    input_p = "*"
    print(patternmatch(input_string, input_p))
