# # III. TUPLURI
# # - se declara cu paranteze ()
# # - sunt IMUTABILE
# # - sunt ORDONATE
# # - accepta duplicate
# # - se acceseaza pe baza de index
# # - elementele nu pot fi mmodificate => nu putem schimba, sterge, clear, etc elementele
#
#
# # 1. Definirea unui tuplu gol:
# t = ()
# print(type(t))
#
# # 2. Definirea unui tuplu populat:
# t = ('mere', 'pere', 'nectarine', 'gutui', 'pere')
# print(t)
#
# # 3. Functii care se pot folosi cu un tuple
# # 3.1 Functia .index() => returneaza indexul elemntului caruia dam indexul ca parametru
# print(t.index('nectarine'))
# # 3.2 Functia .count() => returneaza de cate ori apare un element dat ca si parametru in tuplul nostru
# print(t.count('pere'))
#
#
# # IV. DICTIONARE
# # Elementele sunt de tip cheie-valoare
# # Cheile trebuie sa fie UNICE
# # Cheile servesc drept inlocuitori pt index
# # sunt ORDONATE
# # Cheia e in partea stanga, valoarea in partea dreapta. Se folosesc : intre ele. Toate elementele se despart prin virgula
#
# # 1. Definirea unui dictionar gol
# d = {}
# print(type(d))
#
# # 2. Definirea unui dictionar populat
# d = {
#     "Marca": "Audi",
#     "Model": "TT",
#     "An_fabricatie": 2010,
#     "Norma_euro": "Euro 4",
#     "Combustibil": "Benzina",
#     "Model": "TT"
# }
# print(d)

# # 3. Functii
# # Accesarea elementelor dintr-un dict (cu cheie sau cu .get())
# print(f'Numele masinii este {d["Marca"]}')
# print(f'Modelul masinii este {d.get("Model")}')

# Adaugarea de elemente intr-un dict
# d["Numar_de_locuri"] = 5

# Actualizarea elementelor intr-un dictionar cu update
# d.update({"Numar_de_locuri": 5})
# print(d)
# numar_locuri = {"Numar_de_locuri": 5}
# d.update(numar_locuri)
# print(d)
# centuri = {"Centuri": True}
# d.update(centuri)
# print(d)

# Stergerea unui element cu functia .pop()
# d.pop("Norma_euro")
# print(d)

# Accesarea valorilor dintr-un dictionar folosind .values()
# print(f'Valorile proprietatilor masinii mele sunt: {d.values()}')

# Accesarea cheilor dintr-un dictionar folosind .keys()
# print(f'Proprietatile masinii mele sunt: {d.keys()}')

# Accesarea perechilor cheie valoare
# print(f'Dictionarul este format din urmatoarele elemente: {d.items()}')

# Dictionar imbricat
apa_plata = {
    "borsec": {
        "nume": "borsec",
        "producator": "borsec",
        "cantitate_vanzare": "500ml",
        "impachetare": "baxuri"
    },
    "aqua carpatica": {
        "nume": "aqua carpatica",
        "cantitate_vanzare": "2l",
        "impachetare": "sticla"
    },
    "dorna":
        {
            "nume": "dorna",
            "producator": "dorna",
            "impachetare": "bax",
            "promovare": {"reclama": "Hai gata cu fotosinteza, la culcare toata lumea"},
            "televiziune promovare": ["tvr1", "tvr2", "acasa tv", "antena1"]
        }
}
print(apa_plata["aqua carpatica"]["impachetare"])
print(apa_plata["dorna"]["promovare"]["reclama"])
print(apa_plata["dorna"]["televiziune promovare"][1])


# *********************************************************************************************************************
# STRUCTURI REPETITIVE: While, For, For Each, Do while => (nu este inclusa in curs)

# I. Structure repetitiva WHILE => executam o serie de instructiuni atata timp cat o conditie este adevarata
# Elementul sau variabila de control se declara de regula in afara While-ului

# Exericiu 1: Printati toate num de la 1 la 10 folosind while
# i = 1
# while i <= 10:
#     print(f'Numarul current este {i}')
#     i += 1

# Exercitiu 2: Printati 101 dalmatieni
# i = 1
# while i <= 101:
#     print(f'Dalmatianul numarul {i}')
#     i += 1

# Exercitiul 3: Printati suma numerelor de la 1 la 10
# i = 1
# suma = 0
# while i <= 10:
#     suma += i
#     i += 1
# print(f'Suma numerelor este {suma}')

# Exercitiul 4: Parcurgeti o lista si printati fiecare element
l1 = ["Ramona", "Dan", "Alex", "Iulia", "Carmen", "Raul", "Ramona2", "Simona", "Silviu"]
i = 0
while i < len(l1):
    print(f'Numele este {l1[i]}')
    i += 1

print(len(l1))
# Se foloseste i < len(l1) sau i <= len(l1-1)

# Exercitiul 5: Inlocuiti-l pe Silviu cu Andreea
i = 0
while i < len(l1):
    if l1[i] == "Silviu":
        l1[i] = "Andreea"
    i += 1
print(l1)

# Exercitiul 6: Inlocuiti-l pe Alex cu Adela
i = 0
while i < len(l1):
    if l1[i] == "Alex":
        l1[i] = "Adela"
        break
    i += 1
print(l1)

# II Structura repetitiva FOR
# - este utilizata atunci cand vrem sa parcurgem o lista cu scopul de a printa sau modifica elementele
# - o mai utilizam atunci cand vrem sa executam un set de instructiuni de un numar specific de ori

# Structura unui FOR LOOP
# Parcurgeti numerele de la 0 la 10 si printati-le pe cele pare

# for i in range(0, 11):  # => capatul superior la range nu este luat in considerare
#                         # => start range are valoarea default 0 si poate fi omisa
#     if i % 2 == 0:
#         print(i)
#     else:
#         print("Nu este par.")
#
# for i in range(11):
#     if i % 2 != 0:
#         print(i)
#     else:
#         print("Nu este impar.")

for i in range(11):
    print(i)
    if i == 5:
        break
        
for i in range(999):
    if i == 3:
        break
    print(i)