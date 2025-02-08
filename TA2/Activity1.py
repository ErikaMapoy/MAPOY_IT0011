while True:
    print(" ")
    print("=" * 41)
    print("    ~ STRING MANIPULATION PROGRAM ~   ")
    print("        Created by Pauline Mapoy      ")
    print("=" * 41)
    
    print(" ")
    first_name = input("Enter your First Name: ")
    last_name = input("Enter your Last Name: ")
    age = input("Enter your Age: ")

    full_name = first_name + " " + last_name
    sliced_name = first_name[:3]

    greeting = f"Hello, {sliced_name}! You are {age} years old."
    welcome_msg = "WELCOME TO THE PROGRAM :)"

    print("\n" + "-" * 41)
    print(f"| Full Name:        {full_name:<19} |")
    print(f"| Sliced Name:      {sliced_name:<19} |")
    print(f"|                                       |")
    print(f"| Greeting Message:                     |")
    print(f"| {greeting:<37} |")
    print(f"| {welcome_msg:<37} |")
    print("-" * 41)

    retry = input("\nDo you want to enter again? (yes/no): ").strip().lower()
    if retry != "yes":
        print(" ")
        print("=" * 41)
        print("     THANK YOU FOR USING THE PROGRAM         ")
        print("           Come Back Again! :)               ")
        print("=" * 41)
        break
    
    