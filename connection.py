import mysql.connector as sq


def connect():
    try:
        con = sq.connect(
            host="localhost",
            user="root",
            password="1234",
            database="school",
            port=3307,
            auth_plugin='mysql_native_password'
        )
        c = con.cursor()
        return c, con
    except Exception as e:
        print("Connection error:", e)
