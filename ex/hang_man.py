import random

def secret_word():
    wordfile = "/usr/share/dict/words"
    min_length = 6
    
    good_words = []
    f = open(wordfile)
    for i in f:
        word = i.strip()
        if word.isalpha() and len(word) >= min_length:
            good_words.append(word)
    f.close()
    
    return random.choice(good_words)


secret = secret_word()



print (secret_word)
s = 0
tries = 10
guess =  ['_' for i in range(len(secret_word))]
print(guess)
print(f"Let's play the hangman word game. You have {tries} tries remaining, please enter a letter to guess the word")
guess_letter = input()
for i in guess:
    for j in secret_word:
        if guess_letter == j:
            guess[s] = guess_letter
            s += 1
      
     # print (guess)

    
print(guess)        
