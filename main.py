# CREATE DATABASE IN MYSQL - SCHOOL
from admin import admin_login
from teacher import teacher_login
from student import student_login

if __name__ == "__main__":
    print("_________WELCOME TO SCHOOL________")
    try:
        while True:
            op = input("1->Admin\n2->Teacher\n3->Student\n4->Exit\nEnter Your Option")
            if op == '1' or op.lower() == "admin":
                admin_login()
            elif op == '2' or op.lower() == "teacher":
                teacher_login()
            elif op == '3' or op.lower() == "student":
                student_login()
            elif op == '4' or op.lower() == 'exit':
                break
    except Exception as e:
        print("Error occurred:", e)
