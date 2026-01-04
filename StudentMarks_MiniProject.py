#count number of students

numofStudents = int(input("Enter Total Students: "))

#Data Storage

studentData = []

#inserting data

for i in range(numofStudents):
    print(f"Enter the data of Student {i+1}")
    name = input("Name: ")
    roll_no = int(input("Roll Number: "))
    marks = int(input("Marks: "))
    
    if marks > 95:
        grades = "A"
    elif marks > 85:
        grades = "B"
    elif marks > 60:
        grades = "C"
    elif marks > 35:
        grades = "D"
    else:
        grades = "F"
    
    students = {
        "name" : name,
        "roll_no" : roll_no,
        "marks" : marks,
        "grades" : grades
    }
    
    studentData.append(students)

#Data Printing
print("All Student Data: \n")
for s in studentData:
    print(f"{s['name']} - Roll Num: {s['roll_no']} - Marks: {s['marks']} - Grades: {s['grades']}")

#Passed Students
print("\n Student who are passed: ")

for j in studentData:
    if j['marks'] >= 35:
        print(f"{j['name']} - {j['marks']}")