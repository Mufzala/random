friends = ("Yaya", "Hama", "Bhaiya")
name = ( "Mano", "Maan")
number = (3,5,6,7,8,12,22.34,34,34,45,55)
num = [8,12,22.34,34,34]

# concatenation
print(friends + name)
print(friends[1])
print(name[-2])

# membership with "IN" or "Not In"
print("Mano" in name) 
print("Maha" not in name)

# unpacking
a, b, c = friends
print(b,c,a)

# max and min
print(max(number))
print(min(number))

# convert tuple to list
my_list = list(number)
print(my_list)

# convert list to tuple
my_tuple = tuple(num)
print(my_tuple)


#type of friends
print (type(friends))

