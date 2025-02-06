print("="*53)
print("|               ~ CHARACTER COUNTER ~               |")
print("|           Program by Pauline Erika Mapoy          |")
print("="*53)

def count_characters(input_string):
    vowels = "AEIOUaeiou"
    vowels_count = consonants_count = spaces_count = others_count = 0

    for char in input_string:
        if char.isalpha():
            if char in vowels:
                vowels_count += 1
            else:
                consonants_count += 1
        elif char == " ":
            spaces_count += 1
        else:
            others_count += 1

    print("-"*53)
    print(f"Vowels: {vowels_count}")
    print(f"Consonants: {consonants_count}")
    print(f"Spaces: {spaces_count}")
    print(f"Other Characters: {others_count}")
    print("-"*53)

while True:
    input_string = input("Enter a String: ")
    count_characters(input_string)
    
    repeat = input("Do you want to enter another String? (sige/wag): ").lower()
    if repeat != "sige":
        print("="*53)
        print("|          THANK YOU FOR USING THE PROGRAM          |")
        print("|                 Come Back Again! :)               |")
        print("="*53)
        break