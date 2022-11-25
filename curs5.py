# Structuri repetitive - CONTINUARE
#
# # Exercitiul 1: For in for => parcurgerea unei matrici
# my_list = [
#     [1, "test1"],
#     [2, "test2", 3, "test3"],
#     [34, "test4"],
#     [5]
# ]
#
# for i in range(len(my_list)):
#     for j in range(len(my_list[i])):
#         print(f'Valoarea curenta a elementlui din lista de pe pozitia [{i}][{j}] este: {my_list[i][j]}')
#
# # Exercitiul 2: Parcurgeti o lista de elemente, printati elementele pe ecran.
# # Daca intalniti stringul 'gutui' inlocuiti-l cu 'caise'
#
# fructe = ['gutui', 'prune', 'mere', 'pere']
#
# for i in range(len(fructe)):
#     print(fructe[i])
#     if fructe[i] == 'gutui':
#         fructe[i] = 'caise'
# print(fructe)
#
# # Exercitiul 3:
# # Avem o lista de culori. Si vrem sa vindem haine in culorile respective
# # cand vine un cumparator vrem sa ii prezentam haine in culorile alese de el
# # adica, daca cumparatorul ne spune ca nu ii place culoarea x, ii vom exclude de la prezentare hainele
# # in culoarea respectiva
# #
# # culori_disponibile = ['rosu', 'roz', 'verde', 'galben', 'violet', 'magenta', 'maro', 'albastru']
# # culori_nepotrivite = ['galben', 'albastru', 'maro']
# #
# # for culoare in range(len(culori_disponibile)):
# #     if culori_disponibile[culoare] in culori_nepotrivite:
# #         break
# #     print(f'Va recomandam haine in culoarea {culori_disponibile[culoare]}')
#
# # Structura FOR EACH
# # diferenta intre for si for eaach:
# # la for stocam indexul elemntului in variabila de la iteratie
# # iar la for each stocam elementul in variabila de la iteratie
#
# # Exercitiul 4: parcurge lista de animale si daca intalnim soarece il stergem
# animale = ['cal', 'pisica', 'caine', 'magar', 'soarece', 'oaie', 'vaca']
#
# # Varianta cu for
# # for animal in range(len(animale)-1):
# #     if animale[animal] == 'soarece':
# #         animale.pop(animal)
# # print(animale)
#
# # Varianta for each
# # Nu putem folosi pop, pt ca functiia pop ia ca si parametru indexul
# # folosim remove() care ia ca si parametru chiar valoarea
# for animal in animale:
#     if animal == 'soarece':
#         animale.remove(animal)
# print(animale)
#
# # For Else
# # Putem avea ELSE ca parte a structurilor repetitive while, for si for each (OPTIONAL)
# # Else-ul se executa O SINGURA DATA LA FINAL
#
# for i in range(0, 6):
#     print(i)
# else:
#     print("Gata!")
#
# i = 0
# while i <= 5:
#     print(i)
#     i += 1
# else:
#     print("Gata!")


# FUNCTII
# O modalitate prin care putem 'economisi' cod
# Functia se defineste cu keywordul DEF (def defineste inceputul unei functii)
# Functiile trebuie sa aiba un nume sugestiv
# Functia are mereu () dupa nume si : dupa paranteze
# () => reprezentant al zonei unde putem pune sau nu parametrii
# : => reprezentant al zonei de inceput al corpului unei functii
# Functia poate avea optiunea de RETURN (return este un keyword)
# Corpul functiei este marcat de indentare fata de marginea fisierului
# Functia tebuie sa fie apelata pentru a o folosi
# Apelarea functiei se face cu numele functiei() (include parantezele)
# Odata declarata functie, ea poate fi apelata ori de cate ori este nevoie!
# Fiecare apel al functiei ne executa codul din corpul functiei

# # 1. Functii simple (functii fara parametrii)
# def print_noapte_buna():
#     print("Noapte buna!")  # => Acesta este continutul corpului functiei, definit prin intermediul indentarii
#     print("Este ora 8.")
#
#
# # print_noapte_buna()
# #
# # print_noapte_buna()
# #
# # print_noapte_buna()
#
# x = print_noapte_buna()
# print(f"x este {x}")
#
#
# def print_noapte_buna1():
#     print("Noapte buna!")
#     print("Este ora 8.")
#     msg = "Sunt obosit"
#     return msg
#
#
# y = print_noapte_buna1()
# print(f"x este {y}")
#
#
# # Exercitiu: Suma a doua numere
# # calculeaza_suma()  # Functia trebuie mai intai definita si apoi apelata!!
# def calculeaza_suma():
#     a = 3
#     b = 4
#     suma = a + b
#     print(f'Suma numerelor {a} si {b} este {suma}')
#     return suma
#
#
# calculeaza_suma()
#
#
# # 2. Functii cu parametrii
# # Parametrii(aici a si b) se pun in parantezele rotunde atunci cand definim functia
# # Atunci cand apelam functia, ce punem intre paranteze se numesc ARGUMANTE(aici 2 si 8)
# def calc_suma(a, b):
#     suma = a + b
#     print(f'Suma celor doua numere este {suma}')
#     return suma
#
#
# x = calc_suma(2, 8)
# calc_suma(2, 3)
# print(f'x este {x}')

# 3. Functii cu numar indefinit de parametrii
# Ne folosim de keywordul * atunci cand nu stim cati parametrii vom avea
def calculeaza_pretul(*nr):
    pret = 0  # definim si initializam var pret cu valoarea 0
    for element in nr:
        pret = pret + element
    return pret


# SAU
def calculeaza_pretul2(*nr):
    pret = 0
    for i in nr:
        pret += i
    return pret


print(calculeaza_pretul(2, 6, 7))
print(calculeaza_pretul(1, 3))
print(calculeaza_pretul(2, 6, 7, 8, 5, 6, 4))
print(calculeaza_pretul("casa", "masina"))  # aici avem o eroare deoarece nu putem insuma nr 0 cu strings