import os
from Write import Write

class AddProduct:
    def add_product(self, name, brand, price, quantity, country):
        if not os.path.exists("Product_File.txt"):
            with open("Product_File.txt", "w") as f:
                pass

        with open("Product_File.txt", "r") as f:
            products = f.readlines()

        for product_line in products:
            parts = product_line.strip().split(",")
            if len(parts) == 6 and parts[1].lower() == name.lower():
                print("\n[!] Error: This product already exists in the inventory system.")
                return False

        new_id = str(len(products) + 1)
        new_entry = f"{new_id},{name},{brand},{price},{quantity},{country}\n"

        with open("Product_File.txt", "a") as f:
            f.write(new_entry)

        print(f"\n[✓] Success: '{name}' added successfully!")
        Write.added_transcript(name, brand, price, quantity, country)
        return True


class RestockProduct:
    def restock_product(self, product_name, quantity):
        if not os.path.exists("Product_File.txt"):
            print("\n[!] Error: Product master file not found.")
            return

        with open("Product_File.txt", "r") as f:
            products = f.readlines()
            
        updated_products = []
        found = False

        for product in products:
            parts = product.strip().split(",")
            if len(parts) == 6:
                i_d, name, brand, price, curr_qty, country = parts
                if name.lower() == product_name.lower():
                    new_qty = int(curr_qty) + quantity
                    updated_products.append(f"{i_d},{name},{brand},{price},{new_qty},{country}\n")
                    print(f"\n[✓] Success: Restocked '{name}' by +{quantity}. New Stock Level: {new_qty}.")
                    Write.restock_transcript(name, quantity)
                    found = True
                else:
                    updated_products.append(product)

        if not found:
            print(f"\n[!] Error: Product '{product_name}' could not be located.")
            return

        with open("Product_File.txt", "w") as f:
            f.writelines(updated_products)


class SellProduct:
    def sell_product(self, products_to_sell):
        if not os.path.exists("Product_File.txt"):
            print("\n[!] Error: Product master file not found.")
            return 0, []

        with open("Product_File.txt", "r") as f:
            products = f.readlines()

        product_dict = {}
        for product in products:
            parts = product.strip().split(",")
            if len(parts) == 6:
                product_dict[parts[1].lower()] = [parts[0], parts[1], parts[2], float(parts[3]), int(parts[4]), parts[5]]

        total_cost = 0.0
        successful_sales = []

        print("\n┌────────────────── TRANSACTION RECEIPT ──────────────────┐")
        for product_name, quantity in products_to_sell:
            lookup_name = product_name.lower()
            if lookup_name in product_dict:
                data = product_dict[lookup_name]
                curr_qty = data[4]
                price = data[3]
                
                free_items = quantity // 3
                total_qty_needed = quantity + free_items

                if curr_qty < total_qty_needed:
                    print(f" │ [!] Insufficient Stock for '{data[1]}'")
                    print(f" │     Available: {curr_qty} | Required: {total_qty_needed} (inc. {free_items} free)")
                else:
                    cost = price * quantity
                    total_cost += cost
                    data[4] -= total_qty_needed
                    successful_sales.append((data[1], quantity, cost))
                    print(f" │ [✓] {quantity}x {data[1]}")
                    if free_items > 0:
                        print(f" │     + Promo Benefit: {free_items} item(s) issued at $0.00")
                    print(f" │     Subtotal: ${cost:.2f}")
            else:
                print(f" │ [!] Item Error: '{product_name}' is not in the system registry.")

        print("├─────────────────────────────────────────────────────────┤")
        print(f" │ TOTAL DUE: ${total_cost:.2f}")
        print("└─────────────────────────────────────────────────────────┘")

        with open("Product_File.txt", "w") as f:
            for data in product_dict.values():
                f.write(f"{data[0]},{data[1]},{data[2]},{data[3]},{data[4]},{data[5]}\n")

        return total_cost, successful_sales