import student
import os

class PrintMeny:
    
    def __init__(self):
        self.studentList = []


    def addStudent(self):
        os.system('cls')
        print("---------------------------------------------------------------------------- \n\n\t\t\t-- Add Student --")
        addStudentName = input(f"\n\n\tInput Student's name: ")
        addStudentEdu = input(f"\n\tInput Student's Education: ")
        addStudentPhone = input(f"\n\tInput Student's Phone Number: ")

        currStudent = student.student(addStudentName, addStudentEdu, addStudentPhone)

        self.studentList.append(currStudent)

    # Prints a list of students sorted by their first name
    def print_studentList(self):
        os.system('cls')
        self.studentList = sorted(self.studentList, key=lambda p: p.name)
        print("---------------------------------------------------------------------------- \n\n\t\t\t-- Student List --")

        i = 1
        for student in self.studentList:
            print(f"\n\t{i}. {student.get_student()}")
            i = i + 1 

    def del_student(self):
        #!
        # Removes the student one number after the one displayed... fix later?? maybe.
        #!
        os.system('cls')
        print("----------------------------------------------------------------------------\n\n\t\t\t -- Remove Student --")
        i = 1
        for student in self.studentList:
            print(f"\n\t{i}. {student.get_student()}")
            i = i + 1 
        menuInput = input(f"\n\tSelect Which student you want to remove: ")
        try:
            val = int(menuInput)
        except ValueError:
            input(f"\n\tPlease enter a valid student")
            self.del_student()
        else:
            val - 1
            self.studentList.pop(val)
            self.print_studentList()
            input(f"\n\tPress any key to exit")


    # Prints the main menu
    def testprint(self):
        os.system('cls')
        print("----------------------------------------------------------------------------\n\n\t\t\t -- Student Terminal --")
        print(f"\n\n\t\t1. Add Student \n\t\t2. Del Student \n\t\t3. Print Student List \n\t\t4. Exit")

        menuInput = input("\n\tInput: ")

        if (menuInput == "1"):
            os.system('cls')
            self.addStudent()
   
        elif (menuInput == "2"):
            self.del_student()

        elif (menuInput == "3"):   
            self.print_studentList()
            menuSelect = input("\n\tPress any key to exit:")


        return menuInput 
    
        

    
        


    

