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