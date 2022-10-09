#JenniferChu
#1873159

word = input()
word_rev = word[::-1]
if ' ' not in word:
    if word == word_rev:
        print(word, 'is a palindrome')
    else:
        print(word, "is not a palindrome")
else:
    no_space = word.replace(' ','')
    no_space_rev = no_space[::-1]
    if no_space == no_space_rev:
        print(word, 'is a palindrome')
    else:
        print(word, "is not a palindrome")