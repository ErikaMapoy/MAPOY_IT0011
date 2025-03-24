class ClothingItem:
    def __init__(self, item_id, name, description, size, price):
        self.item_id = item_id
        self.name = name
        self.description = description
        self.size = size
        self.price = price

    def __str__(self):
        return f"ID: {self.item_id} | Name: {self.name} | Size: {self.size} | Price: ₱{self.price:.2f} | Description: {self.description}"


class ClothingInventory:
    def __init__(self):
        self.inventory = {}

    def add_clothing_item(self):
        try:
            print("\n" + "=" * 50)
            print("\n" + "DETAILS OF THE CLOTHE:")
            item_id = input("      > Enter Clothing ID: ").strip()
            if item_id in self.inventory:
                raise ValueError("CLOTHING ID ALREADY EXISTS")
            
            name = input("      > Enter Clothing Name: ").strip()
            description = input("      > Enter Clothing Description: ").strip()
            size = input("      > Enter Size (S, M, L, XL): ").strip().upper()
            if size not in ["S", "M", "L", "XL"]:
                raise ValueError("ONLY CHOOSE FROM S, M, L, OR XL")

            price = float(input("      > Enter Price: "))
            if price < 0:
                raise ValueError("PRICE CANNOT BE NEGATIVE")

            self.inventory[item_id] = ClothingItem(item_id, name, description, size, price)
            
            print("\n" + "=" * 50)
            print("\n       !! CLOTHING ITEM SUCCESSFULLY ADDED !!")
        
        except ValueError as e:
            print("\n" + "=" * 50)
            print(f"      !! ERROR !! {e}")
            print("=" * 50)

    def view_clothing_items(self):
        if not self.inventory:
            print("\n" + "=" * 50)
            print("\n          NO CLOTHING ITEMS AVAILABLE :(")
        else:
            print("\n" + "=" * 50)
            print("                CLOTHING INVENTORY")
            print("=" * 50)
            for item in self.inventory.values():
                print(item)

    def update_clothing_item(self):
        try:
            print("\n" + "=" * 50)
            item_id = input("\n      > Enter Clothing ID to Update: ").strip()
            if item_id not in self.inventory:
                raise KeyError("CLOTHING ID NOT FOUND")
            
            print("\nENTER NEW CLOTHE DETAILS:")
            name = input(f"      > New Name ({self.inventory[item_id].name}): ").strip() or self.inventory[item_id].name
            description = input(f"      > New Description ({self.inventory[item_id].description}): ").strip() or self.inventory[item_id].description
            
            size_input = input(f"      > New Size (S, M, L, XL) ({self.inventory[item_id].size}): ").strip().upper()
            size = size_input if size_input in ["S", "M", "L", "XL", ""] else self.inventory[item_id].size
            
            price_input = input(f"      > New Price (₱{self.inventory[item_id].price:.2f}): ").strip()
            price = float(price_input) if price_input else self.inventory[item_id].price
            if price < 0:
                raise ValueError("PRICE CANNOT BE NEGATIVE")

            self.inventory[item_id] = ClothingItem(item_id, name, description, size, price)
            print("\n" + "=" * 50)
            print("\n     !! CLOTHING ITEM SUCCESSFULLY UPDATED !!")
        
        except KeyError as e:
            print(f"\n      !! ERROR !! {e}")
        except ValueError as e:
            print(f"\n      !! ERROR !! {e}")

    def delete_clothing_item(self):
        try:
            print("\n" + "=" * 50)
            item_id = input("\n         Enter Clothing ID to Delete: ").strip()
            if item_id not in self.inventory:
                raise KeyError("CLOTHING ID NOT FOUND")
            
            del self.inventory[item_id]
            print("\n" + "=" * 50)
            print("\n     !! CLOTHING ITEM SUCCESSFULLY DELETED !!")
        
        except KeyError as e:
            print(f"\n      !! ERROR !! {e}")

    def menu(self):
        while True:
            print("\n" + "=" * 50)
            print("|                                                |")
            print("|      ITEM (CLOTHES) MANAGEMENT APPLICATION     |")
            print("|          ~  Program By Pauline Mapoy  ~        |")
            print("|                      __   __                   |")
            print("|                    /|  \\-/  |\\                 |")
            print("|                   /_|  o.o  |_\\                |")
            print("|                     | o'o'o |                  |")
            print("|                     |  o^o  |                  |")
            print("|                     |_______|                  |")
            print("|                                                |")
            print("=" * 50)
            print("|           [1] - Add Clothing Item              |")
            print("|           [2] - View Clothing Items            |")
            print("|           [3] - Update Clothing Item           |")
            print("|           [4] - Delete Clothing Item           |")
            print("|           [5] - Exit                           |")
            print("=" * 50)

            choice = input("\n               ENTER YOUR CHOICE: ").strip()
            if choice == '1':
                self.add_clothing_item()
            elif choice == '2':
                self.view_clothing_items()
            elif choice == '3':
                self.update_clothing_item()
            elif choice == '4':
                self.delete_clothing_item()
            elif choice == '5':
                print("\n" + "=" * 50)
                print("|         THANK YOU FOR USING THE PROGRAM        |")
                print("|                Come Back Again! :)             |")
                print("=" * 50)
                break
            else:
                print("\n            !! ERROR. INVALID CHOICE !!")
                print("                  Please Try Again")


if __name__ == "__main__":
    inventory_manager = ClothingInventory()
    inventory_manager.menu()