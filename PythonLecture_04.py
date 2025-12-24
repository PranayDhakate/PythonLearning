marks = int(input("How much marks did you got in total?\n"))

if(marks >= 90):
    print("Grade A")
elif(marks >= 80 and marks < 90):
    print("Grade B")
elif(marks >= 70 and marks < 80):
    print("Grade C")
elif(marks > 70):
    print("Grade D")
else:
    print("Invalid Marks!")