def divide(a, b):
    if b == 0:
        print("\n" + "-" * 52)
        print("     !! ERROR !! Division by Zero is Not Allowed")
        print("-" * 52 + "\n")
        return None
    return a / b

def exponentiation(a, b):
    return a ** b

def remainder(a, b):
    if b == 0:
        print("\n" + "-" * 52)
        print("     !! ERROR !! Division by Zero is Not Allowed")
        print("-" * 52 + "\n")
        return None
    return a % b

def summation(a, b):
    if a > b:
        print("\n" + "-" * 52)
        print("        !! ERROR !! The second number must be")
        print("      greater than or equal to the first number")
        print("-" * 52 + "\n")
        return None
    return sum(range(a, b + 1))

def main():
    while True:
        print("=" * 52)
        print("|              Program by Pauline Mapoy            |")
        print("|         ~  MATHEMATICAL OPERATIONS MENU  ~       |")
        print("=" * 52)
        print("|               [D] - Divide                       |")
        print("|               [E] - Exponentiation               |")
        print("|               [R] - Remainder                    |")
        print("|               [F] - Summation                    |")
        print("|               [Q] - Quit                         |")
        print("=" * 52)
        
        print(" ")
        choice = input("                ENTER YOUR CHOICE: ").strip().upper()
        print(" ")
        print("=" * 52)
        
        if choice == 'Q':
            print("|          THANK YOU FOR USING THE PROGRAM         |")
            print("|                 Come Back Again! :)              |")
            print("=" * 52)
            break
        
        if choice in ['D', 'E', 'R', 'F']:
            try:
                print(" ")
                num1 = int(input("                Enter 1st Number : "))
                num2 = int(input("                Enter 2nd Number : "))
                print(" ")
                
                if choice == 'D':
                    result = divide(num1, num2)
                elif choice == 'E':
                    result = exponentiation(num1, num2)
                elif choice == 'R':
                    result = remainder(num1, num2)
                elif choice == 'F':
                    result = summation(num1, num2)
                
                if result is not None:
                    print("                RESULT:", result)
                    print(" ")
                    print("=" * 52)
                    print(" ")
                    retry = input("Do you want to Perform Another Calculation? (Y/N): ").strip().upper()
                    print(" ")
                    if retry != 'Y':
                        print("=" * 52)
                        print("|          THANK YOU FOR USING THE PROGRAM         |")
                        print("|                 Come Back Again! :)              |")
                        print("=" * 52)
                        print(" ")
                        break
            except ValueError:
                print("\n" + "-" * 52)
                print("!INVALID INPUT! Please Enter Integers Only")
                print("-" * 52 + "\n")
        else:
            print("\n" + "-" * 52)
            print("!INVALID CHOICE! Please Select a Valid Option")
            print("-" * 52 + "\n")

if __name__ == "__main__":
    main()