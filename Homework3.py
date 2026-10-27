class Product:
    def __init__(self, name: str, price: float, stock: int, description: str = ""):
        self.name = name
        self.price = price
        self.stock = stock
        self.description = description
    def __str__(self):
        return f"{self.name} — {self.price} грн (На складі: {self.stock} шт.)"

class Cart:
    def __init__(self):
        self.items = {}
    def add_product(self, product: Product, quantity: int = 1):
        if quantity <= 0:
            print("Кількість не може бути 0.")
            return

        current_qty_in_cart = self.items.get(product, 0)
        total_requested = current_qty_in_cart + quantity

        if total_requested <= product.stock:
            self.items[product] = total_requested
            print(f"Додано до кошика: {product.name} ({quantity} шт.)")
        else:
            print(f"Помилка: Недостатньо товару '{product.name}' на складі. "
                  f"Доступно: {product.stock} шт. (у кошику вже є {current_qty_in_cart} шт.)")

    def remove_product(self, product: Product, quantity: int = None):
        if product not in self.items:
            print(f"Товар '{product.name}' відсутній у кошику.")
            return
        if quantity is None or quantity >= self.items[product]:
            del self.items[product]
            print(f" Товар '{product.name}' видалено з кошика.")
        else:
            self.items[product] -= quantity
            print(f"Кількість товару '{product.name}' зменшено на {quantity} шт.")

    def calculate_total(self) -> float:
        total = sum(product.price * qty for product, qty in self.items.items())
        return total
    def display_cart(self):
        if not self.items:
            print("Ваш кошик порожній.")
            return

        print("\n--- ВМІСТ КОШИКА ---")
        for product, qty in self.items.items():
            subtotal = product.price * qty
            print(f"• {product.name} | Ціна: {product.price} грн | Кількість: {qty} шт. | Сума: {subtotal} грн")
        print(f"Загальна вартість: {self.calculate_total()} грн")
        print("---------------------\n")

    def clear_cart(self):
        self.items.clear()
        print("Кошик повністю очищено.")

if __name__ == "__main__":
    laptop = Product("Ігровий ноутбук", 39805, stock=5)
    mouse = Product("Ігрова миша", 1256, stock=10)
    keyboard = Product("Ігрова клавіатура", 2153, stock=2)
    products = {"1": laptop, "2": mouse, "3": keyboard}
    my_cart = Cart()

    while True:
        print("\n--- МАГАЗИН ---")
        print("Доступні товари:")
        for key, prod in products.items():
            print(f"[{key}] {prod}")
        print("[0] Завершити покупки та показати кошик")

        choice = input("Введіть номер товару: ")

        if choice == "0":
            break
        elif choice in products:
            try:
                qty = int(input("Введіть кількість: "))
                my_cart.add_product(products[choice], qty)
            except ValueError:
                print("Будь ласка, введіть число!")
        else:
            print("Невірний вибір. Спробуйте ще раз.")
    my_cart.display_cart()