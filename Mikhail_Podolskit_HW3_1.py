print("Задача №1")

class Auto:
    def __init__(self, year, model):
        self.year = year
        self.model = model

    def get_year(self):
        return self.year

    def get_model(self):
        return self.model

    def tech_info(self):
        print(f"\nГод выпуска: {self.year}; Модель: {self.model}")

    def move(self):
        print("Помчался....")

a1 = Auto(1978, "Ваз 2109")

a1.tech_info()
a1.move()
print(a1.get_model())
print(a1.get_year())


class Train:
    def __init__(self, year, model):
        self.year = year
        self.model = model

    def get_year(self):
        return self.year

    def get_model(self):
        return self.model

    def tech_info(self):
        print(f"\nГод выпуска: {self.year}; Модель: {self.model}")

    def hard_stop(self):
        print("Жесткая остановка....")

t1 = Train(1999, "Ласточка")

t1.tech_info()
t1.hard_stop()
print(t1.get_model())
print(t1.get_year())

class Transport_sredstvo:
    def __init__(self, year, model):
        self.year = year
        self.model = model

    def get_year(self):
        return self.year

    def get_model(self):
        return self.model

    def tech_info(self):
        print(f"\nГод выпуска: {self.year}; Модель: {self.model}")

    def yamzhik(self):
        print("Ямщик не гони лошадей....")

ts1 = Transport_sredstvo(1978, "Тройка лошадей")

ts1.tech_info()
ts1.yamzhik()
print(ts1.get_model())
print(ts1.get_year())

class Express:
    def __init__(self, year, model):
        self.year = year
        self.model = model

    def get_year(self):
        return self.year

    def get_model(self):
        return self.model

    def tech_info(self):
        print(f"\nГод выпуска: {self.year}; Модель: {self.model}")

    def moving(self):
        print("Помчали с ветерком....")

ex1 = Express(2015, "Сапсан")

ex1.tech_info()
ex1.moving()
print(ex1.get_model())
print(ex1.get_year())



print(f"\n Задача №2")
class Rectangle:
    def __init__(self, dlina, shirina):
        self.dlina = dlina
        self.shirina = shirina

    def get_dlina(self):
        return self.dlina

    def get_shirina(self):
        return self.shirina

    def set_dlina(self, value):
        self.dlina = value

    def set_shirina(self, value):
        self.shirina = value

    def perimetr(self):
        return (self.dlina + self.shirina) * 2

    def plozhad(self):
        return self.dlina * self.shirina

    def __str__(self):
        return f"Длина = {self.dlina}; Ширина = {self.shirina}"

r1 = Rectangle(7, 1)
r2 = Rectangle(13, 8)

print(r1)
print(r1.get_dlina())
print(r1.get_shirina())
print(r1.perimetr())
print(r1.plozhad())