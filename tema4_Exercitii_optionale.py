# Tema 4: Exercitii optionale

'''
1.
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
Itereaza prin listă alte_numere
Populează corect celelalte liste
Afișeaza cele 4 liste la final
'''
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
for numar in alte_numere:
    if numar % 2 == 0:
        numere_pare.append(numar)
    else:
        numere_impare.append(numar)
    if numar > 0:
        numere_pozitive.append(numar)
    else:
        numere_negative.append(numar)
print(f'Lista cu numere pare este {numere_pare}')
print(f'Lista cu numere impare este {numere_impare}')
print(f'Lista cu numere pozitive este {numere_pozitive}')
print(f'Lista cu numere negative este {numere_negative}')

'''
2. Aceeași listă:
Ordonează crescător lista fară să folosești sort.
Te poți inspira vizual de aici.
https://www.youtube.com/watch?v=lyZQPjUT5B4
'''
print()
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
for i in range(len(alte_numere)):
    for j in range(0, len(alte_numere)-i-1):
        if alte_numere[j] > alte_numere[j+1]:
            alte_numere[j], alte_numere[j+1] = alte_numere[j+1], alte_numere[j]
    else:
        continue
print(alte_numere)

# SAU
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
for i in range(len(alte_numere)):
    for j in range(i + 1, len(alte_numere)):
        if alte_numere[i] > alte_numere[j]:
            alte_numere[i], alte_numere[j] = alte_numere[j], alte_numere[i]
print(alte_numere)

'''
3. Ghicitoare de număr:
numar_secret = Generați un număr random între 1 și 30
Numar_ghicit = None
Folosind un while
User alege un număr

Programul îi spune:
● Nr secret e mai mare
● Nr secret e mai mic
● Felicitări! Ai ghicit!
'''
import random
numar_secret = random.randint(1, 30)
numar_ghicit = None
while True:
    numar_ghicit = int(input("Alege un numar de la 1 la 30: "))
    if numar_ghicit > numar_secret:
        print("Nr secret e mai mic")
    elif numar_ghicit < numar_secret:
        print("Nr secret e mai mare")
    elif numar_ghicit == numar_secret:
        print("Felicitari! Ai ghicit!")
        break

'''
4. Alege un număr de la tastatură
Ex: 7
Scrie un program care să genereze în consolă următoarea piramidă
1
22
333
4444
55555
666666
7777777

Ex:3
1
22
333
'''
numar = int(input("Alege un numar: "))
for i in range(numar):
    for j in range(i+1):
        print(i+1, end="")
    print()
    i += 1

# SAU
nr = int(input("Scrie un numar: "))
i = 1
while i <= nr:
    print(' ')
    for j in range(i):
        j = i
        print(j, end='')
        j = j + 1
    i = i + 1

'''
5.
tastatura_telefon = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9],
[0]
]
Iterează prin listă 2d
Printează ‘Cifra curentă este x’
(hint: nested for - adică for în for)
'''
print()
tastatura_telefon = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9],
[0]
]
for i in range(len(tastatura_telefon)):
    for j in range(len(tastatura_telefon[i])):
        print(f'Cifra curenta este {tastatura_telefon[i][j]}')

# sau cu for each
for row in tastatura_telefon:
    for column in row:
        print(f'FOR EACH: Cifra curenta este {column}')
