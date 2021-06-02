# This function assumes that 'string' does not have '?' or '*' inside of it, only 'p'
def patternmatch(string, p):
    # Base case
    if (p == "" and string == "") or p == string or (p == "*" and string == ""):
        return True
    
    if p == "" or (string == "" and p != "*"):
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
