from connection import connect

# DEFAULT_LOGIN_DETAILS
# PHONE_NO-8870350805
# PASSWORD-1234
def admin_login():
    try:
        c, con = connect()
    except Exception as e:
        print("Connection error in user:", e)
        return
    c.execute(
        "CREATE TABLE IF NOT EXISTS admin_details (ad_id INT, ad_user_name TEXT not null, ad_password TEXT not null, ad_phone VARCHAR(10), ad_mail TEXT not null, CHECK(length(ad_phone) = 10 AND ad_mail LIKE '%@%'),primary key (ad_id,ad_phone))")
    con.commit()
    c.execute("SELECT * FROM admin_details")
    admin = c.fetchall()
    if not admin:
        c.execute(
            "INSERT INTO admin_details(ad_id,ad_user_name,ad_password,ad_phone,ad_mail) values (1,'Srik','1234','8870350805','vsrik@gmail.com'")
        c.commit()
    c.execute(
        "CREATE TABLE IF NOT EXISTS student_details (s_id INT PRIMARY KEY AUTO_INCREMENT,s_user_name TEXT NOT NULL,s_password TEXT NOT NULL,s_phone VARCHAR(10) NOT NULL,father_name TEXT,mother_name TEXT,city TEXT,s_mail TEXT NOT NULL,s_grade VARCHAR(10) NOT NULL,fee_due DECIMAL(10, 2) DEFAULT 0,fee_paid DECIMAL(10, 2) DEFAULT 0)")
    con.commit()
    try:
        print("_____enter login details______")
        ph = input("Enter your phone number: ")
        pas = input("Enter your password: ")

        try:
            c.execute("SELECT * FROM admin_details WHERE ad_phone=%s AND ad_password=%s", (ph, pas))
            result = c.fetchall()
            if not result:
                print("No user found")
            else:
                print("_________Login Success_________")
                admin_features(c, con)
        except Exception as e:
            print("Admin fetching error:", e)
        finally:
            c.close()
            con.close()
    except Exception as e:
        print("Admin login details error:", e)


def admin_features(c, con):
    try:
        while True:
            t = input(
                "\n1->Create new admin\n2->Create new teacher\n3->Create new student\n4->delete a admin\n5->delete a teacher\n6->delete Student\n7->view  details of teacher\n8->view  details of Student\n9->fee_add\n10->Exit\nEnter your Choice")
            if t == '1':
                user = input("Enter the username: ")
                pas = input("Enter the password: ")
                ph = input("Enter the phone number: ")
                mail = input("Enter the email address: ")
                c.execute(
                    "INSERT INTO admin_details (ad_user_name, ad_password, ad_phone, ad_mail) VALUES (%s, %s, %s, %s)",
                    (user, pas, ph, mail))
                con.commit()
                print("New admin added successfully!")
                c.fetchall()
            elif t == '2':
                c.execute(
                    "CREATE TABLE IF NOT EXISTS teacher_details (t_id INT, t_user_name TEXT not null, t_password TEXT not null, t_phone VARCHAR(10), t_mail TEXT not null,t_qualification TEXT not null,CHECK(length(t_phone) = 10 AND t_mail LIKE '%@%'),primary key (t_id,t_phone))")
                con.commit()
                t_id = int(input("Enter teacher ID: "))
                t_user_name = input("Enter teacher username: ")
                t_password = input("Enter teacher password: ")
                t_phone = input("Enter teacher phone number: ")
                t_mail = input("Enter teacher email: ")
                t_qualification = input("Enter teacher qualification: ")
                c.execute(
                    "INSERT INTO teacher_details (t_id, t_user_name, t_password, t_phone, t_mail, t_qualification)VALUES (%s, %s, %s, %s, %s, %s)",
                    (t_id, t_user_name, t_password, t_phone, t_mail, t_qualification))
                con.commit()
                print("Data inserted successfully!")
            elif t == '3':
                s_user_name = input("Enter student username: ")
                s_password = input("Enter student password: ")
                s_phone = input("Enter student phone number: ")
                s_mail = input("Enter student email: ")
                s_grade = input("Enter student grade: ")
                c.execute(
                    "INSERT INTO student_details (s_user_name, s_password, s_phone, s_mail, s_grade)VALUES (%s, %s, %s, %s, %s)",
                    (s_user_name, s_password, s_phone, s_mail, s_grade))
                con.commit()
            elif t == '4':
                cph = input("enter admin phone number to delete: ")
                print("_____enter Admin login details to delete______")
                ph = input("Enter your phone number: ")
                pas = input("Enter your password: ")
                c.execute("SELECT * FROM admin_details WHERE ad_phone=%s AND ad_password=%s", (ph, pas))
                result = c.fetchall()
                if not result:
                    print("can't delete without proper permission")
                else:
                    ch = c.execute("select *from admin_details where ad_phone=%s", (cph,))
                    result = ch.fetchall()
                    if not result:
                        print("not such customer found")
                    else:
                        cf = input("all records of admin will be deleted\n1->confirm\n 2->Cancel\n")
                        if cf == '1':
                            c.execute("delete from admin_details where ad_phone=%s", cph)
                            con.commit()
                            print("full admin details records has been deleted")
                        elif cf == '2':
                            print("delete has been cancelled")
                            pass
            elif t == '5':
                t_id = input("Enter teacher ID to delete: ")
                print("Enter Admin login details to delete")
                ph = input("Enter your phone number: ")
                pas = input("Enter your password: ")
                c.execute("SELECT * FROM admin_details WHERE ad_phone=%s AND ad_password=%s", (ph, pas))
                result = c.fetchall()
                if not result:
                    print("Can't delete without proper permission")
                else:
                    c.execute("SELECT * FROM teacher_details WHERE t_id=%s", (t_id,))
                    result = c.fetchall()
                    if not result:
                        print("No such teacher found")
                    else:
                        cf = input("All records of teacher will be deleted\n1->confirm\n2->Cancel\n")
                        if cf == '1':
                            c.execute("DELETE FROM teacher_details WHERE t_id=%s", (t_id,))
                            con.commit()
                            print("Teacher record has been deleted successfully")
                        elif cf == '2':
                            print("Delete has been cancelled")
                            pass
            elif t == "6":
                s_id = input("Enter student ID to delete: ")
                print("Enter Admin login details to delete")
                ph = input("Enter your phone number: ")
                pas = input("Enter your password: ")
                c.execute("SELECT * FROM admin_details WHERE ad_phone=%s AND ad_password=%s", (ph, pas))
                result = c.fetchall()
                if not result:
                    print("Can't delete without proper permission")
                else:
                    c.execute("SELECT * FROM student_details WHERE s_id=%s", (s_id,))
                    result = c.fetchall()
                    if not result:
                        print("No such student found")
                    else:
                        cf = input("All records of student will be deleted\n1->confirm\n2->Cancel\n")
                        if cf == '1':
                            c.execute("DELETE FROM student_details WHERE s_id=%s", (s_id,))
                            con.commit()
                            print("Student record has been deleted successfully")
                        elif cf == '2':
                            print("Delete has been cancelled")
                            pass
            elif t == "7":
                c.execute("SELECT * FROM teacher_details")
                teachers = c.fetchall()
                if not teachers:
                    print("No teachers found")
                else:
                    print("Teacher Details:")
                    for teacher in teachers:
                        print(
                            f"ID: {teacher[0]}, Username: {teacher[1]}, Phone: {teacher[3]}, Email: {teacher[4]}, Qualification: {teacher[5]}")
            elif t == "8":
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
            elif t == '9':
                try:
                    s_id = input("Enter student ID to update fee due: ")
                    c.execute("select * from student_details where s_id = %s", (s_id,))
                    result = c.fetchall()
                    if not result:
                        print("No Student Record Found")
                    else:
                        fee_due = float(input("Enter new fee due amount: "))
                        c.execute("UPDATE student_details SET fee_due = %s WHERE s_id = %s", (fee_due, s_id))
                        con.commit()
                        print("Fee due updated successfully!")
                except Exception as e:
                    print("Error updating fee due:", e)
            elif t == "10":
                break
    except Exception as e:
        print("Admin Connection Error", e)
