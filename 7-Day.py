import random
# Hangman
word_list=["aardvark","baboon","camel"]
chose_word= random.choice(word_list)
print(chose_word)

#TODO-1 Create Placholder with the same number of blanks as  the chose_word
placeholder =""
word_lenght=len(chose_word)
for position in range(word_lenght):
    placeholder += "-"

print(placeholder)


# ToDO-2
display= ""
guess =input("Guess a letter:").lower()
for letter in chose_word:
    if letter == guess:
        display += letter
    else:
        display +="-"
        
print(display)
# 6-09-2024
