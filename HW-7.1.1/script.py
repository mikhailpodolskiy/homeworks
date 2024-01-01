import random

lst = [random.randint(1, 110) for i in range(7)]
print(f"Полученный список: {lst}")
def max_index()-> tuple:
    return (max(lst), lst.index(max(lst)))

print(f"Задача № 1, решение: {max_index()}")


def inverted()-> list:
    return list(reversed(lst))

print(f"Задача № 2, решение: {inverted()}")
