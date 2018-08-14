import string
def ari(f):
    num_words = 0
    num_char = 0
    num_sentence = 0
    txt = open(f)
    file_read = txt.read()
    words = str.split(file_read)
    for i in words:
        num_char += len(i)
    num_words = len(words)
    num_sentence = file_read.count('.')
    index = 4.71*(num_char/num_words) + 0.5*(num_words/num_sentence) -21.43
    print(num_sentence,num_words,num_char)


    return index

def ari(f):

    txt = open(f)
    file_read = txt.read()

    
    words = str.split(file_read)
    for i in words:
        num_char += len(i)
    num_words = len(words)
    num_sentence = file_read.count('.')
    index = 4.71*(num_char/num_words) + 0.5*(num_words/num_sentence) -21.43
    print(num_sentence,num_words,num_char)


    return index
