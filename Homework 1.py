class Product:
    def __init__(self, name: str, price: int, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self) -> float:
        return self.price * self.quantity

    def display_info(self) -> None:
        total = self.calculate_total_price()
        print(f"Товар: {self.name}")
        print(f"Ціна за одиницю: {self.price} грн")
        print(f"Кількість: {self.quantity} шт.")
        print(f"-" * 28)
        print(f"Загальна вартість: {total} грн")

if __name__ == "__main__":
    product1 = Product(name="Телефон", price=21562, quantity=4)
    product1.display_info()
    total_cost = product1.calculate_total_price()