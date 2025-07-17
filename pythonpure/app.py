
print("Airtel Store app is running...")

#lets create a list
age = 20

list1 = ["geeks","for","geeks2"]
print("The list is :",list1)

print("The zero index value of my list is ",list1[0])
print("the index of 0 to 4 datas are",list1[0:4])
print("The backward index is ",list1[::-1])

myset = set(["geeks", "for", "geeks2"])
print("The set is :", myset)

# Sets don't support indexing, so we'll convert to list for demonstration
myset_list = list(myset)
print("The first element of my set (converted to list) is ", myset_list[0])
print("The backward order of my set (converted to list) is ", myset_list[::-1])

#this is a comment 
#lets take input from user

#conditional statements
if(age.isdigit() and int(age) < 18):
    print("You are a minor.")
elif(age.isdigit() and int(age) >= 18):
    print("You are an adult.")
else:
    print("Invalid age input.Please enter a valid number")

def hello(name):
    print("Hello,",name,"Welcome to Airtel Store app!")
    print("Where technology meets convenience.")
    print("We have a wide range of products and services to choose from.")

def goodbye(name):
    print("Goodbye,",name,"! Thank you for visiting Airtel Store app.")
    print("We hope to see you again soon!")

# Call the hello function
def Main():
    print("Started the Airtel Store app")
    name = input('Enter your name: ')
    class1 = input("Enter your class: ")
    age = input("Enter your age")

    print("My name is "+name +" i am in class "+ class1 +"and i am "+age +" years old")
    hello(name)
    goodbye(name)

if __name__ == "__main__":
    Main()
else:       
    print("Airtel Store app is not running as the main module.")

#looping/iterations
for i in range(5):
    print("The item in the list is apple", i)

print("while loop")
while(i < 5):
    print("The item in the list is apple", i)
    i += 1


#catching exceptions
try:
    print("This is a try block")
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError as e:
    print("Caught an exception:", e)    
finally:
    print("This is the finally block, which always executes.")

#from __future__ import division
print(7/5)  # This will perform true division, resulting in 1.4
print(7//5)  # This will perform floor division, resulting in 1

#multiple line statements
print("This is a long statement that can be split across multiple lines " 
   "using parentheses, allowing for better readability and organization.")

"""
This is a multi-line comment.
It can span multiple lines and is useful for providing detailed explanations or documentation.
"""
# Importing necessary modules
import math
import random   


# Using the math module to calculate square root
print("The square root of 16 is:", math.sqrt(16))
# Using the random module to generate a random number
print("A random number between 1 and 10 is:", random.randint(1, 10))
# Using the random module to shuffle a list
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print("Shuffled list:", my_list)    
# Using the random module to choose a random element from a list
random_choice = random.choice(my_list)
print("Randomly chosen element from the list:", random_choice)
# Using the random module to sample multiple elements from a list
random_sample = random.sample(my_list, 3)
print("Random sample of 3 elements from the list:", random_sample)  
# Using the random module to generate a random float
random_float = random.uniform(1, 10)
print("Random float between 1 and 10:", random_float)   
# Using the random module to generate a random float with a specific range
random_float_range = random.uniform(5, 15)
print("Random float between 5 and 15:", random_float_range)

#converting to list tuple and set functions
s = {books, "pen", "pencil", "eraser"}
tuple1 = tuple(s)
print("The set is:", s)
set1 = set(tuple1)
print("The tuple is:", tuple1)
list1 = list(set1)
print("The list is:", list1)
