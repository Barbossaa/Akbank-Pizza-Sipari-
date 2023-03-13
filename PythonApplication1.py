import csv
import datetime

# 1. Menu.txt oluþturma
with open("Menu.txt", "w") as f:
    f.write("* Lutfen Bir Pizza Tabani Seciniz:\n")
    f.write("1: Klasik\n")
    f.write("2: Margarita\n")
    f.write("3: TurkPizza\n")
    f.write("4: Sade Pizza\n")
    f.write("* ve sececeginiz sos:\n")
    f.write("11: Zeytin\n")
    f.write("12: Mantarlar\n")
    f.write("13: Keci Peyniri\n")
    f.write("14: Et\n")
    f.write("15: Sogan\n")
    f.write("16: Misir\n")
    f.write("* Tesekkur ederiz!\n")
    
    
# 2. Pizza üst sýnýfýný oluþturma

class Pizza:
    def __init__(self):
        self.description = "Bilinmeyen Pizza"
        self.cost = 0.0

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost

# 3. Pizza alt sýnýflarýný oluþturma
class Klasik(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Klasik Pizza"
        self.cost = 10.0

class Margherita(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Margherita Pizza"
        self.cost = 15.0

class TurkPizzasi(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Turk Pizza"
        self.cost = 20.0

class DominosPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Dominos Pizza"
        self.cost = 25.0

# 3. Decorator sýnýfý oluþturma
class Decorator(Pizza):
    
    
    def __init__(self, component):
        component = None
        self.component = component

    def get_cost(self):
        if self.component:
            return self.component.get_cost() + super().get_cost()
        else:
            return super().get_cost()



    def get_description(self):
        if self.component:
            return self.component.get_cost()  + super().get_description()
        else:
            return super().get_description()

class Zeytin(Decorator):
    def __init__(self):
        super().__init__(self)
        self.description = "Zeytinli"
        self.cost = 2.0

class Mantarlar(Decorator):
    def __init__(self):
        super().__init__(self)
        self.description = "Mantarlarli"
        self.cost = 2.0

class KeciPeyniri(Decorator):
    def __init__(self):
        super().__init__(self)
        self.description = "Keci Peynirli"
        self.cost = 3.0

class Et(Decorator):
    def __init__(self):
        super().__init__(self)
        self.description = "Etli"
        self.cost = 4.0

class Sogan(Decorator):
    def __init__(self):
        super().__init__(self)
        self.description = "Soganli"
        self.cost = 1.5

class Misir(Decorator):
    def __init__(self):
        super().__init__(self)
        self.description = "Misirli"
        self.cost = 1.5


# Sipariþi alma

def main():
    
    menu = open("Menu.txt", "r")
        
    for i in range(0,5):
        print(menu.readline())

    pizza_secimi = input()
    
    if pizza_secimi == "1":
        pizza = Klasik()
    elif pizza_secimi == "2":
        pizza = Margherita()
    elif pizza_secimi == "3":
        pizza = TurkPizzasi()
    elif pizza_secimi == "4":
        pizza = DominosPizza()
    else:
        print("Gecersiz bir sayi girdiniz.")
        quit()

    for y in range(0,5):
        print(menu.readline())

    sos_secimi = input()

    if sos_secimi == "11":
        sos = Zeytin()
    elif sos_secimi == "12":
        sos = Mantarlar()
    elif sos_secimi == "13":
        sos = KeciPeyniri()
    elif sos_secimi == "14":
        sos = Et()
    elif sos_secimi == "15":
        sos = Sogan()
    elif sos_secimi == "16":
        sos = Misir()
    else:
        print("Gecersiz bir sayi girdiniz.")
        quit()

    total_cost = pizza.get_cost() + sos.get_cost()
    order_time = datetime.datetime.now()
    order_description = sos.get_description() + ' ' + pizza.get_description()

    print("Total cost: {:.2f} TL --> {} ".format(total_cost, order_description))

    name = input("Ismini gir: ")
    id_number = input("TC numarani gir: ")
    cc_number = input("Kredi karti numarani gir: ")
    cc_password = input("Kredi karti sifreni gir: ")
    print("Bilgileriniz kaydedildi. Bizi tercih ettiginiz icin tesekkurler!")

    

    with open('Orders_Database.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, id_number, cc_number, cc_password, order_description, total_cost, order_time])

    
  
main()