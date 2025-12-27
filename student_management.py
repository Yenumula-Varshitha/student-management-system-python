def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")

    try:
        with open("students.txt", "r") as file:
            students = file.readlines()
            for student in students:
                _, existing_roll = student.strip().split(",")
                if existing_roll == roll:
                    print("Roll number already exists!\n")
                    return
    except FileNotFoundError:
        pass

    with open("students.txt", "a") as file:
        file.write(name + "," + roll + "\n")

    print("Student added successfully!\n")
def view_students():
    try:
        with open("students.txt", "r") as file:
            students = file.readlines()

        if not students:
            print("No students found.\n")
            return

        print("Student Records:")
        for student in students:
            name, roll = student.strip().split(",")
            print("Name:", name, "| Roll:", roll)
        print()

    except FileNotFoundError:
        print("No records file found.\n")


def search_student():
    roll_to_search = input("Enter roll number to search: ")

    try:
        with open("students.txt", "r") as file:
            students = file.readlines()

        found = False
        for student in students:
            name, roll = student.strip().split(",")
            if roll == roll_to_search:
                print("\nStudent Found:")
                print("Name:", name)
                print("Roll:", roll, "\n")
                found = True
                break

        if not found:
            print("Student not found.\n")

    except FileNotFoundError:
        print("No records file found.\n")


def delete_student():
    roll_to_delete = input("Enter roll number to delete: ")

    try:
        with open("students.txt", "r") as file:
            students = file.readlines()

        with open("students.txt", "w") as file:
            found = False
            for student in students:
                name, roll = student.strip().split(",")
                if roll != roll_to_delete:
                    file.write(student)
                else:
                    found = True

        if found:
            print("Student deleted successfully!\n")
        else:
            print("Student not found.\n")

    except FileNotFoundError:
        print("No records file found.\n")


while True:
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Exiting program.")
        break
    else:
        print("Invalid choice.\n")