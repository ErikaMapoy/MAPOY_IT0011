while True:
    print("=" * 51)
    print(" " * 12 + "INPUT NEW STUDENT INFORMATION")
    print("     ~ Program Created by Pauline Erika Mapoy ~     ")
    print("=" * 51)

    last_name = input("Enter Last Name: ")
    first_name = input("Enter First Name: ")
    age = input("Enter Age: ")
    contact_number = input("Enter Contact Number: ")
    course = input("Enter Course: ")

    student_info = f"Name: {first_name} {last_name}\nAge: {age}\nContact: {contact_number}\nCourse: {course}\n"

    with open("students.txt", "a") as file:
        file.write(student_info)

    print("=" * 51)   
    print("              !! SAVE SUCCESSFULLY !!")
    print("=" * 51)
    
    print(" ")
    again = input("Do you want to enter another student? (yes/no): ").strip().lower()
    if again != "yes":
        print(" ")
        print("=" * 51)
        print("          THANK YOU FOR USING THE PROGRAM         ")
        print("                Come Back Again! :)               ")
        print("=" * 51)
        break
