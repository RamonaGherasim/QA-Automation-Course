# Tema 6: OOP_Clase & Obiecte

# Imports
import math
from datetime import date

# Exercitii obligatorii

# 1.Clasa Cerc
# Atribute: raza, culoare
# Constructor pentru ambele atribute
# Metode:
# ● descrie_cerc() - va PRINTA culoarea și raza
# ● aria() - va RETURNA aria
# ● diametru()
# ● circumferinta()


class Circle:
    # constructor
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    # methods
    def circle_description(self):
        print(f'The color of the circle is {self.color} and the radius is {self.radius}')

    def area(self):
        area = math.pi * (self.radius ** 2)
        return area

    def diameter(self):
        diameter = self.radius * 2
        return diameter

    def circumference(self):
        circumference = 2 * math.pi * self.radius
        return circumference


# First object - instance of class Circle()
circle1 = Circle(3, "red")
circle1.circle_description()
print(f'The area of circle1 is {circle1.area()}')
print(f'The diameter of circle1 is {circle1.diameter()}')
print(f'The circumference of circle1 is {circle1.circumference()}')

# Second object - instance of class Circle()
circle2 = Circle(2, "green")
circle2.circle_description()
print(f'The area of circle2 is {circle2.area()}')
print(f'The diameter of circle2 is {circle2.diameter()}')
print(f'The circumference of circle2 is {circle2.circumference()}')

# 2. Clasa Dreptunghi
# Atribute: lungime, latime, culoare
# Constructor pentru toate atributele
# Metode:
# ● descrie()
# ● aria()
# ● perimetrul()
# ● schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
# Ea va lua ca și parametru o nouă culoare și va suprascrie atributul self.culoare. Puteti verifica schimbarea culorii
# prin apelarea metodei descrie().


class Rectangle:
    # constructor
    def __init__(self, length, width, color):
        self.length = length
        self.width = width
        self.color = color

    # methods
    def describe(self):
        print(f'This rectangle has a length of {self.length}, a width of {self.width} and the color {self.color}')

    def area(self):
        area = self.length * self.width
        return area

    def perimeter(self):
        perimeter = 2 * self.length + 2 * self.width
        return perimeter

    def change_color(self, new_color):
        self.color = new_color


# First object - instance of class Rectangle()
rect1 = Rectangle(5, 3, "pink")
rect1.describe()
print(f'The area of rect1 is {rect1.area()}')
print(f'The perimeter of rect1 is {rect1.perimeter()}')
rect1.describe()
rect1.change_color("purple")
rect1.describe()

# Second object - instance of class Rectangle()
rect2 = Rectangle(10, 20, "orange")
rect2.describe()
print(f'The area of rect2 is {rect2.area()}')
print(f'The perimeter of rect2 is {rect2.perimeter()}')
rect2.describe()
rect2.change_color("yellow")
rect2.describe()

# 3. Clasa Angajat
# Atribute: nume, prenume, salariu
# Constructor pt toate atributele
# Metode:
# ● descrie()
# ● nume_complet()
# ● salariu_lunar()
# ● salariu_anual()
# ● marire_salariu(procent)


class Employee:
    # constructor
    def __init__(self, surname, firstname, salary):
        self.surname = surname
        self.firstname = firstname
        self.salary = salary

    # methods
    def describe(self):
        print(f'''
My surname is {self.surname}.
My first name is {self.firstname}.
I have a salary of {self.salary}.''')

    def full_name(self):
        full_name = self.surname + ' ' + self.firstname
        return full_name

    def monthly_salary(self):
        monthly_salary = self.salary
        return monthly_salary

    def annual_salary(self):
        annual_salary = self.salary * 12
        return annual_salary

    def salary_increase(self, percentage):
        salary_increase = (percentage / 100) * self.salary
        return salary_increase


# First object - instance of class Employee()
e1 = Employee("Gherasim", "Ramona", 1000)
e1.describe()
print(f'My full name is {e1.full_name()}.')
print(f'My monthly salary is {e1.monthly_salary()}.')
print(f'My annual salary is {e1.annual_salary()}')
print(f'My salary will increase with {e1.salary_increase(3)} this month.')

# Second object - instance of class Employee()
e2 = Employee("Bob", "Ion", 4500)
e2.describe()
print(f'My full name is {e2.full_name()}.')
print(f'My monthly salary is {e2.monthly_salary()}.')
print(f'My annual salary is {e2.annual_salary()}')
print(f'My salary will increase with {e2.salary_increase(10)} this month.')


# 4.Clasa Cont
# Atribute: iban, titular_cont, sold
# Constructor pentru toate atributele
# Metode:
# ● afisare_sold() - Titularul x are în contul y suma de n lei
# ● debitare_cont(suma)
# ● creditare_cont(suma)

class Account:
    # constructor
    def __init__(self, iban, account_holder, balance):
        self.iban = iban
        self.account_holder = account_holder
        self.balance = balance

    def show_balance(self):
        print(f'Account holder {self.account_holder} has an amount of {self.balance} lei in their {self.iban} account.')

    def account_debit(self, amount):
        self.balance -= amount
        return self.balance

    def account_credit(self, amount):
        self.balance += amount
        return self.balance


# First object - instance of class Account()
account1 = Account(12345, "Ramona Gherasim", 500)
account1.show_balance()
print(f'My balance after spending 43 lei is {account1.account_debit(43)}')
print(f'My balance after receiving 90 lei is {account1.account_credit(90)}')

# Second object - instance of class Account()
account2 = Account(67890, "Ion Bob", 10000)
account2.show_balance()
print(f'My balance after spending 789 lei is {account2.account_debit(789)}')
print(f'My balance after receiving 142 lei is {account2.account_credit(142)}')


# Exercitii optionale

# 1. Clasa Factura
# Atribute: seria (va fi constantă, nu trebuie constructor, toate facturile vor
# avea aceeași serie), număr, nume_produs, cantitate, pret_buc
# Constructor: toate atributele, fara serie
# Metode:
# ● schimbă_cantitatea(cantitate)
# ● schimbă_prețul(pret)
# ● schimbă_nume_produs(nume)
# ● generează_factura() - va printa tabelar dacă reușiți
# Factura seria x numar y
# Data: generați automat data de azi
# Produs | cantitate | preț bucată | Total
# Telefon | 7 | 700 | 49000
# Indiciu pt data: https://www.geeksforgeeks.org/get-current-date-using-python/


class Factura:
    # atribute
    serie_factura = "SV-001-2022"

    # constructor
    def __init__(self, numar, nume_produs, cantitate, pret_buc):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc

    # methods
    def schimba_cantitatea(self, cantitate_noua):
        self.cantitate = cantitate_noua
        return self.cantitate

    def schimba_pretul(self, pret_nou):
        self.pret_buc = pret_nou
        return self.pret_buc

    def schimba_nume_produs(self, nume_nou):
        self.nume_produs = nume_nou
        return self.nume_produs

    def genereaza_factura(self):
        print(f'''
Factura seria {self.serie_factura} numarul {self.numar}
Data: {date.today()}
Produs    |{"Cantitate":^13}|{"pret bucata":^13}|{"Total":^13}|
Telefon   |{self.cantitate:^13}|{self.pret_buc:^13}|{self.cantitate * self.pret_buc:^13}|
''')


# First object - instance of class Factura()
f1 = Factura(1, "Zahar Margaritar", 10, 5.5)
f1.genereaza_factura()
f1.schimba_pretul(7.5)
f1.genereaza_factura()
f1.schimba_cantitatea(20)
f1.genereaza_factura()
f1.schimba_nume_produs("Zahar Coronita")
print(f1.nume_produs)


# 2.Clasa Masina
# Atribute: marca, model, viteza maxima, viteza_actuala, culoare,
# culori_disponibile (set), inmatriculata (bool)
# Culoare = gri - toate mașinile cand ies din fabrica sunt gri
# Viteza_actuală = 0 - toate mașinile stau pe loc când ies din fabrica
# Culori disponibile = alegeți voi 5-7 culori
# Marca = alegeți voi - fabrica produce o singură marca dar mai multe modele
# Inmatriculata = False
# Constructor: model, viteza_maxima
# Metode:
# ● descrie() - se vor printa toate atributele, în afară de culori_disponibile
# ● înmatriculare() - va schimba atributul înmatriculată în True
# ● vopsește(culoare) - se va vopsi mașina în noua culoare DOAR dacă noua
# culoare e în opțiunea de culori disponibile, altfel afișați o eroare
# ● accelerează(viteza) - se va accelera la o anumită viteza, dacă viteza e
# negativă-eroare, daca viteza e mai mare decat viteza_max - masina va
# accelera până la viteza maximă
# ● franeaza() - mașina se va opri și va avea viteza 0

class Masina:
    # atribute
    marca = "Nissan"
    model = None
    viteza_max = 0
    viteza_actuala = 0
    culoare = "gri"
    culori_disponibie = {"albastru", "rosu", "verde", "galben", "mov", "negru", "visiniu"}
    inmatriculata = False

    # constructor
    def __init__(self, model, viteza_max):
        self.model = model
        self.viteza_max = viteza_max

    # metode
    def descrie(self):
        print(f'''
Marca masinii este {self.marca}
Modelul masinii este {self.model}
Culoarea masinii este {self.culoare}
Viteza maxima a acestei masini este de {self.viteza_max} km/h
Viteza actuala a acestei masini este {self.viteza_actuala} km/h
Masina este inmatriculata?  {self.inmatriculata}
''')

    def inmatriculare(self):
        self.inmatriculata = True
        return self.inmatriculata

    def vopseste(self, culoare_noua):
        if culoare_noua in self.culori_disponibie:
            self.culoare = culoare_noua
        else:
            print("Aceasta culoare nu este disponibila.")
        return self.culoare

    def accelereaza(self, viteza_accelerare):
        if viteza_accelerare < 0:
            self.viteza_actuala = "Eroare, viteza nu poate fi negativa!"
        elif viteza_accelerare > self.viteza_max:
            self.viteza_actuala = self.viteza_max
            return self.viteza_actuala
        else:
            self.viteza_actuala = viteza_accelerare
            return self.viteza_actuala

    def franeaza(self):
        self.viteza_actuala = 0
        return self.viteza_actuala


m1 = Masina("X-Trail", 250)
m1.descrie()
m1.inmatriculare()
m1.descrie()
m1.vopseste("roz")
m1.descrie()
m1.vopseste("rosu")
m1.descrie()
m1.accelereaza(100)
m1.descrie()
m1.franeaza()
m1.descrie()

#
# # 3. Clasa TodoList
# # Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)
# # La început nu avem taskuri, dict e gol și nu avem nevoie de constructor
# # Metode:
# # ● adauga_task(nume, descriere) - se va adauga in dict
# # ● finalizează_task(nume) - se va sterge din dict
# # ● afișează_todo_list() - doar cheile
# # ● afișează_detalii_suplimentare(nume_task) - în funcție de numele taskului, printăm detalii suplimentare.
# # ○ Dacă taskul nu e în todo list, întrebam utilizatorul dacă vrea să-l adauge.
# # ○ Dacă acesta răspunde nu - la revedere
# # ○ Dacă răspunde da - îi cerem detalii task și salvăm nume+detalii în dict

class TodoList:
    # atribute
    todo = {}

    # metode
    def adauga_task(self, nume, descriere):
        self.todo.update({nume: descriere})

    def finalizeaza_task(self, nume):
        self.todo.pop(nume)

    def afiseaza_todo_list(self):
        print(self.todo.keys())

    def afiseaza_detalii_suplimentare(self, nume_task):
        if nume_task in self.todo.keys():
            print(self.todo[nume_task])
        else:
            adaugare_ca_task_nou = input(f"Taskul \"{nume_task}\" nu este in lista. Ati dori sa il adaugati? \n> ")\
                .lower()
            if adaugare_ca_task_nou == "nu":
                print("La revedere!")
            else:
                descriere_noua = input(f"Adaugati o descriere pentru {nume_task}: ")
                self.adauga_task(nume_task, descriere_noua)


todo1 = TodoList()
todo1.adauga_task("termina tema", "Termina tema 6 pentru cursul de testare automata")
todo1.adauga_task("dormi", "Dormi inainte de 1am")
print(TodoList.todo)
todo1.afiseaza_todo_list()
todo1.finalizeaza_task("termina tema")
print(TodoList.todo)
todo1.afiseaza_detalii_suplimentare("citeste o carte")
todo1.afiseaza_todo_list()
print(TodoList.todo)
