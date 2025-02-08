print("=" * 50)
print("         UPPERCASE LOWERCASE MANIPULATION   ")
print("           ~ Created by Pauline Mapoy ~     ")
print("=" * 50)

while True:
    print(" ")
    first_name = input("Enter your First Name: ")
    last_name = input("Enter your Last Name: ")

    full_name = first_name + " " + last_name

    print("\n" + "-" * 50)
    print(f"| Full Name:                {full_name:<20} |")  
    print(f"| Full Name in Uppercase:   {full_name.upper():<20} |")
    print(f"| Full Name in Lowercase:   {full_name.lower():<20} |")
    print(f"| Length of Full Name:      {len(full_name):<20} |")
    print("-" * 50)

    repeat = input("\nDo you want to enter another name? (yes/no): ").lower()
    if repeat != "yes":
        print(" ")
        print("=" * 50)
        print("         THANK YOU FOR USING THE PROGRAM         ")
        print("               Come Back Again! :)               ")
        print("=" * 50)
        break
    