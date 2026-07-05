import datetime

class Write:
    @staticmethod
    def restock_transcript(product_name, product_quantity):
        now = datetime.datetime.now()
        filename = now.strftime("%Y-%m-%d_%H-%M-%S") + "_restocked_product.txt"
        with open(filename, "w") as f:
            f.write("==================================================\n")
            f.write(f"INVENTORY ADJUSTMENT REPORT - {now.strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("==================================================\n")
            f.write(f"Target Item   : {product_name}\n")
            f.write(f"Inward Vol    : {product_quantity} Units\n")
            f.write("Status        : Complete / Verified\n")

    @staticmethod
    def added_transcript(product_name, product_brand, product_price, product_quantity, product_country):
        now = datetime.datetime.now()
        filename = now.strftime("%Y-%m-%d_%H-%M-%S") + "_added_product.txt"
        with open(filename, "w") as f:
            f.write("==================================================\n")
            f.write(f"NEW SKU INITIAL REGISTRY - {now.strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("==================================================\n")
            f.write(f"Item Profile  : {product_name}\n")
            f.write(f"Brand Origin  : {product_brand}\n")
            f.write(f"Market Price  : ${product_price:.2f}\n")
            f.write(f"Initial Stock : {product_quantity} Units\n")
            f.write(f"Manufacturer  : {product_country}\n")
            f.write("Status        : Active Registry Saved\n")

    @staticmethod
    def sold_transcript(products_sold, total_cost):
        now = datetime.datetime.now()
        filename = now.strftime("%Y-%m-%d_%H-%M-%S") + "_sold_product.txt"
        with open(filename, "w") as f:
            f.write("==================================================\n")
            f.write(f"POINT OF SALE SYSTEM RECEIPT - {now.strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("==================================================\n")
            f.write("Settled Ledger:\n")
            for name, qty, cost in products_sold:
                f.write(f"  - {qty}x {name:<25} Subtotal: ${cost:.2f}\n")
            f.write("--------------------------------------------------\n")
            f.write(f"TOTAL GROSS CHARGED : ${total_cost:.2f}\n")
            f.write("==================================================\n")