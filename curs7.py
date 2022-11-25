# OOP Recapitulare

from curs7_Import import TestCase1, TestCase2, TestCase3
import math  # se cauta dupa modelul built-in (built-in => in interiorul Python) math apelandu-se functia import()
# <=> __import__()
# modul python = un fisier care contine definitii si statements python, adica functii, clase, variabile

# from math import *
# print(pi)
# print (factorial(6))

# from math import pi
# print(pi)

pie = math.pi
print("The value of pi is: ", pie)

child1 = TestCase1()
child2 = TestCase2()
child3 = TestCase3('test_case_nr_0003', 'the test case validate the design and functionality of [OK] button')
child1.test_exe()
child2.test_exe()
print(child3.get_name())
print(child3.get_summary())
child3.test_exe()
child3.runTwice()

# Se printeazza si rezutatul pe care noi l-am implementat in fisierul din care importam (print name de 2 ori)
# Daca nu dorim sa se intample asta (nu vrema sa stim nimic despre obiectele instantiate in fiesierul de unde importam)
# folosim if __name__ == "__main__": => vezi exemplul in fisierul curs7_Import


# Exercitiu
class Masina:
    # definirea atributelor
    model = None
    culoare = "orange"
    marca = None
    viteza_max = 0
    viteza_curenta = 0
    an_fabricatie = 0
    capacitate_motor = 0
    serie_sasiu = None
    tip_combustibil = "motorina"
    cutie_viteze = "automat"

    # constructor
    def __init__(self, marca1, model1, culoare1):
        self.marca = marca1
        self.model = model1
        if culoare1 == "orange":
            self.culoare = "portocaliu"
        # self.culoare = culoare

    # definirea metodelor
    def paint(self, colour):
        self.culoare = colour

    def start_masina(self):
        self.viteza_curenta += 5
        print("Masina s-a pus in miscare!")
        return self.viteza_curenta


bmw = Masina("bmw", "120D", "rosu")
bmw.culoare = "galben"
print(bmw.culoare)
bmw.paint("verde")
print(bmw.culoare)
print(bmw.start_masina())


# Pilonii OOP = 4 concepte/notiuni de baza
# Sunt 4 piloni care ne ajuta la o mai buna gestionare a codului si economisirea de cod
# 1. Mostenirea
# 2. Polimorfismul
# 3. Encapsularea
# 4. Abstractizarea
# In munca de QA automation cel mai de baza este mostenirea si poate polimorfismul

# I. MOSTENIREA
# => Da posibilitatea unei clase de a mosteni atribute si metode definite intr-o alta clasa parinte
# Dupa numele clasei (clasa copil) se pun paranteze atunci cand mosteneste o clasa parinte.
# Intre paranteze se da ca si parametr numele clasei de baza (clasei parinte)
# Aceasta mostenire se foloseste tot in ideea de a crea un template si de a folosi template-ul in mai multe situatii
# E.g Avem clasa parinte Animale si vream sa cream o clasa copil AnimaleDomestiice si o clasa copil AnimaleSalbatice
# Creand o clasa copil extindem clasa parinte si adaugam metodde si atribute care sunt specifice clasei copil

# II. POLIMORFISMUL
# => Ne ofera posibilitatea de a crea functii cu nume identic dar cu comportament diferit
# Spunem ca avem polimorfism atunci cand implementam aceeasi metoda in doua clase diferite
# Exista polimorfism prin re-implementarea metodei din clasa parinte
# Mai putem avea polimorfism prin definirea de functii sau metode cu parametrii impliciti
# Tot polimorfism mai avvem atunci prin definirea unei functii sau metode cu nr indefinit de parametrii (*args, **kwargs)

