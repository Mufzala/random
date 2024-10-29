#                                   ***Sets***

s = {4,6,5,6,4,3,7,9,1}
e = set()       # dnt use {} curly braces to make empty set because it create empty dictionary
print(s, type(s))

# methods of set

r = {4,6,5,6,4,3,7,9,1, "yaya", "maan"}
# add
r.add("Mano")
# remove 
r.remove(1)
# pop
r.pop() # that is used for removing random number in the set  *(most it is not used in the programs)*
# union
print(s.union(r))
# intersection
print(s.intersection(r))
# subset
print({3,4}.issubset(r))
print(r.issubset({3}))
# supperset
print(r.issuperset({3}))
# print(r)
