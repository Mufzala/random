#                                            *** list***
fruits = ["Apple", "Banana", "Orange", "grapes", "Mango"]
num = [0 , 4,  6 , 7 ,9, 22, 12, 45]
name = ["Yaya", "Hama", "Bhaiya", "Mano", "Maan"]   #list
print(type(name))

no = num.count(45)
print (no)

a = num.index(22)
print (a)

repeated = num
print (repeated)

#          *** Indexing/Slicing ***

# fruits[3] = "pomegrant"
# print(fruits[3])

# print(num[2:7])
# num[5] = 55
# print(num[5])

# print(name[1:4:2])
# num[2] = "hamiiee"
# print(name[2])


# print(f"Your favourite fruits is: {fruits},\nSome digits are: {num}, \nSome students names are: {name}")

#           *** Append function ***
# name.append("The End")
# print (name)

#           ***Sort function ***
# name.sort()
# print(name)

# fruits.sort()
# print(fruits)

#           *** Reverse/sort function ***
# num.sort()
# num.reverse()
# print(num)

#           *** insert/delete function ***
# num.insert(3, 333)
# num.pop(4)
num.remove(45)
print (num)