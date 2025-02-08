from datetime import datetime

def translate_date(date_str):
    date_obj = datetime.strptime(date_str, "%m/%d/%Y")
    return date_obj.strftime("%B %d, %Y")

def print_title():
    print("=" * 48)
    print("|             !! DATE TRANSLATOR !!            |")
    print("|        Program Created by Pauline Mapoy      |")
    print("=" * 48)
    print(" ")

def print_separator():
    print("=" * 48)

def main():
    while True:
        print_title()

        date_input = input("Enter the Date (mm/dd/yyyy): ")
        human_readable_date = translate_date(date_input)
        print(f"Date Output: {human_readable_date}")
        
        print(" ")
        print_separator()
        print(" ")
        
        again = input("Do you want to enter another date? (yes/no): ").lower()
        print(" ")
        if again != 'yes':
            print("=" * 48)
            print("|        THANK YOU FOR USING THE PROGRAM       |")
            print("|               Come Back Again! :)            |")
            print("=" * 48)
            break

if __name__ == "__main__":
    main()