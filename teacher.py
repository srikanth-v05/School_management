from connection import connect


def teacher_login():
    try:
        c, con = connect()
        print("_____enter login details______")
        ph = input("Enter your phone number: ")
        pas = input("Enter your password: ")
        c.execute(
            "CREATE TABLE IF NOT EXISTS exam_results (result_id INT PRIMARY KEY AUTO_INCREMENT,student_id INT,exam_subject VARCHAR(50),exam_date DATE,exam_score FLOAT,FOREIGN KEY (student_id) REFERENCES student_details(s_id))")
        con.commit()
        try:
            c.execute("SELECT * FROM teacher_details WHERE t_phone=%s AND t_password=%s", (ph, pas))
            result = c.fetchall()
            if not result:
                print("No user found")
            else:
                print("_________Login Success_________")
                teacher_features(c, con)
        except Exception as e:
            print("Teacher fetching error:", e)
        finally:
            c.close()
            con.close()
    except Exception as e:
        print("Teacher login details error:", e)


def teacher_features(c, con):
    while True:
        t = input(
            "\n1->view  details of teacher\n2->view  details of Student\n3->add details of Student\n4->exam result\n5->Exit")
        if t == '1':
            c.execute("SELECT * FROM teacher_details")
            teachers = c.fetchall()
            if not teachers:
                print("No teachers found")
            else:
                print("Teacher Details:")
                for teacher in teachers:
                    print(
                        f"ID: {teacher[0]}, Username: {teacher[1]}, Phone: {teacher[3]}, Email: {teacher[4]}, Qualification: {teacher[5]}")
        elif t == '2':
            c.execute("SELECT * FROM student_details")
            students = c.fetchall()
            if not students:
                print("No students found")
            else:
                print("1->All Student\n2->Particular Grade")
                k = int(input("\nEnter Your Choice"))
                if k == "1":
                    print("Student Details:")
                    for student in students:
                        print(
                            f"ID: {student[0]}, Username: {student[1]}, Phone: {student[3]}, Email: {student[4]}, Grade: {student[5]}")
                elif k == '2':
                    grade = int(input("Enter the Grade"))
                    c.execute("SELECT * FROM student_details WHERE s_grade = %s", (grade,))
                    students = c.fetchall()
                    if not students:
                        print(f"No students found for grade {grade}")
                    else:
                        print(f"Student Details for Grade {grade}:")
                        for student in students:
                            print(
                                f"ID: {student[0]}, Username: {student[1]}, Phone: {student[3]}, Email: {student[4]}, Grade: {student[5]}")
        elif t == '3':
            try:
                s_id = input("Enter student ID to update details: ")
                father_name = input("Enter father's name: ")
                mother_name = input("Enter mother's name: ")
                city = input("Enter city: ")
                c.execute("UPDATE student_details SET father_name = %s, mother_name = %s, city = %sWHERE s_id = %s",
                          (father_name, mother_name, city, s_id))
                con.commit()
                print("Student details updated successfully!")
            except Exception as e:
                print("Error:", e)

        elif t == '4':

            try:
                student_id = input("Enter student ID: ")
                exam_subject = input("Enter exam subject: ")
                exam_date = input("Enter exam date (YYYY-MM-DD): ")
                exam_score = float(input("Enter exam score: "))
                c.execute(
                    "INSERT INTO exam_results (student_id, exam_subject, exam_date, exam_score)VALUES (%s, %s, %s, %s)",
                    (student_id, exam_subject, exam_date, exam_score))
                con.commit()
                print("Exam result added successfully!")
            except Exception as e:
                print("Error:", e)
        elif t == "5":
            break
