# Bruteforce approach
def checkPalindrome_1(string, k):
    if string == string[::-1]:
        return True

    # Checks if this substring is a palindrome for at least one child substring up to k characters removed from original
    if k > 0:
        for position in range(0, len(string)):
            sub_string = string[position - 1:] + string[position:]
            checkPalindrome_1(sub_string, k - 1)

    # No matches found
    return False


# Improved
def checkPalindrome_2(string, k):
    pass


if __name__ == "__main__":
    input_string = "abcba"
    input_number = 3
    print(checkPalindrome_1(input_string, input_number))