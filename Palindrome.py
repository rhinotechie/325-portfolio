# Bruteforce approach
def checkPalindrome_1(string, k):
    # Not a palindrome if empty.
    if string == "":
        return False

    # Is the current substring a palindrome?
    if string == string[::-1]:
        return True

    # Checks if substring is a palindrome for at least one child substring up to k characters removed from original
    results = []
    if k > 0:
        for position in range(0, len(string)):
            sub_string = string[:position] + string[position + 1:]
            results.append(checkPalindrome_1(sub_string, k - 1))

    # No matches found
    if True in results:
        return True
    else:
        return False


# Dynamic programming with top down approach with memoization.
def checkPalindrome_2(string, k):
    string_memo = {}
    return helper_2(string, k, string_memo)


# Helper function for improved palindrome approach.
def helper_2(string, k, string_memo):
    # Not a palindrome if empty.
    if string == "":
        return False

    # Is this an overlapping sub-problem that has been solved?
    if string in string_memo:
        return False

    # Is the current substring a palindrome?
    if string == string[::-1]:
        return True

    # Checks if substring is a palindrome for at least one child substring up to k characters removed from original
    if k > 0:
        for position in range(0, len(string)):
            sub_string = string[:position] + string[position + 1:]
            if checkPalindrome_1(sub_string, k - 1):
                return True

    # No matches found
    string_memo[string] = False
    return False


if __name__ == "__main__":
    input_string = "abcba"
    input_number = 3
    print(checkPalindrome_2(input_string, input_number))
