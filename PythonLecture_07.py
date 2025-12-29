'''
dictionary data structure stores valuein the form of Key - Value
It takes all data types
Their is no order in distionary
For nested dist we can create distionary in value part as below
'''


info = {
    "key" : "vaue",
    "name" : "pranay",
    "age" : 27,
    "language" : ["Python", "C++", "Java"],
    "topics" : ("Set", "Dict")
}

print(info)
print(type(info))

print(info["name"])

#Nested Dict
stud = {
    "name" : "Sejal",
    "age" : 24,
    "sub" : {
        "phy" : 17,
        "chem" : 12.25,
        "maths" : 19.75
    }
}

print((stud))
print()