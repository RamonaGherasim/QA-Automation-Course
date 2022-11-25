# Tema 5: Functii
# Exerictii obligatorii

# 1.Funcție care să calculeze și să returneze suma a două numere
def calc_suma(a, b):
    suma_num = a + b
    return suma_num


print(f'Suma numerelor  103 si 547 este {calc_suma(103, 547)}')
print(f'Suma numerelor 8.45 si 10.55 este {calc_suma(8.45, 10.55)}')


# 2. Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar
def este_num_par(a):
    if a % 2 == 0:
        return True
    else:
        return False


print(f'2 este un numar par: {este_num_par(2)}')
print(f'7 este un numar par: {este_num_par(7)}')


# 3. Funcție care returnează numărul total de caractere din numele tău complet.
# (nume, prenume, nume_mijlociu)
def total_char(nume, prenume, nume_mijlociu):
    num_char = len(nume) + len(prenume) + len(nume_mijlociu)
    return num_char


print(total_char('Alexandra', 'Ramona', 'Gherasim'))
print(total_char('Alex', 'Valentin', ''))


# 4. Funcție care returnează aria dreptunghiului
def calc_aria_dreptunghi(lungime, latime):
    aria = lungime * latime
    return aria


print(f'Aria dreptunghiului este {calc_aria_dreptunghi(10, 6)}')
print(f'Aria dreptunghiului este {round(calc_aria_dreptunghi(20.5, 5.7), 2)}')


# 5. Funcție care returnează aria cercului
# def calc_aria_cerc(raza):


# 6. Funcție care returnează True dacă un caracter x se găsește într-un string dat
# și False dacă nu găsește.
def gaseste_char(my_string, caracter):
    if caracter in my_string:
        return True
    else:
        return False


my_string = 'Am rezolvat problema!'
caracter = 'x'
print(f'{caracter} se fla in propozitia {my_string}: {gaseste_char(my_string, caracter)}')
print(f'z se afla in propozitia mea: {gaseste_char(my_string, "z")}')


# 7. Funcție fără return, primește un string și printează pe ecran:
# ● Nr de caractere lower case este x
# ● Nr de caractere upper case exte y
def upper_lower_in_string(string):
    uppercase = 0
    lowercase = 0
    for i in range(len(string)):
        if string[i].islower():
            lowercase += 1
        elif string[i].isupper():
            uppercase += 1
    print(f'''
    Nr de caractere lower case este: {lowercase}
    Nr de caractere upper case este: {uppercase}
    ''')


upper_lower_in_string('Am rEzolvat-o sI pE asTA!')
upper_lower_in_string('AceSta ESTE stringuL meu*')


# 8. Funcție care primește o LISTA de numere și returnează o LISTA doar cu
# numerele pozitive
def numere_pozitive(lista):
    lista_pozitive = []
    for num in lista:
        if num > 0:
            lista_pozitive.append(num)
    return lista_pozitive


lista = [1, 6, -8, 5, 9, -1, 4]
print(f'Lista cu numere pozitive este {numere_pozitive(lista)}')


# 9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA
# ● Primul număr x este mai mare decat al doilea nr y
# ● Al doilea nr y este mai mare decat primul nr x
# ● Numerele sunt egale.

def compara_num(x, y):
    if x > y:
        print(f'Primul numar {x} este mai mare decat al doilea numer {y}')
    elif y > x:
        print(f'Al doilea numar {y} este mai mare decat primul numar {x}')
    else:
        print('Numerele sunt egale')


compara_num(5, 7)
compara_num(7, -5)
compara_num(2.4, 1.8)


# 10. Funcție care primește un număr și un set de numere.
# ● Printeaza ‘am adaugat numărul nou în set’ + returnează True
# ● Printeaza ‘nu am adaugat numărul în set. Acesta există deja’ +
# returnează False

def adauga_num_in_set(numar, set_num):
    if numar in set_num:
        print('Nu am adaugat numarul in set, acesta exista deja')
        return False
    else:
        print('Am adaugat numarul nou in set')
        return True


numar = 3
set_num = {7, 12, 3, -8, 5.4}
print(adauga_num_in_set(numar, set_num))
print(adauga_num_in_set(14, {12, 1, 0, -6, 87.2}))


# Exercitii optionale
# 1. Funcție care primește o lună din an și returnează câte zile are acea luna
def zile_in_luna(luna):
    luna_30_zile = ["Aprilie", "Iunie", "Septembrie", "Noiembrie"]
    if luna in luna_30_zile:
        return "30 zile"
    elif luna == "Februarie" or luna == "februarie":
        return "28 zile"
    else:
        return "31 zile"


print(f'Aprilie are {zile_in_luna("Aprilie")}')
print(f'Februarie are {zile_in_luna("Februarie")}')
print(f'Decembrie are {zile_in_luna("Decembrie")}')


# 2. Funcție calculator care să returneze 4 valori. Suma, diferența, înmulțirea,
# împărțirea a două numere.
def calculator(a, b):
    suma = a + b
    diferenta = a - b
    inmultirea = a * b
    impartirea = a / b
    return f'''
Suma este {str(suma)}
Diferenta este {str(diferenta)}
Inmultirea este {str(inmultirea)}
Impartirea este {str(round(impartirea, 2))}'''


print(calculator(10, 5))
print(calculator(-10, 2))


# 3. Funcție care primește o lista de cifre (adică doar 0-9)
# Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
# Returnează un DICT care ne spune de câte ori apare fiecare cifră
# => dict {
# 0: 0
# 1 :2
# 2: 0
# 3: 1
# 4: 0
# 5: 3
# 6: 0
# 7: 2
# 8: 0
# 9: 1
# }
def numara_cifre(lista):
    dict_num = {}
    for i in lista:
        dict_num[i] = lista.count(i)
    return dict_num


print(numara_cifre([0, 1, 4, 8]))
print(numara_cifre([1, 3, 1, 5, 9, 7, 7, 5, 5]))


# 4. Funcție care primește 3 numere. Returnează valoarea maximă dintre ele
def gaseste_max(a, b, c):
    return max(a, b, c)


print(f'Numarul maxim este {gaseste_max(3, 9, 12)}')
print(f'Numarul maxim este {gaseste_max(-8, 5.5, 7.2)}')


# 5. Funcție care să primească un număr și să returneze suma tuturor numerelor
# de la 0 la acel număr
# Exemplu: daca dam nr 3. Suma va fi 6 (0+1+2+3)
def suma_num(x):
    suma = 0
    for i in range(x+1):
        suma += i
    return suma


print(f'Suma tuturor numerelor de la 0 la numarul tau este {suma_num(3)}')
print(f'Suma tuturor numerelor de la 0 la numarul tau este {suma_num(12)}')

# Exercitii optionale - Bonus
# 1.Funcție care primește 2 liste de numere (numerele pot fi dublate). Returnați numerele comune
# Exemplu:
# list1 = [1, 1, 2, 3]
# list2 = [2, 2, 3, 4]
# Răspuns: {2, 3}
def elem_comune(list1, list2):
    # Metoda 1:
    # comune = []
    # for i in list1:
    #     if i in list2:
    #         comune.append(i)
    # return set(comune)

    # Metoda 2:
    return set(list1) & set(list2)


list1 = [1, 1, 2, 3]
list2 = [2, 2, 3, 4]

print(elem_comune(list1, list2))


# 2. Funcție care să aplice o reducere de preț
# Dacă produsul costa 100 lei și aplicăm reducere de 10%. Pretul va fi 90
# Tratați cazurile în care reducerea e invalida. De exemplu o reducere de 110% e invalidă.
def aplica_reducere(pret, reducere):
    reducere2 = pret * reducere/100
    if reducere2 < 100:
        pret_final = pret - reducere2
        return pret_final
    else:
        return "Reducerea este invalida"


print(aplica_reducere(100, 20))
print(aplica_reducere(100, 100))


# 3. Funcție care să afișeze data și ora curentă din ro
# (bonus: afișați și data și ora curentă din China)
import pytz
from datetime import datetime


def afiseaza_ora_curenta(timezone):
    ora_curenta = datetime.now(timezone)
    data = ora_curenta.strftime("%d-%m-%y")
    ora = ora_curenta.strftime("%H:%M:%S")

    return "Data este " + data + " si ora este " + ora


timezone_ro = pytz.timezone('Europe/Bucharest')
timezone_ch = pytz.timezone('Asia/Shanghai')

print(f'Ro: {afiseaza_ora_curenta(timezone_ro)}')
print(f'China: {afiseaza_ora_curenta(timezone_ch)}')


# 4. Funcție care să afișeze câte zile mai sunt până la ziua ta / sau până la Crăciun dacă nu vrei să ne zici cand
# e ziua ta :)
from datetime import date


def numaratoare_Craciun():
    craciun = date(year=2022, month=12, day=25)
    zile_pana_la_craciun = (craciun - date.today()).days
    return zile_pana_la_craciun


print(f'Mai sunt {numaratoare_Craciun()} zile pana la Craciun')