print("Hello Bhai")


name = "Pranay"
age = 27
gender = "Male"
passed = False
travel = None


print(type(name))
print(type(age))
print(type(gender))
print(type(passed))
print(type(travel))

"""
Data Types
Integers
String
Float
Boolean
None


Note: Python is a case sensitive languages
"""

# sum
a = 10
b = 2

print("Sum ", a+b) #Sum
print( a*b) #Multiply
print(a/b) #Divide
print(a%b) #Remaimder
print(a**b) #Power

num = 10
#num = num + 10 Below code means the same
num += 10
print(num)


#Type Conversion & Type Casting

a = 2
b = 7.12

sum = a + b
print(round(sum,2))

x = 10
y = "5"
add = x + int(y)
print(add)

#Take input from user

Name = input("What is your name?")
print("Welcome ", Name)

age = input("What is your age? ")
print(type(age), age)

print(type(int(age)),age)
#Note: Input in python takes all values as input in string format then we have to type cast it.
