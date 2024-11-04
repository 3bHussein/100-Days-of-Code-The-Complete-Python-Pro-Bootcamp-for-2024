#Simple Function
def greet():
  print("Hello Angela")
  print("How do you do Jack Bauer?")
  print("Isn't the weather nice today?")
greet()

#Function that allows for input
#'name' is the parameter.
#'Jack Bauer' is the argument.
def greet_with_name(name):
  print(f"Hello {name}")
  print(f"How do you do {name}?")
greet_with_name("Jack Bauer")

#Functions with more than 1 input
def greet_with(name, location):
  print(f"Hello {name}")
  print(f"What is it like in {location}?")

#Calling greet_with() with Positional Arguments
greet_with("Jack Bauer", "Nowhere")
#vs.
greet_with("Nowhere", "Jack Bauer")


#Calling greet_with() with Keyword Arguments
greet_with(location="London", name="Angela")
# 



def add(x ,y):
  total=x+y
  print(total)



add(5,6)



def welcome(name):
  # print("welcome ",name)
  print(f'welcome {name} ')
  # print(name)
  
# x=input('enter your name \n')  
# welcome(x)

def greet_with(name,location):
  # print(f'welcome {name}')
  print("welcome ",input('enter your'))
  print(f'what is it like {location}')
  
# greet_with('ahmed','alexandria')
greet_with(name='ahmed',location='alex')





def hello(name):
  print('you almost welcome ',name)
  print(f'you alway welcome {name}')

hello('Havel')
# KeyWord Arguments
def total(x,y,z):
  print('your X',x) #5
  print('your Y',y) #6
  print('your Z',z) #7

# Old Way
total(5,6,7)
# KeyWord Arguments
total(z=5,y=7,x=6)

# 

# Caesar  Cipher 

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char.isalpha():
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
  print(f"Here's the {cipher_direction}d result: {end_text}\n")

run = True
while run:
  # print(logo)
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  if shift > 26:
    shift = shift % shift == 0

  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  choice = input("Do you want to run this program again?\nType 'yes' or 'no': ")
  if choice == 'no':
    run = False
    print("Goodbye.")
    
    