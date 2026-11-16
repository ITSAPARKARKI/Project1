from connection import mydb
from student import add_std, display_all, search_std, update_std, delete_std, std_stat





print("----- STUDENT MANAGEMENT SYSTEM -----")

try:
    while True:
        print("\n1. Add Student")
        print("2. Display All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Student Statistics")
        print("7. Exit")

        try:
            user_input = int(input("Enter your option: "))

            if user_input == 1:
                add_std()

            elif user_input == 2:
                display_all()

            elif user_input == 3:
                search_std()

            elif user_input == 4:
                update_std()

            elif user_input == 5:
                delete_std()

            elif user_input == 6:
                std_stat()

            elif user_input == 7:
                print("Exit Successfully!")
                break

            else:
                print("Invalid option! Please try again.")

        except ValueError:
            print("Please enter a number from 1 to 7!")

finally:
    mydb.close()
