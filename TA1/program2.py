print("="*53)
print("|              ~ SUM OF DIGITS COUNTER ~            |")
print("|           Program by Pauline Erika Mapoy          |")
print("="*53)

def sum_of_digits(input_string):
    total = 0
    digits_found = []

    for char in input_string:
        if char.isdigit():
            digits_found.append(char)
            total += int(char)

    print("-"*53)
    
    if digits_found:
        print(f"Digits found: {', '.join(digits_found)}")
        print(f"Solution: {' + '.join(digits_found)} = {total}")
    else:
        print("No digits found.")

    print(f"Sum of digits: {total}")
    print("-"*53)

while True:
    input_string = input("Enter a String with Digits: ")
    sum_of_digits(input_string)
    
    repeat = input("Do you want to enter another String? (sige/wag): ").lower()
    if repeat != "sige":
        print("="*53)
        print("|          THANK YOU FOR USING THE PROGRAM          |")
        print("|                 Come Back Again! :)               |")
        print("="*53)
        break