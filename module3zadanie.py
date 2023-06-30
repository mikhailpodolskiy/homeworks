class BankAccount:
    def __init__(self, account_number, name, balance):
        self.__account_number = account_number
        self.__name = name
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance > amount:
            self.__balance -= amount
        else:
            print("Недостаточно средств")

    def check_balance(self):
        return self.__balance

    def get_name(self):
        return self.__name

    def get_account_number(self):
        return self.__account_number

klient001 = BankAccount(12234344544, "Иванов Петр Иванович", 10)

print(f"Клиент {klient001.get_name()}, номер счета {klient001.get_account_number()} Ваш баланс {klient001.check_balance()} рублей")

amount = float(input("Сколько хотите положить на счет?\n>> "))
klient001.deposit(amount)

print(f"После пополнения Ваш баланс равен {klient001.check_balance()} рублей")

amount1 = float(input("Сколько хотите снять со счета?\n>> "))
klient001.withdraw(amount1)
print(f"Баланс Вашего счета равен {klient001.check_balance()} рублей")
