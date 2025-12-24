age = int(input("What is your Age? \n"))

if(age>=21):
    print("You can vote and apply for licence.")
else:
    print("You are not in legal age.")
    
print("-------------------------")

color = input("what is the color?\n1>Green\n2>Yellow\n3>Red\n")

if(color == "Red"):
    print("Wait!")
elif(color == "Yellow"):
    print("Look!")
else:
    print("You can go now!")