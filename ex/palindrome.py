def palindrome(s):
    reverse = s[::-1]
    if s == reverse:
        return True
    else:
        return False


def palindrome(s):
    return s == s[::-1]
