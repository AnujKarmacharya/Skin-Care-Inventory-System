import os

class Display:
    @staticmethod
    def safe_pad(text, width):
        """Truncates text with '...' if it exceeds width, otherwise pads it perfectly."""
        text = str(text)
        if len(text) > width:
            return text[:width - 3] + "..."
        return f"{text:<{width}}"

    @staticmethod
    def display_products():
        if not os.path.exists("Product_File.txt"):
            with open("Product_File.txt", "w") as f:
                pass
            print("\n┌──────────────────────────────────────────────────┐")
            print("│ Warning: Product inventory is currently empty.   │")
            print("└──────────────────────────────────────────────────┘")
            return

        with open("Product_File.txt", "r") as f:
            lines = [line.strip() for line in f if line.strip()]

        if not lines:
            print("\n┌──────────────────────────────────────────────────┐")
            print("│ Warning: Product inventory is currently empty.   │")
            print("└──────────────────────────────────────────────────┘")
            return

        # Explicitly defined safe structural column widths
        w_id, w_name, w_brand, w_price, w_qty, w_country = 5, 30, 18, 12, 9, 14

        # Table Header UI
        print("\n┌" + "─"*w_id + "┬" + "─"*w_name + "┬" + "─"*w_brand + "┬" + "─"*w_price + "┬" + "─"*w_qty + "┬" + "─"*w_country + "┐")
        print(f"│{Display.safe_pad('ID', w_id)}│"
              f"{Display.safe_pad('PRODUCT NAME', w_name)}│"
              f"{Display.safe_pad('BRAND', w_brand)}│"
              f"{Display.safe_pad('PRICE', w_price)}│"
              f"{Display.safe_pad('STOCK', w_qty)}│"
              f"{Display.safe_pad('COUNTRY', w_country)}│")
        print("├" + "─"*w_id + "┼" + "─"*w_name + "┼" + "─"*w_brand + "┼" + "─"*w_price + "┼" + "─"*w_qty + "┼" + "─"*w_country + "┤")

        # Table Rows
        for line in lines:
            parts = line.split(",")
            if len(parts) == 6:
                i_d, name, brand, price, quantity, country = parts
                try:
                    formatted_price = f"${float(price):.2f}"
                except ValueError:
                    formatted_price = f"${price}"

                print(f"│{Display.safe_pad(i_d, w_id)}│"
                      f"{Display.safe_pad(name, w_name)}│"
                      f"{Display.safe_pad(brand, w_brand)}│"
                      f"{Display.safe_pad(formatted_price, w_price)}│"
                      f"{Display.safe_pad(quantity, w_qty)}│"
                      f"{Display.safe_pad(country, w_country)}│")

        # Table Footer UI
        print("└" + "─"*w_id + "┴" + "─"*w_name + "┴" + "─"*w_brand + "┴" + "─"*w_price + "┴" + "─"*w_qty + "┴" + "─"*w_country + "┘")