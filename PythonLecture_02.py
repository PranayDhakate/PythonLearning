#String

str1 = "This is a String"
str2 = 'My name is Pranay'
str3 = "My mother's name is Megha"

print (str1 ,"\n", str2)

#Escape sequence characters
# \n used for nextline
# \t used for tab

#String concatenation
fname = "Pranay"
lname = "Dhakate"

print(fname + " " + lname)

#Length functn (Space is also calculated in len function)

print(len(fname))

#Indexing (Starts with 0 to n)
City = "Nagpur"
print(City[4])

#Slicing string 
homeTown = "Chandrapur"
print(homeTown[0:4])

print(homeTown[1:len(homeTown)]) # same as str[1: ]
print(homeTown[ : 4]) #same as str[0:4]
print(homeTown[-1:-1])