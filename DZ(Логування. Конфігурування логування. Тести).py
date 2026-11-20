def check_age(age):
    assert age >= 18, "Вам має бути 18 років або більше"
    print("Ви можете використовувати цей сервіс")

user_age = int(input("Введіть ваш вік: "))
check_age(user_age)