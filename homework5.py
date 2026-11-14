try:
    Vedenechislo = input("Введіть число: ")
    chislo = int(float(Vedenechislo))
    print(f"Ціле число: {chislo}")

except ValueError:
    print("Можна писати лише числа")