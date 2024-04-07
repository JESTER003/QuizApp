# import mysql.connector as c
# import mysql


# def insert(username, password):
#     """Inserts user data into the database.

#     Args:
#         username: The username to insert.
#         password: The password to insert.
#     """
#     try:
#         con = c.connect(
#             host="localhost", user="root", passwd="gujjup_0003_3114", database="quizapp"
#         )
#         cursor = con.cursor()
#         query = "INSERT INTO st (name, passs ,score) VALUES (%s, %s,%s)"
#         cursor.execute(query, (username, password))
#         con.commit()
#         print("Data inserted successfully")
#     except mysql.connector.Error as err:
#         print("Error:", err)
#     finally:
#         if con:
#             con.close()


# def login(username, password):
#     """Logs in a user and presents a quiz.

#     Args:
#         username: The username to login with.
#         password: The password to login with.
#     """
#     try:
#         con = c.connect(
#             host="localhost", user="root", passwd="gujjup_0003_3114", database="quizapp"
#         )
#         cursor = con.cursor()
#         sql = "SELECT * FROM st WHERE name = %s AND passs = %s AND score=%s"
#         cursor.execute(sql, (username, password))
#         result = cursor.fetchall()
#         if result:
#             print("Logged in Successfully!")
#             questions = [
#                 {
#                     "question": "QUS 1) who developed python?",
#                     "answer": "A) Guido van Rossum",
#                 },
#                 {
#                     "question": "QUS 2) who developed c programing language?",
#                     "answer": "A) Dennis Ritchie",
#                 },
#                 {
#                     "question": "QUS 3) who developed java programing language?",
#                     "answer": "A) james Gosling",
#                 },
#             ]
#             for question in questions:
#                 print(question["question"])
#                 print("A)", question["answer"])
#                 print("B) Vishal")
#                 print("C) Ansh")
#                 print("D) Gunjan")
#                 ans = input("Your ans: ").lower()
#                 if ans == question["answer"]:
#                     print("correct")
#                 else:
#                     print("wrong")
#         else:
#             print("Login failed")
#     except mysql.connector.Error as err:
#         print("Error:", err)
#     finally:
#         if con:
#             con.close()

#     score = 0
#     for question in questions:
#         # ... (existing code for question display and answer checking)
#         if ans == question["answer"].lower():
#             score += 1
#             print("correct")
#         else:
#             print("wrong")

#     # Update score in database
#     # cursor = .cursor()
#     # query = "UPDATE st SET score = %s WHERE name = %s"
#     # val = (score, username)
#     # cursor.execute(query, val)
#     # mydb.commit()

#     print("Your final score:", score)  # Display final score


# while True:
#     n = int(input("Enter your choice (1: insert, 2: login): "))
#     if n == 1:
#         username = input("Enter username: ")
#         password = input("Enter password: ")
#         insert(username, password)
#     elif n == 2:
#         username = input("Enter username: ")
#         password = input("Enter password: ")
#         login(username, password)
#     else:
#         print("Invalid choice")


# ********************************************************************* --second approch--*******************************************************
# ********************************************************************* --second approch--*******************************************************

import mysql.connector
import mysql
# Database connection details (replace with your actual credentials)
db_host = "localhost"
db_user = "root"
db_password = "gujjup_0003_3114"
db_name = "quizapp"

# Sample quiz questions (replace with your actual questions and answers)
questions = [
    {"question": "QUS 1) Who developed Python?", "answer": "A) Guido van Rossum"},
    {"question": "QUS 2) Who developed the C programming language?", "answer": "A) Dennis Ritchie"},
    {"question": "QUS 3) Who developed the Java programming language?", "answer": "A) James Gosling"},
]


def connect_to_database():
    """Connects to the MySQL database and returns the connection object"""
    try:
        mydb = mysql.connector.connect(
            host=db_host, user=db_user, password=db_password, database=db_name
        )
        return mydb
    except mysql.connector.Error as err:
        print("Error connecting to database:", err)
        return None


def insert_user(username, password):
    """Inserts a new user into the 'st' table"""
    mydb = connect_to_database()
    if mydb is None:
        return

    cursor = mydb.cursor()
    query = "INSERT INTO st (name, passs) VALUES (%s, %s)"
    val = (username, password)
    try:
        cursor.execute(query, val)
        mydb.commit()
        print("Data inserted successfully")
    except mysql.connector.Error as err:
        print("Error inserting data:", err)
    finally:
        if mydb:
            mydb.close()


def login(username, password):
    """Logs in a user and presents a quiz.

    Args:
        username: The username to login with.
        password: The password to login with.
    """
    try:
        mydb = connect_to_database()
        if mydb is None:
            return

        cursor = mydb.cursor()
        sql = "SELECT * FROM st WHERE name = %s AND passs = %s"
        cursor.execute(sql, (username, password))
        result = cursor.fetchall()

        if result:
            print("Logged in Successfully!")
            score = 0
            for question in questions:
                print(question["question"])
                print("A)", question["answer"])
                print("B) Vishal")
                print("C) Ansh")
                print("D) Gunjan")
                ans = input("Your answer (a-d): ").lower()
                if ans == question["answer"].lower():
                    score += 1
                    print("correct")
                else:
                    print("wrong")

            # Update score in database
            cursor = mydb.cursor()  # Get cursor from open connection
            query = "UPDATE st SET score = %s WHERE name = %s"
            val = (score, username)
            cursor.execute(query, val)
            mydb.commit()

            print("Your final score:", score)
        else:
            print("Login failed")
    except mysql.connector.Error as err:
        print("Error:", err)
    finally:
        if mydb:
            mydb.close()


def main():
    """Prompts user for choice (insert or login) and executes functions"""
    while True:
        choice = input("Enter your choice (1: insert, 2: login): ")
        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            insert_user(username, password)
        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            login(username, password)
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
