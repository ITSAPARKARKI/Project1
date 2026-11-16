
from connection import mydb
import mysql.connector


def add_std():
    mycursor = mydb.cursor()

    try:
        student_id = int(input("Enter Student ID: "))
        name = input("Enter Student Name: ")
        age = int(input("Enter Student Age: "))
        grade = float(input("Enter Student Grade: "))

        sql = "INSERT INTO STUDENT (ID, NAME, AGE, GRADE) VALUES (%s, %s, %s, %s)"
        values = (student_id, name, age, grade)

        mycursor.execute(sql, values)
        mydb.commit()

        print("Student added successfully!")

    except ValueError:
        print("Invalid input! ID and age must be integers, and grade must be a number.")

    except mysql.connector.Error as error:
        mydb.rollback()
        print("Database error:", error)

    finally:
        mycursor.close()


def display_all():
    mycursor = mydb.cursor()

    try:
        mycursor.execute("SELECT * FROM STUDENT")
        result = mycursor.fetchall()

        if not result:
            print("No students found!")
            return

        for student in result:
            print("\nID:", student[0])
            print("Name:", student[1])
            print("Age:", student[2])
            print("Grade:", student[3])
            print("-------------------")

    except mysql.connector.Error as error:
        print("Database error:", error)

    finally:
        mycursor.close()


def search_std():
    mycursor = mydb.cursor()

    try:
        student_id = int(input("Enter Student ID: "))

        sql = "SELECT * FROM STUDENT WHERE ID = %s"
        value = (student_id,)

        mycursor.execute(sql, value)
        result = mycursor.fetchone()

        if result:
            print("\nStudent Found!")
            print("ID:", result[0])
            print("Name:", result[1])
            print("Age:", result[2])
            print("Grade:", result[3])
        else:
            print("Student not found!")

    except ValueError:
        print("Please enter a valid Student ID!")

    except mysql.connector.Error as error:
        print("Database error:", error)

    finally:
        mycursor.close()


def update_std():
    mycursor = mydb.cursor()

    try:
        student_id = int(input("Enter Student ID to update: "))

        sql = "SELECT * FROM STUDENT WHERE ID = %s"
        value = (student_id,)

        mycursor.execute(sql, value)
        result = mycursor.fetchone()

        if result:
            print("\nStudent Found!")
            print("ID:", result[0])
            print("Name:", result[1])
            print("Age:", result[2])
            print("Grade:", result[3])

            print("\nWhat do you want to update?")
            print("1. Name")
            print("2. Age")
            print("3. Grade")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                new_value = input("Enter new name: ")
                sql = "UPDATE STUDENT SET NAME = %s WHERE ID = %s"

            elif choice == 2:
                new_value = int(input("Enter new age: "))
                sql = "UPDATE STUDENT SET AGE = %s WHERE ID = %s"

            elif choice == 3:
                new_value = float(input("Enter new grade: "))
                sql = "UPDATE STUDENT SET GRADE = %s WHERE ID = %s"

            else:
                print("Invalid choice!")
                return

            values = (new_value, student_id)

            mycursor.execute(sql, values)
            mydb.commit()

            print("Student updated successfully!")

        else:
            print("Student not found!")

    except ValueError:
        print("Invalid input! Please enter a valid number.")

    except mysql.connector.Error as error:
        mydb.rollback()
        print("Database error:", error)

    finally:
        mycursor.close()


def delete_std():
    mycursor = mydb.cursor()

    try:
        student_id = int(input("Enter Student ID to delete: "))

        sql = "SELECT * FROM STUDENT WHERE ID = %s"
        value = (student_id,)

        mycursor.execute(sql, value)
        result = mycursor.fetchone()

        if result:
            print("\nStudent Found!")
            print("ID:", result[0])
            print("Name:", result[1])
            print("Age:", result[2])
            print("Grade:", result[3])

            confirm = input("\nAre you sure you want to delete this student? (yes/no): ")

            if confirm.lower() == "yes":
                sql = "DELETE FROM STUDENT WHERE ID = %s"
                mycursor.execute(sql, value)
                mydb.commit()

                print("Student deleted successfully!")

            else:
                print("Deletion cancelled!")

        else:
            print("Student not found!")

    except ValueError:
        print("Please enter a valid Student ID!")

    except mysql.connector.Error as error:
        mydb.rollback()
        print("Database error:", error)

    finally:
        mycursor.close()


def std_stat():
    mycursor = mydb.cursor()

    try:
        sql = """
        SELECT
            COUNT(*),
            AVG(GRADE),
            MAX(GRADE),
            MIN(GRADE)
        FROM STUDENT
        """

        mycursor.execute(sql)
        result = mycursor.fetchone()

        print("\n----- STUDENT STATISTICS -----")
        print("Total Students:", result[0])

        if result[1] is not None:
            print("Average Grade:", round(result[1], 2))
            print("Highest Grade:", result[2])
            print("Lowest Grade:", result[3])
        else:
            print("No grades available!")

    except mysql.connector.Error as error:
        print("Database error:", error)

    finally:
        mycursor.close()
