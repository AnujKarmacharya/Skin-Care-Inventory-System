from Operations import AddProduct, RestockProduct, SellProduct
from Read import Display
from Write import Write

class Main:
    def __init__(self):
        self.add_product = AddProduct()
        self.restock_product = RestockProduct()
        self.sell_product = SellProduct()
    
    def main(self):
        while True:
            print("\n┌─────────────────────────────────────────────────────────┐")
            print("│               SKINCARE INVENTORY SYSTEM                 │")
            print("└─────────────────────────────────────────────────────────┘")
            print("  [1] Add / Restock Products")
            print("  [2] Sell Products")
            print("  [3] Log Out")
            print("───────────────────────────────────────────────────────────")
            
            try:
                choice = int(input(" Selection Index ❯ "))
            except ValueError:
                print("[!] Input Error: Please supply a valid numerical option.")
                continue
            
            if choice == 1:
                while True:
                    print("\n┌── INVENTORY CONFIGURATION MANAGEMENT ───────────────────┐")
                    print("  [1] Process Batch Restock Order")
                    print("  [2] Register Brand New Product (Product Entry)")
                    print("  [3] Return to Main Control Console")
                    print("└─────────────────────────────────────────────────────────┘")
                    try:
                        sub_choice = int(input(" Config Index ❯ "))
                    except ValueError:
                        print("[!] Input Error: Please enter a valid number.")
                        continue
                    
                    if sub_choice == 1:
                        Display.display_products()
                        product_name = input("\nEnter exact product name to update: ").strip()
                        try:
                            quantity = int(input("Enter quantity units received: "))
                            if quantity <= 0:
                                print("[!] Validation Error: Quantity value must be greater than zero.")
                                continue
                            self.restock_product.restock_product(product_name, quantity)
                        except ValueError:
                            print("[!] Input Error: Expected standard integers for stock count.")
                            
                    elif sub_choice == 2:
                        adding = True
                        while adding:
                            print("\n── New Registration Form ──")
                            name = input(" Product Descriptive Name : ").strip()
                            brand = input(" Manufacturing Brand      : ").strip()
                            
                            try:
                                price = float(input(" Retail Price ($)         : "))
                                quantity = int(input(" Initial Base Stock Count : "))
                                if price < 0 or quantity < 0:
                                    print("[!] Validation Error: Financial parameters cannot be negative values.")
                                    continue
                            except ValueError:
                                print("[!] Data Type Error: Please review standard formats for price/units.")
                                continue
                                
                            country = input(" Country of Origin        : ").strip()
                            self.add_product.add_product(name, brand, price, quantity, country)
                            
                            while True:
                                cont = input("\nRegister another product? (y/n): ").lower().strip()
                                if cont == 'n':
                                    adding = False
                                    break
                                elif cont == 'y':
                                    break
                                else:
                                    print("Please answer with 'y' or 'n'.")

                    elif sub_choice == 3:
                        break
                    else:
                        print("[!] Option out of valid range.")

            elif choice == 2:
                Display.display_products()
                products_to_sell = []

                print("\n── Active Processing Cart (Enter 'done' to calculate transaction totals) ──")
                while True:
                    name = input(" Target Product Name ❯ ").strip()
                    if name.lower() == "done":
                        break
                    if not name:
                        continue
                    try:
                        qty = int(input(f" Unit Quantity for '{name}' ❯ "))
                        if qty <= 0:
                            print("[!] Quantity cannot be zero or lower.")
                            continue
                        products_to_sell.append((name, qty))
                    except ValueError:
                        print("[!] Item rejected. Quantity must be numeric.")

                if products_to_sell:
                    total_cost, sold_items = self.sell_product.sell_product(products_to_sell)
                    if sold_items and total_cost > 0:
                        Write.sold_transcript(sold_items, total_cost)
                else:
                    print("\n[*] Processing Abandoned: Cart contains no items.")
                
            elif choice == 3:
                print("\nClosing background processes... System Session Safely Terminated.")
                break
            else:
                print("[!] System Selection Range Fault.")

if __name__ == "__main__":
    app = Main()
    app.main()