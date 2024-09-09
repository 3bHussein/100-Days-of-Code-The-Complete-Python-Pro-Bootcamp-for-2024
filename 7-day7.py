#asdasd
import random


word_list=["apple","camel","aardvarka"]

chose_word=random.choice(word_list)
print(chose_word)
guess=input("guess the word \no").lower()

placeholder =""
word_lenght= len(chose_word)
for positon in range(word_lenght):
    placeholder +='-'

# print(placeholder)

display=""
for letter in chose_word:
    if letter== guess:
        display += letter
    else:
        display +="-"

print(display)
# 
