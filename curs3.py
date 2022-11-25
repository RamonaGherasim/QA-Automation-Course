# CURS 3 - STRUCTURI DE DATE

# Structura alternativa IF
# IF fara indentare
a = 5
b = 10
# if a>b:
# print("a este mai mare decat b")

# if else:
if a > b:
    print("a este mai mare decat b")
else:
    print("a nu este mai mare decat b")

# if else if else:
if a<b:
    print("a este mai mic decat b")
elif a == b:
    print("a egal cu b")
else:
    print("Nu este mai mare")

# if cu operatori logici
if a<b or a==b:
    print("Mesaj 1")

else:
    print("Mesaj 2")

# exercitiul 4
'''RO: Daca un client are peste 65 de ani, atunci va beneficia de o reducere de 15%.
Altfel, daca clientul nu are varsta de peste 65 de ani si calatoreste cu cel putin un copil, 
atunci acesta va beneficia de o reducere de 10%.
Pentru ambele tipuri de clienti, seniori (varsta peste 65 de ani) si non-seniori (varsta sub 65 de ani) 
se va aplica o reducere de 10% daca acestia calatoresc iarna.
De asemenea, pentru ambele tipuri de clienti, seniori (varsta peste 65 de ani) si non-seniori (varsta sub 65 
ani) vom avea o taxa de lux de 3% daca acestia calatoresc la clasa I, indiferent de anotimp sau o taxa de 
manipulare de 1% altfel
'''

# varsta = int(input("Va rugam sa introduceti varsta: "))
# anotimp = input("Va rugam sa introduceti anotimpul in care calatoriti: ")
# clasa = int(input("Introduceti clasa la care calatoriti: "))
# pretBilet = int(input("Introduceti pretul biletului: "))
#
# if varsta > 65:
#     discount = 0.15
# else:
#     nrCopii = int(input("Introduceti numarul de copii care va insotesc: "))
#     if nrCopii >= 1:
#         discount = 0.10
# if anotimp == "iarna":
#     discount += 0.1
# if clasa == 1:
#     taxa = 0.03
# else:
#     taxa = 0.01
#
# pretBilet = pretBilet - pretBilet*discount + pretBilet*taxa
# print(discount)
# print(taxa)
# print(pretBilet)

# BLACKBOX TESTING = testarea fara acces la cod (doar front-end)
# WHITEBOX TESTING = testarea cu acces la cod
# decision coverage(acopera fiecare ramura din cod) si statement coverage (acopera fiecare instructiune cel putin o data)
# decision coverage este mai acoperitor decat statement coverage

# ******************************************************
# Scenariul: Persoana peste 65 ani care calatoreste iarna la clasa 1
# Test case = cum testam?
# Test summary (test condition): Verifica faptul ca pentru un calator peste 65 ani, care calatoreste iarna,
# la clasa 1, se aplica un discount de 25% si o taxa de 3%.
# Steps to reproduce:
#   1. Intra in aplicatie
#   2. Alege destinatia dorita pentru a identifica pretul de baza a biletului
#   3. Completeaza informatiile legate de varsta, sezon si clasa
#   4. Verifica pretul calculat al biletului
# Expected result: Seniorul va primi o reducere de 25% si va plati o taxa de 3% din pretul biletului


# I. Lista
# se defineste cu paranteze patrate []
# este o colectie de date ORDONATE (sau structura de date), cu tipuri de date diferite sau de acelasi fel
# lista are proprietatea de a fi MUTABILA = isi poate schimba elementele
# Actiuni asupra unei liste:
# - putem adauga elemente
# - putem sterge elemente
# - sa modificam un element de la un anumit index
# - sa mutam un element la un anumit index

# 1. Declararea si initializarea unei liste goale
a = []

# 2. Declararea si initializzarea unei liste populate
a_prezenti = ['Raul', 'Simona', 'Alex', 'Dan', 'Ramona1']
a_absenti = ["Silviu", "Carmen", "Iulia", "Ramona"]

# 3. Accesarea elementelor dintr-o lista
print(f'Primul element din lista este: {a_prezenti[0]}')
print(f'Primul element din lista este: {a_absenti[0]}')
# accesarea ultimului element din lista:
print(f'Ultimul element: {a_prezenti[len(a_prezenti)-1]}')
print(f'Ultimul element: {a_prezenti[-1]}')

# # 4. Functia append => adauga la finalul listei
a_prezenti.append('Adela')
print(a_prezenti)

# # 5. Functia insert => adauga unde specificam indexul
a_absenti.insert(2, "Adela")
print(a_absenti)

# # 6. Functia index
print(a_absenti.index("Iulia"))

# # 7. Functia remove - returneaza None! Nu putem apela functia si printa in aceeasi linie
print(a_prezenti.remove("Dan"))

# 8. Functia pop - returneaza elementul care este scos din lista
print(a_absenti.pop(-1))
print(a_absenti)

# 9. Functia count - numara de cate ori apare un element in lista. Returneaza un int
print(a_prezenti.count("Simona"))

# 10. Fnctia extend - retuneaza None!
print(a_prezenti.extend(a_absenti))
print(a_prezenti)

# 11. Functia clear = goleste continutul listei
a_prezenti.clear()

# 12. Functia sort - sorteaza in ordine alfabetica in functie de alfabetul ASCII
# ASCII: https://infoas.ro/lectie/90/codul-ascii-tabel-complet

# liste NEOMOGENE
lista_neomogena = ['Maria', 12, True, 15.3]


# II. Seturi
# = structuri sau colectii de date, NEORDONATE si IMUTABILE (adica nu putem modifica valorile)
# se defineste cu o pereche de {}
# operatii:
# - putem accesa elementele
# - putem adauga elemente
# - putem sterge elemente

# 1. Definirea unui set gol
set_gol = set()

# 2. Definirea unui set populat
set_populat = {'caine', 'pisica', 'hamster', 'papagal'}

# 3. Accesarea unui element din set
# NU SE ACCESEAZA PRIN INDEX !!!
# prin parcurgerea setului cu for
# prin varianta cu operatorul IN
print('hamster' in set_populat) # returneaza boolean
assert'hamster' in set_populat, "Error: hamster nu este in set_populat!"
assert'gaina' in set_populat, "Error: gaina nu este in set_populat!"

# 4. Functia ADD
print(set_populat.add("gaina"))  # returneaza None!
print(set_populat)

# 5. Functia POP => sterge un element la INTAMPLARE pt ca nu avem index in seturi!
print(set_populat.pop())
print(set_populat)

# 6. Functia REMOVE => Are nevoie de un parametru care sa specifice ce anume sa stearga!
# Da eroare daca elementul nu exista!
print(set_populat.remove("broasca"))  # returneaza None!
print(set_populat)

# 7. Functia DISCARD()
# se executa fara sa returneze eroare atunci cand elementul nu este gasit
print(set_populat.discard("broasca"))

# 8. Functia UPDATE()
# face concatenare
# modifica setul de la care am plecat
set_populat.update(set_populat2)

# 9. Functia UNION()
# face concatenarea
# dar se mai creaza o a3a lista de elemente care repr concatenarea celor doua liste implicate
set_populat.union(set_populat2)

# 10. Functia CLEAR()
# sterge continutul setului
