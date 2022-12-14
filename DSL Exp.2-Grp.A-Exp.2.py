'''
Experiment Number 2 : Write a python program to store marks stored in subject "Fundamentals of Data Structure"
                         by N students in the class. Write functions to compute following:
                         1. The average score of the class.
                         2. Highest score and lowest score of the class.
                         3. Count of students who were absent for the test.
                         4. Display mark with highest frequency.
'''


def absentSC(listOfStudent, numberOfStudent):
    count = 0
    for i in range(numberOfStudent):
        if listOfStudent[i]==0:
            count +=1
    return count       

def maxMarks(listOfStudent, numberOfStudent):
    max = 0
    for i in range(numberOfStudent):
        if max<listOfStudent[i]:
            max = listOfStudent[i]

    return max

def largestMFreq(numberOfStudent, listOfStudent):
    count = 0
    check = maxMarks(listOfStudent, numberOfStudent)
    
    for i in range(numberOfStudent):
        if check == listOfStudent[i]:
            count += 1
    return count

def minMFreq(numberOfStudent, listOfStudent):
    count = 0
    check = minMarks(listOfStudent, numberOfStudent)
    
    for i in range(numberOfStudent):
        if check == listOfStudent[i]:
            count += 1
    return count

def minMarks(listOfStudent, numberOfStudent):
    min = listOfStudent[0]
    for i in range(numberOfStudent):
        if min>listOfStudent[i]:
            min = listOfStudent[i]

    return min

def averageOfMarks(listOfStudent, numberOfStudent):
    sumInitialize = 0
    for i in range(numberOfStudent):
        sumInitialize += listOfStudent[i]

    return (sumInitialize/numberOfStudent)

loop = True
listOfStudent = []   
numberOfStudent = int(input("Enter No of Student: "))
count = 1
    
for i in range(numberOfStudent):
    marks = int(input(f"Enter marks for student {count}: "))
    listOfStudent.append(marks)
    count+=1

def showList():
    print("Select Your Choice From Following list:- \n1)Average Marks\n2)Maximum Marks\n3)Minimum Marks\n4)Maximum Marks Frequency\n5)Minimum Marks Frequency\n6)Count Of Absent Student\n7)Create New List Of Marks\n8)Exit")
showList()

while loop:
    choice = input("Enter your choice: ")
    if choice == "1":
        print("Average marks obtained by student is:",averageOfMarks(listOfStudent, numberOfStudent))    
    elif choice == "2":
        print("Maximum marks obtained by student is: ",maxMarks(listOfStudent, numberOfStudent))   
    elif choice == "3":
        print("Minimum marks obtained by student is: ",minMarks(listOfStudent, numberOfStudent))
    elif choice == "4":
        print(f"{maxMarks(listOfStudent, numberOfStudent)} is largest marks and its frequency is: ",largestMFreq(numberOfStudent, listOfStudent))       
    elif choice == "5":
        print(minMarks(listOfStudent, numberOfStudent), " is minimum marks and its frequency is: ",minMFreq(numberOfStudent, listOfStudent))       
    elif choice == "6":
        print("Number of absent student are: ", absentSC(listOfStudent, numberOfStudent))      
    elif choice == "7":
        print("New list created")
        listOfStudent = [] 
        numberOfStudent = int(input("Enter No of Student: "))
        count = 1
        for i in range(numberOfStudent):
            marks = int(input(f"Enter marks for student {count}: "))
            listOfStudent.append(marks)
            count+=1
        print("Select Your Choice From Following list:- \n1)Average Marks\n2)Maximum Marks\n3)Minimum Marks\n4)Maximum Marks Frequency\n5)Minimum Marks Frequency\n6)Count Of Absent Student\n7)Create New List Of Marks\n8)Exit")
    elif choice == "8":
        loop = False
    else:
        print("You entered wrong choice try again")
