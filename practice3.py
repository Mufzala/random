name = "yaya khan"


 #length of the name
print (len(name)) 

#indexing from right to left starting from (-1,-2,-3,...)
print (name[-4 : -1]) 

# indexing form left to right starting fromm (0,1,2...)
print (name[0:2]) 


print (name.endswith("a"))      #name end with "a" =true
print (name.capitalize())         # 1st letter capital
print (name.startswith("m"))  # name start with "m" = false
print(name.title())                  # 1st letter of every word is capital


index = name.find("khan")
print (index) 

replaced_string = name.replace ("khan", "Sajid")
print (replaced_string)

print (name)

a = "yaya is a good girl\n and not a bad girl"
b = "yaya is a good girl \t and not a bad girl"
c = "yaya is a good girl \n and not a 'bad' girl"

print (a)
print (b)
print (c)