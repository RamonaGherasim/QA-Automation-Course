# Tema 4: Functii
# Exercitii obligatorii

'''
1.Având lista:
mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
'Fiat', 'Trabant', 'Opel']
Folosește un for că să iterezi prin toată lista și să afișezi;
● ‘Mașina mea preferată este x’.
● Fă același lucru cu un for each.
● Fă același lucru cu un while.
'''
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
'Fiat', 'Trabant', 'Opel']

# Folosind For
for i in range(len(masini)):
    print(f'1: Masina mea preferata este {masini[i]}')

print()
# Folosind For Each
for masina in masini:
    print(f'2: Masina mea preferata este {masina}')

print()
# Folosind While
i = 0
while i <= len(masini)-1:
    print(f'3: Masina mea preferata este {masini[i]}')
    i += 1
# # SAU
print()
i = 0
while True:
    print(f'4: Masina mea preferata este {masini[i]}')
    i += 1
    if i == len(masini):
        break

# '''
# 2. Aceeași listă:
# Folosește un for else
# În for:
# - Modifică elementele din listă astfel încât să fie scrise cu majuscule,
# exceptând primul și ultimul.
# În else:
# - Printează lista.
# '''
print()
for i in range(len(masini)):
    masini[i] = masini[i].upper()
    if i == 0 or i == len(masini)-1:
        masini[i] = masini[i].title()
else:
    print(masini)

# SAU
for i in range(1, len(masini)-1):  # ne deplasasm de la a2a pozitie pana la penultima
    masini[i] = masini[i].upper()
print(masini)

'''
3. Aceeași listă:
Vine un cumpărător care dorește să cumpere un Mercedes.
Itereaza prin ea prin modalitatea aleasă de tine.
Dacă mașina e mercedes:
Printează ‘am găsit mașina dorită de dvs’
Ieși din ciclu folosind un cuvânt cheie care face acest lucru
Altfel:
Printează ‘Am găsit mașina X. Mai căutam‘
'''
print()
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
'Fiat', 'Trabant', 'Opel']
for masina in masini:
    if masina == "Mercedes":
        print(f"Am gasit masina dorita de dumneavoastra: {masina}")
        break
    else:
        print(f"Am gasit masina {masina}. Mai cautam!")

'''
4. Aceași listă:
Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu
excepția Trabant și Lăstun.
- Dacă mașina e Trabant sau Lăstun:
Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie
else).
- Printează S-ar putea să vă placă mașina x.
'''
print()
for masina in masini:
    if masina == "Trabant" or masina == "Lăstun":
        continue
    print(f"S-ar putea sa va placa masina {masina}")

'''
5. Modernizează parcul de mașini:
● Crează o listă goală, masini_vechi.
● Itereaza prin mașini.
● Când găsesti Lăstun sau Trabant:
- Salvează aceste mașini în masini_vechi.
- Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).

● Printează Modele vechi: x.
● Modele noi: x.
'''
print()
masini_vechi = []
i = 0
while i < len(masini):
    if masini[i] == "Trabant" or masini[i] == "Lăstun":
        masini_vechi.append(masini[i])
        masini[i] = "Tesla"
    i += 1
print(f'Modele vechi: {masini_vechi}')
print(f'Modele noi: {masini}')

'''
6. Având dict:
pret_masini = {
'Dacia': 6800,
'Lăstun': 500,
'Opel': 1100,
'Audi': 19000,
'BMW': 23000
}
Vine un client cu un buget de 15000 euro.
● Prezintă doar mașinile care se încadrează în acest buget.
● Itereaza prin dict.items() și accesează mașina și prețul.
● Printează Pentru un buget de sub 15000 euro puteți alege mașină
xLastun
● Iterează prin listă.
'''
print()
pret_masini = {
'Dacia': 6800,
'Lăstun': 500,
'Opel': 1100,
'Audi': 19000,
'BMW': 23000
}

for name, value in pret_masini.items():
    if pret_masini[name] < 15000:
        print(f'Pentru un buget de sub 15000 euro puteti alege masina {name} la pretul de {pret_masini[name]}euro')

'''
7. Având lista:
numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
● Iterează prin ea.
● Afișează de câte ori apare 3 (nu ai voie să folosești count).
'''
print()
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
nr_aparitii = 0
for numar in numere:
    if numar == 3:
        nr_aparitii += 1
print(f'Numarul 3 apare de {nr_aparitii} ori in lista')

'''
8. Aceeași listă:
● Iterează prin ea
● Calculează și afișează suma numerelor (nu ai voie să folosești sum).
'''
print()
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
suma = 0
for numar in numere:
    suma += numar
print(f'Suma numerelor din lista este {suma}')

'''
9. Aceeași listă:
● Iterează prin ea.
● Afișază cel mai mare număr (nu ai voie să folosești max).
'''
print()
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
nr_max = 0
for numar in numere:
    if numar > nr_max:
        nr_max = numar
print(f'Numarul maxim din lista mea este: {nr_max}')

'''
10. Aceeași listă:
● Iterează prin ea.
● Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
Ex: dacă e 3, să devină -3
● Afișază noua listă.
'''
print()
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
i = 0
while i < len(numere):
    numere[i] = numere[i] * -1
    i += 1
print(f'Lista a devenit: {numere}')

# SAU
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
lista_neg = []
for numar in numere:
    if numar > 0:
        numar = numar - numar*2
        #numar = -(abs(numar)) # alta solutie
    lista_neg.append(numar)
print(f'Lista a devenit: {lista_neg}')