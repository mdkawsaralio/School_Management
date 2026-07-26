import csv
import os

import pandas as pd

class student:
    def __init__ (self,name,roll,class_name,address):
        self.name=name
        self.roll=roll
        self.class_name=class_name
        self.address=address


class student_data:
    def add_student(self,student):
    
        if not os.path.exists("student.csv"):
            read=pd.DataFrame(columns=["name","roll","class_name","address"])
            read.to_csv("student.csv",index=False)

        read=pd.read_csv("student.csv")
        if ((read["name"]==student.name) & (read["roll"]== student.roll)).any():   
            print("Student has already exists in database")
            return
        
        with open ("student.csv","a", newline="") as data:
            writer=csv.writer(data)
            writer.writerow([student.name,student.roll, student.class_name,student.address])
            print("Student is Successfully Added to the Database")
    
    def remove_student(self,student):
        if not os.path.exists("student.csv"):
            print("There is no database")
            return
        read=pd.read_csv("student.csv")
        for index,row in read.iterrows():
            if row["name"]==student.name and row["roll"]==student.roll:
                read=read.drop(index)
                read.to_csv("student.csv",index=False)    # index=False prevents pandas from saving the DataFrame's index as a column in the CSV.            print("Successfully Deleted")
                print("Successfully Deleted")
                return
        print("Student is not in the databae")


    def student_info(self,student):
        if not os.path.exists("student.csv"):
            print("There is no Database")
            return

        read=pd.read_csv("student.csv")
        for index,row in read.iterrows():
            if row["name"]==student.name and row["roll"]==student.roll:
                print(row)
                return
        print("Student not found")

    def search_student (self, student):
        if not os.path.exists("student.csv"):
            print("There is no database")
            return
        read=pd.read_csv("student.csv")
        for index,row in read.iterrows():
            if row["name"]==student.name and row["roll"]==student.roll:
                print("Student Found")
                return
        print("Student is not in Database")

    def view_all (self):
        if not os.path.exists("student.csv"):
            print("There is no database")
            return
        read=pd.read_csv("student.csv")
        print(read)
        return
    def update_info(self,current_student,new_student):
        if not os.path.exists("student.csv"):
            print("There is no database")
            return
        read=pd.read_csv("student.csv")
        for index,row in read.iterrows():
            if row["roll"]==current_student.roll:
                read.loc[index,"name"]=new_student.name
                read.loc[index, "roll"]=new_student.roll
                read.loc[index,"class_name"]=new_student.class_name
                read.loc[index,"address"]=new_student.address

                read.to_csv("student.csv",index=False)
                print("Information Successfully Updated")
                return
        print("student does not exists")
        
print("Wellcome to Student Management")
print("1. Add New Student")
print("2. Remove Student")
print("3. Update Student Info")
print("4. Student info")
print("5. View all student")
print("6. Search Student")
print("7. Exit")

while(True):
    choice=int(input("Enter Input: "))
    if choice ==1:
        try:
            name=input("Enter Student Name: ")
            roll=int(input("Enter Student Roll: "))
            class_name=input("Enter Class name: ")
            address=input("Enter Address of the student: ")
            students=student(name,roll,class_name,address)
            student_data().add_student(students)
        except ValueError:
            print("Please Enter data Correctly")
    if choice ==2:
        try:
            name=input("Enter Student Name: ")
            roll=int(input("Enter Student Roll: "))
            students=student(name,roll,None,None)
            student_data().remove_student(students)

        except:
            print("Please Enter data Correctly")
    if choice==3:
        try:
            roll=int(input("Enter Current student Roll: "))
            new_name=input("Enter New student Name: ")
            new_roll=int(input("Enter New student Roll: "))
            new_class_name=input("Enter new class name: ")
            new_address=input("Enter New Address: ")
            new_student=student(new_name,new_roll,new_class_name,new_address)
            current_student=student(None,roll,None,None)
            student_data().update_info(current_student,new_student)

        except ValueError:
            print("Please Enter data Correctly")
    if choice==4:
        try:
            name=input("Enter Student Name: ")
            roll=int(input("Enter Student Roll: "))
            students=student(name,roll,None,None)
            student_data().student_info(students)
        except:
            print("Please Enter data Correctly")
    if choice ==5:
        student_data().view_all()
    
    if choice ==6:
        try:
            name=input("Enter Student Name: ")
            roll=int(input("Enter Student Roll: "))
            students=student(name,roll,None,None)
            database=student_data().search_student(students)

        except:
            print("Please Enter data Correctly")
    if choice ==7:
        print("Thank's for visiting Student Management")
        break

    


    