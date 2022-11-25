# METODA SLICE()

poezie = "Ana are mere si, este vesela pentru ca este miercuri"
# Extragem toate caracterele de la inceput pana la sfarsit cu specificarea pozitiei de start si de stop
print(poezie[0:len(poezie)])

# Extragem toate caracterele de la inceput pana la sfarsit cu pozitiile de start si finish implicite
print(poezie[:])

# Extragem toate caracterele de la inceput pana la sfarsit cu pozitiile de start, finish si pasul implicite
print(poezie[::])

#Extragem toate caracterele de la inceput pana la sfarsit cu pasul 2
print(poezie[0:len(poezie):2])

#Extragem toate caracterele de la inceput pana la sfarsit cu pasul 2, cu start si finish implicite
print(poezie[::2])

# Extragem toate caracterele de la pozitia 5 pana la pozitia 13, inclusiv
print(poezie[5:14])

# Extragem ultimele 3 caractere de la final
print(poezie[len(poezie)-3:len(poezie)])
# SAU
print(poezie[-3:])

# Printam stringul in ordine inversa
print(poezie[::-1])

# METODA SPLIT()
print(poezie.split(sep=","))
print(poezie.split(sep="L"))
print(poezie.split(sep=" "))

# METODA REPLACE()
print(poezie.replace("A", "m"))
print(poezie.replace("Ana", "Maria"))

# METODA UPPER()
print(poezie.upper())
print(poezie.upper().replace("A", "m"))

# METODA INDEX() SI METODA FIND()
print(poezie.index("A"))
print(poezie.index("a"))
# Diferenta dintre find si index este faptul ca find returneaza -1 in cazul in care caracterul nu este gasit
# iar index returzeaza o eroare
# print(poezie.find("a"))
# print(poezie.find("x"))
# print(poezie.index("x"))

# METODA ISNUMERIC(), METODA COUNT() SI METODA CAPITALIZE()
numeric = "1234"
print(poezie.isnumeric())  # => False
print(numeric.isnumeric())  # => True
print(poezie.count("a"))  # => returns 4
print(poezie.count("A"))  # => returns 1
print(poezie.capitalize())


# OPERATORI = elemente prin interm carora putem face operatii
# operatori de atribuire / assignment operators: =, +=, -=, *=, /=
variabila1 = 7  # se creazza o noua adresa de memorie "variabila1"
variabila1 = 53  # se suprascrie la acceasi adrea sa memorie

# +=
variabila1 += 7 # += mult mai rapid decat +, nu se creeaza un nou obiect = ID NU SE SCHIMBA. Mai bun dpv al optimizarii
print(variabila1)
variabila1 = variabila1 + 7  # + mai slow, result assigned to a new object = ID SE SCHIMBA
list1 = [1, 2, 3]
list2 = [4, 5]
print(id(list1), id(list2))  # METODA ID() returneaza adresa/id
# list1 += list2
# print(list1)
# print(id(list1))
list1 = list1 + list2
print(list1)
print(id(list1))

# -=
var2 = 47;
var2 -= 7
print(var2)  # din valoarea anterioara (47) se scade valoarea 7, iar rezultatul final este suprascris in variabila var2
var2 = var2 - 7
print(var2)

# *=
var2 = 7
var2 *= 7
print(var2)  # valoarea anterioara (7) se va inmulti cu 7, iar rezultatul final este suprascris in variabila var2
var2 = var2 * 2
print(var2)

# /=
var2 = 7
var2 /= 7
print(type(var2))  # valoarea anterioara (7) se va imparti la 7, iar rezultatul final este suprascris in variabila var2
var2 = var2 / 2
print(var2)


# aritmetici - efectuam operatii matematice: +, -, *, /, **, %, //

nr1 = 10
nr2 = 4
print(f'Suma este {nr1 + nr2}')
print(f'Diferenta este {nr1 - nr2}')
print(f'Produsul este {nr1 * nr2}')
print(f'Impartirea este {nr1 / nr2}')
print(f'Restul impartirii este {nr1 % nr2}')
print(f'Rezultatul floor division este {nr1 // nr2}') # Floor division TAIE zecimalele
print(f'Ridicarea la puterea a2a este {nr1 ** nr2}')

# de comparare - comparam valoarea a 2 variabile
# ==(comparare), <=, >=, <, >, !=(diferit)
# Operatorii de comparare returneaza un rezultat de top boolean
nr1 = 5
nr2 = 6
print(nr1 == nr2)
print(nr1 <= nr2)
print(nr1 >= nr2)
print(nr1 < nr2)
print(nr1 > nr2)
print(nr1 != nr2)


# logici - prin interm carora putem evalua conditii compuse/mai complexe
# and, or, not
# orinea prioritatilor: not > and > or
nr1 = 5
nr2 = 6
print(nr1 > nr2 or nr1 == nr2)  # False or False => False
print(nr1 > nr2 or nr1 < nr2)  # False or True => True
print(nr1 > nr2 and nr1 < nr2)  # False and True => False
print(not nr1 > nr2 and nr1 < nr2)  # True and True => True
print(not(nr1 > nr2 and nr1 < nr2))  # not(False and True) => not(False) => True
print(not nr1 == nr2 and not nr1 >= nr2)  # not False and not False => True and True => True