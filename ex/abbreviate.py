def abbreviate(s):
    caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    abbr = []
    for char in s:
        if char in caps:
            abbr += char
    return abbr


    
