#                                    ***Dictionary***
# d = {}
# print(d, type(d))

# methods of diction
# stu = {
#     "yaya" : "Khan",         
#     "program" : "Bscs", 
#      "score" : 100
# }
# print(stu, type(stu))
# print(stu["yaya"])

# print( stu. items())  # items ka use krny pe value and key dno 1 bracket me miln gy
# print( stu. keys())   # keys use krny c hamen first column me likhi hoe chez miln gi like "yaya, program, marks etc"
# print( stu. values()) # isko use krny c hmn keys ki just values miln g

# stu.update({"score" : 99})
# print(stu["marks"])

# print(stu.get("yaya"))        # is me student ka nam ghlt likhny pe "none" show ho ga
# print(stu["yaya"])              # is me student ka nam ghlt likhny pe "error" show ho ga_

# clear dic
p = {
    "a" : 1,
    "b": 2,
}
p.clear()
# shallow copy
q = {
    "ab" : 1,
    "ba": 2,
}
r = q.copy()
print(q, r)

