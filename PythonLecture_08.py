#For Loop


loop1 = [1,2,3,4,5,6,54,212]


for i in loop1:
    print(i)
    
# existing list
numbers = [10, 20, 30, 40]

# take input from user
num = int(input("Enter a number to add to the list: "))

# create a new list and copy elements using for loop
new_list = []

for n in numbers:
    new_list.append(n)

# add the user input
new_list.append(num)

print("Updated list:", new_list)



#While Loop

count = 0

while count <= 5:
    print("Hello ")
    count += 1
    
for i in range(10):
    print(i)