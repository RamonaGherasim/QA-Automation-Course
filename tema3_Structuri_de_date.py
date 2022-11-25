# Tema 3: Structuri de date

# Exercitii obligatorii
'''
1. Declară o listă note_muzicale în care să pui do re mi etc până la do
● Afișeaz-o
● Inversează ordinea folosind slicing și suprascrie această listă.
● Printează varianta actuală (inversată).
● Pe această listă aplică o metodă care bănuiești că face același lucru,
adică să îi inverseze ordinea. Nu trebuie să o suprascrii în acest caz,
deoarece metoda face asta automat.
● Printează varianta actuală a listei. Practic ai ajuns înapoi la varianta
inițială.
Concluzii: slicing e temporar, dacă vrei să păstrezi noua variantă va trebui să
suprascrii lista sau să o salvezi într-o listă nouă. Metoda găsită de tine face
suprascrierea automat și permanentizează aceste modificări. Ambele variante
își găsesc utilitatea în funcție de ce ne dorim în acel moment.
'''
# Declararea listei
note_muzicale = ["do", "re", "mi", "fa", "sol", "la", "si", "do"]
# Afisarea listei
print(note_muzicale)
# Inversarea listei folosind slicing si suprascrierea acesteia
note_muzicale = note_muzicale[::-1]
# Printarea variantei actuale (inversate)
print(note_muzicale)
# Aplicarea metodei reverse (care suprascrie variabila automat)
note_muzicale.reverse()
# Printarea variantei actuale a listei
print(note_muzicale)

# 2. De cate ori apare 'do'?
print(note_muzicale.count('do'))  # => 'do' apare de 2 ori

# 3. Avand 2 liste, [3, 1, 0, 2] si [6, 5, 4]
# Gaseste 2 variante sa le unesti intr-o singura lista.
list_a = [3, 1, 0, 2]
list_b = [6, 5, 4]
# Prima varianta: folosirea metodei extend()
# list_a.extend(list_b)
# print(list_a)
# Varianta a 2a, folosirea operatorului aritmetic +
# list_c = list_a + list_b
# print(list_c)
# Varianta 3: folosirea operatorului unpacking *
list_c = [*list_a, *list_b]
print(list_c)

# 4.● Sortează și afișază lista generată la exercițiul anterior.
# ● Sortează numărul 0 folosind o funcție.
# ● Afișaza iar lista.
list_c.sort()
print(list_c)
print(sorted(list_c))
list_c.remove(0)
print(list_c)

# 5. Folosind un if verifică lista generată la exercițiul 3 și afișază:
# ● Lista este goală.
# ● Lista nu este goală.
# Se paote verifica cu urmatoarele variante:
if list_c:
    print("Lista nu este goala")
else:
    print("Lista este goala")

if not list_c:
    print("Lista este goala")
else:
    print("Lista nu este goala")

if bool(list_c):
    print("Lista nu este goala")
else:
    print("Lista este goala")

if len(list_c) == 0:
    print("Lista este goala")
else:
    print("Lista nu este goala")

if len(list_c):
    print("Lista nu este goala")
else:
    print("Lista este goala")

# 6. Folosește o funcție care să șteargă lista de la exercițiul 3.
# Functia clear() sterge elementele din lista
list_c.clear()
# Pentru a sterge lista se poate folosi del???
# del list_c

# 7. Copy paste la exercițiul 5. Verifică încă o dată.
# Acum ar trebui să se afișeze că lista e goală.
if not list_c:
    print("Lista este goala")
else:
    print("Lista nu este goala")

# 8. Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# Folosește o funcție că să afișezi Elevii (cheile)
dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
print(dict1.keys())
# SAU:
for i in dict1.keys():
    print(i)

# 9. Printează cei 3 elevi și notele lor
# Ex: ‘Ana a luat nota {x}’
# Doar nota o vei lua folosindu-te de cheie
print(f'Ana a luat nota {dict1["Ana"]}')
print(f'Gigel a luat nota {dict1["Gigel"]}')
print(f'Dorel a luat nota {dict1["Dorel"]}')
# SAU
# note = [*dict1.values()]
# print(note)
# print(f"Ana a luat nota {note[0]}")
# print(f"Gigel a luat nota {note[1]}")
# print(f"Dorel a luat nota {note[2]}")

# 10. Dorel a făcut contestație și a primit 6
# ● Modifică nota lui Dorel în 6
# ● Printează nota după modificare
dict1["Dorel"] = 6
print(dict1["Dorel"])
# SAU folosind metoda update()
dictDorel = {"Dorel": 6}
dict1.update(dictDorel)
print(dict1["Dorel"])

# 11. Gigel se transferă din clasă
# ● Căuta o funcție care să îl șteargă
# ● Vine un coleg nou. Adaugă Ionică, cu nota 9
# ● Printează noii elevi
# Sterge "Gigel" folosind metoda pop()
dict1.pop("Gigel")
print(dict1)
# SAU folosind del keyword
# del dict1["Gigel"]
# print(dict1)
# Adauga "Ionica" cu nota 9 by creating a new key
dict1["Ionica"] = 9
print(dict1)
# SAU folosind metoda update()
# dict1.update({"Ionel": 9})
# print(dict1)

'''
12. Set
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
● Adaugă în zilele_sapt ‘luni’
● Afișeaza zile_sapt
'''
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
zile_sapt.add('luni')
print(zile_sapt)

# 13.Folosește un if și verifică dacă:
# ● Weekend este un subset al zilelor din săptămânii.
# ● Weekend nu este un subset al zilelor din săptămânii.
if weekend.issubset(zile_sapt):
    print("Weekend este un subset al zilelor saptamanii")
else:
    print("Weekend nu este un subset al zilelor saptamanii")

# 14. Afișează diferențele dintre aceste 2 seturi.
diferenta = zile_sapt - weekend
print(diferenta)
# SAU
print(zile_sapt.difference(weekend))

# 15. Afișază intersecția elementelor din aceste 2 seturi.
# intersectia = zile_sapt and weekend
# print(intersectia)
#SAU
print(zile_sapt.intersection(weekend))

nota_trecere = 4.5
nota = float(input('Alege nota: '))
if nota > nota_trecere:
    print(f'Ai luat nota {nota}')
    print("Ai trecut examenul")