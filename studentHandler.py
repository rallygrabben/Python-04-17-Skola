import student

class PrintMeny:
    
    def __init__(self):
        self.studentList = []


    def addStudent(self):
        print("\n\n\n\n\n\n\n\n\n----------------------------------------------------------------")
        addStudentName = input(f"\n\n\tInput Student's name: ")
        addStudentEdu = input(f"\n\tInput Student's Education: ")
        addStudentPhone = input(f"\n\tInput Student's Phone Number: ")

        currStudent = student.student(addStudentName, addStudentEdu, addStudentPhone)

        self.studentList.append(currStudent)

    def print_studentList(self):
        self.studentList = sorted(self.studentList, key=lambda p: p.name)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n----------------------------------------------------------------")
        print(f"\n\n\t--ElevLista--")

        for student in self.studentList:
            print(f"\n\t\t{student.get_student()}")

    def testprint(self):
        print("----------------------------------------------------------------")
        print(f"\n\n\t\t1. Add Student \n\t\t2. Del Student \n\t\t3. Print Student List \n\t\t4. Exit")

        menyInput = input(f"")

        if (menyInput == "1"):
            self.addStudent()
            print("")
   
        elif (menyInput == "2"):
            print("DelElev")
        elif (menyInput == "3"):    
            self.print_studentList()
        
        return menyInput 
    
        

    
        


    

