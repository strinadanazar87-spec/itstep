from colorama import Fore, Back, Style, init

# автоматично скидає колір після кожного рядка
init(autoreset=True)

# Fore — зміна кольору тексту
print(Fore.YELLOW + "Жовтий текст")
print(Fore.CYAN + "голубий колір")
print(Fore.GREEN + "Зелений текст")

# Back — зміна кольору фону (background)
print(Back.YELLOW + Fore.LIGHTCYAN_EX + "Текст із жовтим фоном та ось таким кольором")

# Style — зміна стилю тексту (наприклад яксравий)
print(Style.BRIGHT + "Яскравий текст")