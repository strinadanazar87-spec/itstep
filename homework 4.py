import random
class Tvaryna:
    def __init__(self, nazva: str, vik: int, vaga: float):
        self.nazva = nazva
        self.vik = vik
        self.vaga = vaga

    def zholody(self) -> str:
        return f"{self.nazva} їсть."

    def sply(self) -> str:
        return f"{self.nazva} спить с-с-с"

    def info(self) -> str:
        return f"Тварина: {self.nazva}, Вік: {self.vik} р., Вага: {self.vaga} кг."

class Sobaka(Tvaryna):
    def __init__(self, nazva: str, vik: int, vaga: float, poroda: str):
        super().__init__(nazva, vik, vaga)
        self.poroda = poroda

    def holos(self) -> str:
        return f"{self.nazva} гавкає: Гав-гав!"

    def aport(self) -> str:
        return f"{self.nazva} біжить за паличкою!"

class Kit(Tvaryna):
    def __init__(self, nazva: str, vik: int, vaga: float, kolir_shvyrky: str):
        super().__init__(nazva, vik, vaga)
        self.kolir_shvyrky = kolir_shvyrky

    def holos(self) -> str:
        return f"{self.nazva} муркоче та нявкає: Мяу-мяу~"

    def tschavyty_myshu(self) -> str:
        return f"{self.nazva} полює на мишу!"

imena_sobak = ["Бобік", "Рекс", "Шарик", "Джек", "Барон"]
porody_sobak = ["Німецька вівчарка", "Лабрадор", "Хаскі", "Пудель", "Доберман"]
imena_kotiv = ["Мурчик", "Барсик", "Рижиk", "Кузя", "Тихон"]
kolory_shvyrky = ["Рудий", "Чорний", "Білий", "Сірий", "Смугастий"]


rand_nazva_pes = random.choice(imena_sobak)
rand_vik_pes = random.randint(1, 12)
rand_vaga_pes = round(random.uniform(5.0, 35.0), 1)
rand_poroda = random.choice(porody_sobak)
pes = Sobaka(nazva=rand_nazva_pes, vik=rand_vik_pes, vaga=rand_vaga_pes, poroda=rand_poroda)
print(pes.info())
print(pes.zholody())
print(pes.holos())
print(pes.aport())
print(f"Порода: {pes.poroda}\n")

rand_nazva_kot = random.choice(imena_kotiv)
rand_vik_kot = random.randint(1, 15)
rand_vaga_kot = round(random.uniform(2.0, 7.0), 1)
rand_kolir = random.choice(kolory_shvyrky)
kotyk = Kit(nazva=rand_nazva_kot, vik=rand_vik_kot, vaga=rand_vaga_kot, kolir_shvyrky=rand_kolir)
print(kotyk.info())
print(kotyk.sply())
print(kotyk.holos())
print(kotyk.tschavyty_myshu())
print(f"Колір шерсті: {kotyk.kolir_shvyrky}")