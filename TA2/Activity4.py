print("=" * 50)
print(" " * 12 + "VIEW ALL STUDENT INFORMATION")

try:
    with open("students.txt", "r") as file:
        contents = file.read()
        print("=" * 50)
        print(" ")
        print(contents)
        print("=" * 50)
except FileNotFoundError:
    print("=" * 50)
    print("                   !! ERROR !!")
    print("     The File 'students.txt' Does Not Exist")
    print("=" * 50)
    