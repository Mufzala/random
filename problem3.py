#           ***use F string***

# name = input("enter your name: ")
# age = input ("Enter your age: ")
# food = input ("Enter your favourite food: ")
# color = input("Enter your favourite color: ")
# field = input("Enter your field: ")

# print(f"Hello {name}, \n you are {age} years old, \n {food} is your favourite food, \n {color} is your favourite color, \n your field is {field} " )

#           *** using "F string" in math***

# import math 
# radius = float(input("Enter the radius of the circle: "))
# area = math.pi * radius ** 2
# print(f"The radisu of the circle is: {radius}, \nThe area of the circle is: {area}")

#               *** replace function***
# letter = ''' Dear <|Name|>
#                  You are selected!
#                  <|Date|>'''
# print(letter.replace("<|Name|>", "Yaya").replace("<|Date|>", "24 oct 2025"))

#               *** find triple space and repalce with single space ***
#                                           ***find and replace ***

# a = " Yaya is a good   girl "
# print(a.replace("   ", " "))
# print (a.find ("girl"))

#                   *** Escape character***
letter = "Dear Yaya, \n\tYou are so sweet.\nThanks! "

print(letter)

