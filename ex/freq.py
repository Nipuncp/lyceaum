def freq(s):
    cnt = 0
    dic = {}
    for letter in s:
        dic[letter] = s.count(letter)
    return dic
