import csv

def load_exchange_rates(filename):
    exchange_rates = {}
    valid_currency_codes = set()  
    
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  
        for row in reader:
            code, name, rate = row
            exchange_rates[code] = {'name': name, 'rate': float(rate)}
            valid_currency_codes.add(code) 
            
    return exchange_rates, valid_currency_codes  

def convert_currency(amount, currency_code, exchange_rates, valid_currency_codes):
    if currency_code in valid_currency_codes:  
        currency = exchange_rates[currency_code]
        converted_amount = amount * currency['rate']
        return currency['name'], converted_amount
    return None, None

def print_title():
    print("")
    print("=" * 45)
    print("|           $ CURRENCY CONVERTER $          |")
    print("|              By Pauline Mapoy             |")
    print("=" * 45)

def print_conversion(usd_amount, currency_name, converted_amount, currency_code):
    print("\n" + "=" * 45)
    print(f"|  {'!! RESULT !!':^40} |")
    print("=" * 45)
    print(f"     USD:          {usd_amount:>14,.2f} USD         ")
    print(f"     {currency_name:<15} {converted_amount:>14,.2f} {currency_code}       ")
    print("=" * 45 + "\n")

def main():
    exchange_rates, valid_currency_codes = load_exchange_rates('currency.csv')

    print_title()

    while True:
        try:
            usd_amount = float(input("\nEnter the amount in USD: "))
            currency_code = input("Enter the currency code to convert to: ").upper()

            currency_name, converted_amount = convert_currency(usd_amount, currency_code, exchange_rates, valid_currency_codes)

            if currency_name:
                print_conversion(usd_amount, currency_name, converted_amount, currency_code)
            else:
                print("Invalid currency code. Please try again.")

        except ValueError:
            print("Invalid input. Please enter a numeric value.")

        another = input("Do you want to convert another currency? (yes/no): ").strip().lower()
        if another not in ['yes', 'y']:
            print("")
            print("=" * 45)
            print("|      THANK YOU FOR USING THE PROGRAM      |")
            print("|             Come Back Again! :)           |")
            print("=" * 45)
            print("")
            break

if __name__ == "__main__":
    main()