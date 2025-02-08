def is_palindrome(num):
    return str(num) == str(num)[::-1]

def print_title():
    print("=" * 30)
    print("    PALINDROME SUM CHECKER")
    print(" ~ Program Created by Mapoy ~")
    print("=" * 30)

def print_separator():
    print("-" * 30)

file_name = 'numbers.txt'

try:
    print_title()

    with open(file_name, 'r') as file:
        line_number = 1

        for line in file:
            numbers = line.strip().split(',')
            total = sum(int(num) for num in numbers)

            print(f"Line {line_number}: {line.strip()}")
            print(f"   Sum: {total}")

            if is_palindrome(total):
                print("   - PALINDROME")
            else:
                print("   - NOT A PALINDROME")

            line_number += 1
            print_separator()

except FileNotFoundError:
    print(" ")
    print(f"  File '{file_name}' Not Found")
    print(" ")
    print("=" * 30)
except Exception as e:
    print(f"An Error Occurred: {e}")

print("            THANK YOU")
print("     FOR USING THE PROGRAM")
print("        Come Back Again!")
print("=" * 30)