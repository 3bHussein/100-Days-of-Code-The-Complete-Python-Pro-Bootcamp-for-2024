#asdasd
import random


word_list=["apple","camel","aardvarka"]

chose_word=random.choice(word_list)
print(chose_word)



placeholder =""
word_lenght= len(chose_word)
for positon in range(word_lenght):
    placeholder +='-'

# print(placeholder)
gameover=False
correct_letter=[]

while not gameover:
    guess=input("guess the word \n").lower()

    display=""
    for letter in chose_word:
        if letter== guess:
            display += letter
        else:
            display +="-"

    print(display)
    if "_" not in display:
        gameover=True
        print("you Win")
    else:
# 
#
