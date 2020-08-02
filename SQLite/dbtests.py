import sqlite3

from sqlite3 import Error

# Create a connection to the database
def connect():
    try:
        connection = sqlite3.connect("Documents/Projects/Python/Steve-s-Python-Practice/SQLite/database.db")
        print("Connected.")
        return connection
    except Error:
        raise(Error)

# Creates table students
def init_students():
    cursor.execute("CREATE TABLE students(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL)")
    print("Created table students.")

# Drops all data in the database
def restart():
    cursor.execute("DROP TABLE IF EXISTS students")
    print("Restarted database.")

# Inserts a student
def new_student(name):
    cursor.execute("INSERT INTO students(name) VALUES(?)", (name,))
    print("Inserted new student {}".format(name))

# Get all students
def get_all_students():
    cursor.execute("SELECT * FROM students")
    return cursor.fetchall()

connection = connect()
cursor = connection.cursor()

restart()
init_students()

new_student("Steve")
new_student("Waluigi")

print("Getting all students:")
students = get_all_students()
for student in students:
    print("\tSID: {}, NAME: {}".format(student[0], student[1]))

connection.commit()
print("Committed.")
connection.close()