
'''
Note:
1) Strings are immutable in python
2) Lists are mutable in python
'''


marks1 = 91.1
marks2 = 92.2
marks3 = "91.9"
marks4 = 92.2
marks5 = 96.4
marks6 = "94.3"

#List It can store data of different data types.
marks = [marks1,marks2,marks3,marks4,marks5,marks6]
print(type(marks))
print(marks)
print(len(marks))

studentInfo = ["Pranay", 27, "Male"]
print(studentInfo)
print(studentInfo[0])

studentInfo[0] = "Golu"
print(studentInfo)

print("============List Functions============")

list = [6,2,1,4,5,2,7,9,0]
list.append(9)
print(list)

list.sort()
print(list)

list.sort(reverse=True)
print(list)

list.insert(1,3)
print(list)

list.remove(9)
print(list)

list.pop(-2)
print(list)