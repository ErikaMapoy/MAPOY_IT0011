import csv

students = []

def compute_grade(class_standing, major_exam):
    return (class_standing * 0.6) + (major_exam * 0.4)

def print_table(student_list):
    if not student_list:
        print("No Student Records Found :(")
        return

    print("\n{:<10} {:<20} {:<15} {:<15} {:<10}".format("ID", "Name", "Class Standing", "Major Exam", "Final Grade"))
    print("=" * 75)

    for student in student_list:
        student_id, name, class_standing, major_exam = student
        final_grade = compute_grade(class_standing, major_exam)
        print("{:<10} {:<20} {:<15.2f} {:<15.2f} {:<10.2f}".format(student_id, f"{name[0]} {name[1]}", class_standing, major_exam, final_grade))
        print("")

def save_file(filename="StudentRecords1.csv"):
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Student ID", "First Name", "Last Name", "Class Standing", "Major Exam"])
        for student in students:
            writer.writerow([student[0], student[1][0], student[1][1], student[2], student[3]])
    print(f"Records saved to {filename} successfully!")

def save_as_file():
    filename = input("Enter filename to save as: ")
    save_file(filename)

def open_file():
    global students
    filename = input("Enter filename to open: ")
    try:
        with open(filename, mode="r") as file:
            reader = csv.reader(file)
            next(reader)  
            students = [(row[0], (row[1], row[2]), float(row[3]), float(row[4])) for row in reader]
        print(f"Records loaded from {filename} successfully!")
    except FileNotFoundError:
        print("File not found. Please enter a valid filename.")

def show_all_students():
    print("\nALL STUDENT RECORDS:")
    print_table(students)

def order_by_last_name():
    sorted_students = sorted(students, key=lambda x: x[1][1])
    print("\nSTUDENTS ORDERED BY LAST NAME:")
    print_table(sorted_students)

def order_by_grade():
    sorted_students = sorted(students, key=lambda x: compute_grade(x[2], x[3]), reverse=True)
    print("\nSTUDENTS ORDERED BY FINAL GRADE:")
    print_table(sorted_students)

def show_student_record(student_id):
    student_list = [student for student in students if student[0] == student_id]
    if student_list:
        print("\nSTUDENT RECORD")
        print_table(student_list)
    else:
        print("Student not found! :(")

def add_record():
    student_id = input("Enter Student ID (6-digit number): ")
    if not student_id.isdigit() or len(student_id) != 6:
        print("Invalid Student ID :(")
        return

    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    class_standing = float(input("Enter Class Standing Grade: "))
    major_exam = float(input("Enter Major Exam Grade: "))

    students.append((student_id, (first_name, last_name), class_standing, major_exam))
    print("")
    print("STUDENT RECORD ADDED :)")

def edit_record(student_id):
    for i, student in enumerate(students):
        if student[0] == student_id:
            first_name = input("Enter New First Name: ")
            last_name = input("Enter New Last Name: ")
            class_standing = float(input("Enter New Class Standing Grade: "))
            major_exam = float(input("Enter New Major Exam Grade: "))

            students[i] = (student_id, (first_name, last_name), class_standing, major_exam)
            print("")
            print("STUDENT RECORD UPDATED :)")
            return
    print("Student not found! :()")

def delete_record(student_id):
    global students
    students = [student for student in students if student[0] != student_id]
    print("")
    print("STUDENT RECORD DELETED (if it existed)")

def display_menu():
    print("\n" + "=" * 40)
    print("  ~ STUDENT RECORD MANAGEMENT SYSTEM ~   ")
    print("             By Pauline Mapoy  ")
    print("=" * 40)
    print("|    [1] - Open File                   |")
    print("|    [2] - Save File                   |")
    print("|    [3] - Save As File                |")
    print("|    [4] - Show All Students Record    |")
    print("|    [5] - Order by Last Name          |")
    print("|    [6] - Order by Grade              |")
    print("|    [7] - Show a Student Record       |")
    print("|    [8] - Add Record                  |")
    print("|    [9] - Edit Record                 |")
    print("|   [10] - Delete Record               |")
    print("|   [11] - Exit                        |")
    print("=" * 40)
    print("")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        print("")

        if choice == "1":
            open_file()
        elif choice == "2":
            save_file()
        elif choice == "3":
            save_as_file()
        elif choice == "4":
            show_all_students()
        elif choice == "5":
            order_by_last_name()
        elif choice == "6":
            order_by_grade()
        elif choice == "7":
            student_id = input("Enter Student ID: ")
            show_student_record(student_id)
        elif choice == "8":
            add_record()
        elif choice == "9":
            student_id = input("Enter Student ID to Edit: ")
            edit_record(student_id)
        elif choice == "10":
            student_id = input("Enter Student ID to Delete: ")
            delete_record(student_id)
        elif choice == "11":
            print("     THANK YOU FOR USING THE PROGRAM         ")
            print("           Come Back Again! :)               ")
            print("")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()