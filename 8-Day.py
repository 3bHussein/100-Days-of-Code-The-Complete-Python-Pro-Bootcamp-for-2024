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

   
  #  