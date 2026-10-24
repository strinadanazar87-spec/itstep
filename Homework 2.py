def grades(score):
    if 0 <= score <= 49:
        return "незадовільно"
    elif 50 <= score <= 69:
        return "задовільно"
    elif 70 <= score <= 89:
        return "добре"
    elif 90 <= score <= 100:
        return "відмінно"
    else:
        return "Можлива оцінка від 1-100"

if __name__ == "__main__":
        user_input = input("Введіть бали студента (від 0 до 100): ")
        score = int(user_input)
        grade = grades(score)
        print(f"Кількість балів: {score}")
        print(f"Оцінка: {grade}")