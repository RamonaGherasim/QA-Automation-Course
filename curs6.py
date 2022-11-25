# === Imports ====
# Importam clasele pe care le-am declarat in fisierul OOP.py
from OOP import Test_case1, Test_Case2, Test_Case3

# Se cauta dupa modulul built-in math apelandu-se functia import()
import math
# Sau se poate scrie: din modulul buil -in math, importa tot
# from math import *
# Daca vrem sa importam o functie concreta, cum ar fi pi:
# from math import pi

# Functii - CONTINUARE
# 3. Functii cu numar indefinit de parametrii
# Ne folosim de keywordul * atunci cand nu stim cati parametrii vom avea
# def calculeaza_pretul(*pret):
#     total = 0  # definim si initializam var total cu valoarea 0
#     for element in pret:
#         total += element
#     return total
#
#
# print(calculeaza_pretul(2, 6, 7))
# print(calculeaza_pretul(1, 3))
# print(calculeaza_pretul(2, 6, 7, 1, 3, 2))
#
# # 4. Functii cu keywordul "kwargs" <=> **nume_argument
# # Fac parte tot din functii cu numar indefinit de parametrii
# # Sunt folosite in special pentru a parcurge dictionare si pentru a opera cu acestea
# apa = {
#         "borsec": {"nume": "borsec", "producator": "borsec", "imbuteliere": "sticla"},
#         "dorna": {"nume": "dorna", "producator": "dorna", "imbuteliere": "peturi"}
# }
#
#
# # def accesare_element_dictioanar(**kwargs):  # Aici kwargs poate avea orice nume
# #     for key, values in kwargs.items():
# #         print(f'Detalii despre apa: {key}')
# #         for key_interior, values_interior in values.items():  # Mergem in valorile fiecarei chei, care aici sunt sub forma altor dictionare
# #             # print(f'Apa {key} are {key_interior}: {values_interior}')
# #             # SAU
# #             print(f'Apa {key} are {key_interior}: {kwargs[key][key_interior]}')
# #
# #
# # accesare_element_dictioanar(**apa)
# # accesare_element_dictioanar(apa)  # Aceasta o sa ridice o eroare deoarece nu folosim **
#
# # Accesare dictionar utilizand o functie cu keywordul **kwargs - daca dictionarul este dinamic
# def accesare_elemente_dictionar(**dictionar_dinamic):
#     for key_primar, value_primar in dictionar_dinamic.items():
#         print(f'Detalii despre apa: {key_primar}')
#         for key_secundar, value_secundar in value_primar.items():  # Mergem in valorile fiecarei chei, care aici sunt sub forma altor dictionare
#             print(f'Apa {key_primar} are {key_secundar}: {value_secundar}')
#             # SAU
#             # print(f'Apa {key_primar} are {key_secundar}: {dictionar_dinamic[key_primar][key_secundar]}')
#
#
# accesare_elemente_dictionar(**apa)
#
#
# # # Accesare dictionar utilizand o functie cu parametru - dictionar definit
# def access_dictionar(dictionar):
#     for key, values in dictionar.items():
#         print(f'{key}: ')
#         for key_interior, values_interior in values.items():
#             print(f'{key}: {key_interior} => {values_interior}')
#
#
# access_dictionar(apa)

# POO = Programare Orientata pe Obiecte (OOP in engleza)
# Cream un template pt atributele si pt comportamentul unui anumit element
# Clasa => tiparul in sine al POO
# Obiectul => Reprezentare efectiva a clasei
# Atributele => Propritatile - sunt ca niste variabile care au anumite valori
# Metodele => Functii in interiorul clasei - ce actiuni putem face

# Exemplu:
"""
Clasa masina (acesta este templatul)
Cand definim o clasa ne gandim ce atribute poate sa aiba elementul
si ce actiuni poate sa faca
A. O masina de exemplu poate sa aiba urmatoarele PROPRIETATI (<=> ATRTIBUTE):
 - culoare
 - viteza
 - an_fabricatie
 - marca
 - model
 - capacitate_rezervor
 - tip_combustibil
 - tractiune
 - serie_sasiu
 - cutie_viteze
 - numar_inmatriculare
B. O masina poate sa faca urmatoarele ACTIUNI ( <=> METODE)
 - pornire de pe loc
 - oprire
 - accelerare
 - franare
 - consum_instant 
 - re
 """

# Definirea unei clase se face cu keywordul class
# Apoi avem nevoie de un nume pentru acea clasa. acesta va incepe cu litera mare si va fi scris in format snake_case
# sau camelCase
# Dupa nume avem intotdeauna ":"
# class Masina:
    # Aici se va scrie corpul clasei

# Constructorul => este un agent responsabil cu crearea obiectului
# Vom vorbi despre 2 tipuri de constructori (cei mai uzuali): constructor implicit si constructor explicit

# 1. Constructorul explicit = cel care se defineste de catre noi in cod
# 2. Constructorul implicit = se apeleaza automat de Python atunci cand constructorul explicit lipseste / nu e definit
#                           = este o bucata de cod care se apeleaza de catre Python

# Definirea unui constructor: __init__()
# Intre paranteze se vor specifica atributele care vrem sa existe in mod obligatoriu la crearea obiectului
# Exista situatii in care putem sa nu avem nimic intre paranteze. Daca nu avem nimic scris intre paranteze, adica nici
# un parametru, atunci toate atributele vor fi optionale

# Elementul self => este un keyword care ne ajuta sa accesam elemente definite in interiorul clasei, fie ele atribute
# sau metode. Toate trebuie accesate cu elementul self.nume_atribut sau self.nume_metoda

# Exemplul 1:
class Scoala:
    # Atribute
    nume_director = None  # None este un keyword care da o valoare nula
    nr_clase = 0
    nr_elevi_clasa = 0

    # Metode
    def calc_nr_total_elevi(self, nr_clase, nr_elevi_clasa):
        nr_total_elevi = nr_clase * nr_elevi_clasa
        return nr_total_elevi

# Instantierea unui obiect al clasei Scoala, care va primi in mod implicit atributele si metodele clasei Scoala
# scoala_Bob = Scoala()
# scoala_Bob.nume_director = "Ion Bob"
# nr_clase = int(input("Introduceti numarul de clase pt scoala Bob: "))
# nr_elevi_clasa = int(input("Introduceti numarul de elevi in fiecare clasa pt scoala Bob: "))
# print(f'Nr total de elevi ai scolii Bob este {scoala_Bob.calc_nr_total_elevi(nr_clase, nr_elevi_clasa)}')
#
# # Am instantiat un nou obiect al clasei Scoala
# scoala_Popovici = Scoala()
# scoala_Popovici.nume_director = "Andrei Popovici"
# print(f'Nr total de elevi ai scolii Popovici este {scoala_Popovici.calc_nr_total_elevi(25, 15)}')  # Dam valorile parametrilor in mod explicit


continut = math.pi
print(f'Pi are valoarea {continut}')

continut2 = math.factorial(3)
print(f'Factorial de 3 este {continut2}')

my_test_case1 = Test_case1()
my_test_case2 = Test_Case2()
my_test_case3 = Test_Case3("Test_case_nr_0003", "The test case validates the design and functionality of the OK button.")

my_test_case1.printeaza_test_case()
my_test_case2.printeaza_test_case()
my_test_case3.printeaza_test_case()
print(my_test_case3.retun_name())
print(my_test_case3.return_summary())




