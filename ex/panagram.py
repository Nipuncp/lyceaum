NUM_ALPHA = 26

def panagram(s):

    pan = 0
    phrase = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for letter in s:     
        for char in alphabet :
            if char == letter and char not in phrase:
                phrase+=char
    for char in phrase:
        for letter in alphabet:
            if char == letter:
                pan += 1
    if pan==NUM_ALPHA:
        return True
    else:
        print(phrase, alphabet)
        return False
    


def panagram(s):
    for i in "abcdefghijklmnopqrstuvwxyz":
        if i not in s:
            return False
    return True
