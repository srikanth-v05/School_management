# student.py
from connection import connect

def student_login():
    try:
        c, con = connect()
    except Exception as e:
        print("Connection error:", e)
        return
    try:
        print("_____enter login details______")
        ph = input("Enter your phone number: ")
        pas = input("Enter your password: ")

        try:
            c.execute("SELECT * FROM student_details WHERE s_phone=%s AND s_password=%s", (ph, pas))
            result = c.fetchall()
            if not result:
                print("No user found")
            else:
                print("_________Login Success_________")
                student_features(c, con)
        except Exception as e:
            print("Student fetching error:", e)
        finally:
            c.close()
            con.close()
    except Exception as e:
        print("Student login details error:", e)

def student_features(c, con):
    while True:
        try:
            t = input("\n1->View My Details\n2->View My Results\n3->Pay Fee\n4->Exit")
            if t == '1':
                student_id = input("Enter student ID to view details: ")
                c.execute("SELECT * FROM student_details WHERE s_id = %s", student_id)
                student = c.fetchone()
                if not student:
                    print("Student not found")
                else:
                    print("Student Details:")
                    print(f"ID: {student[0]}")
                    print(f"Username: {student[1]}")
                    print(f"Password: {student[2]}")
                    print(f"Phone: {student[3]}")
                    print(f"Email: {student[4]}")
                    print(f"Grade: {student[5]}")
                    print(f"Father's Name: {student[6]}")
                    print(f"Mother's Name: {student[7]}")
                    print(f"City: {student[8]}")
                    print(f"Fee Due: {student[9]}")
                    print(f"Fee Paid: {student[10]}")
            elif t == '2':
                try:
                    student_id = input("Enter student ID to view exam results: ")
                    c.execute("SELECT * FROM exam_results WHERE student_id = %s", (student_id,))
                    exam_results = c.fetchall()
                    if not exam_results:
                        print("No exam results found for this student")
                    else:
                        print("Exam Results:")
                        for result in exam_results:
                            print(f"Subject: {result[2]}")
                            print(f"Date: {result[3]}")
                            print(f"Score: {result[4]}")
                except Exception as e:
                    print("Error:", e)
            elif t == '3':
                try:
                    student_id = input("Enter student ID: ")
                    fee_due = float(input("Enter fee amount to pay: "))
                    c.execute("SELECT fee_due, fee_paid FROM student_details WHERE s_id = %s", (student_id,))
                    current_due, fee_paid = c.fetchone()
                    if fee_due > current_due:
                        print("Invalid amount. Please enter an amount less than or equal to the due amount.")
                    else:
                        new_due = current_due - fee_due
                        new_paid = fee_paid + fee_due
                        c.execute("UPDATE student_details SET fee_due = %s, fee_paid = %s WHERE s_id = %s",
                                  (new_due, new_paid, student_id))
                        con.commit()
                        print("Fee paid successfully!")
                except Exception as e:
                    print("Error:", e)
            elif t == '4':
                break

        except Exception as e:
            print("Error:", e)
