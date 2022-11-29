# Continuare PILONI OOP

# Mostenirea - cel mai des folosita
# Encapssularea
# Polimorfismul
# Abstractizarea

# I. Mostenirea
# Clasa parinte <=> Clasa copil.
# Clasa copil mosteneste/imprumuta metodele si atributele clasei parinte
# Clasa copil poate avea si metode si atribute specifice ei
# Evitam duplicarea codului (a metodelor si atributelor care sunt comune)
# Putem avea 3 tipuri:
# 1. unica: Parinte <-> copil
# 2. pe mai multe niveluri: Parinte - Copil - Copil1
# 3. multipla: orice atribut este cautat in clasa parine printr-un algoritm. Poate aparea problema "ddiamantului" - deci
# nu este foarte indicat sa o utilizam

# Definim classa parinte
class Chef:
    # atribute
    cutite = None
    linguri = None

    # constructor
    def __init__(self, numar_cutite):
        self.numar_cutite = numar_cutite

    # metode
    def make_salad(self):
        print("Salad")

    def make_fries(self):
        print("Fries")


# A doua clasa parinte
class Chef2:
    # atribute
    sort = 2


# Definim clasa copil (subclasa)
# Aceasta va mosteni din clasa Chef. Pt asta ii vom da in paranteza param 'Chef'
class JapaneseChef(Chef):
    # constructor propriu
    def __init__(self, cantitate_alge, cutite):
        self.alge = cantitate_alge
        self.cutite = cutite

    # metoda proprie
    def make_sushi(self):
        print('Sushi')


# Definim a doua clasa copil (subclasa)
# Aceasta va mosteni din ambele clase parinte (Chef si Chef2). Pt asta ii vom da in paranteza param 'Chef' si 'Chef2'
class ItalianChef(Chef, Chef2):
    # atribut propriu
    tava = 1

    # metoda proprie
    def make_pizza(self):
        print("Pizza")


new_chef = Chef(4)
new_chef.make_fries()

japan_chef = JapaneseChef(13, 5)
japan_chef.linguri = 6
print(japan_chef.linguri)
japan_chef.make_sushi()
japan_chef.make_salad()

mario_chef = ItalianChef(3)
print(f'Cheful are {mario_chef.tava} tava/tavi.')
print(f'Cheful are {mario_chef.sort} sort/sorturi.')
print(f'Cheful are {mario_chef.linguri} lingura/linguri.')
mario_chef.linguri = 15
print(f'Cheful are {mario_chef.linguri} lingura/linguri.')


# Ex de mostenire pe niveluri: O clasa copil TokyoChef - mosteneste din clasa copil JapaneseChf - care la randul ei
# mosteneste de la clasa parinte Chef
class TokyoChef(JapaneseChef):
    # atribute proprii
    alge = 300


# Constuctorii claselor de baza vor fi enumerati in ordine => aici avem nevoie doar de param pt clasa JapaneseChef
san_chef = TokyoChef(153, 7)
san_chef.make_salad()


# Exercitiul 2: Clasa de baza animale si o clasa copil Pisica care mosteneste clasa Animale
class Animale():
    # atribute
    sunet = None
    culoare = None
    specia = None
    varsta = 0
    sunet_somn_mancare = None

    # metode
    def dorm(self):
        print(f'Acum dorm. {self.sunet_somn_mancare}')

    def imbatranire(self):
        self.varsta += 1
        print(f'Acum am varsta de {self.varsta} ani')

# Definim clasa copil 'Pisica' care mosteneste din clasa 'Animale
class Pisica(Animale):
    # atribute proprii
    toarce = "Da"
    vaneaza_soareci = "None"

    # metode proprii
    def toarce_sa_ceri_mancare(self):
        if self.toarce == "Da":
            self.sunet_somn_mancare = "Meow"  # Aici self.sunet_somn_mancre este un atribut al clasei Pisica si nu a
                                              # al clasei Animale. Deorece inca suntem in cadrul clasei Pisica
            print(self.sunet_somn_mancare)


pisica = Animale()
pisica_mostenitoare = Pisica()
pisica.sunet = "Meow meow"
print(pisica.sunet)
print(pisica_mostenitoare.sunet)
# Chiar daca noi am schimbat valoarea atributului sunet in cadrul clasei pisica, atributul sunet din clasa pisica_mos-
# tenitoare va fi tot None, deoarece fiecare clasa mosteneste atributele nealterate(de la 0, asa cum sunt ele declarate
# in clasa parinte)

pisica.dorm()
pisica_mostenitoare.dorm()
pisica.imbatranire()
pisica_mostenitoare.imbatranire()


# II. POLIMORFISMUL

# Polimorfism prin functie cu numar indefinit de parametrii ( poate fi apelata cu cate argumente avem noi nevoie)
# -- include functiile cu *args and **kwars(specifica dictionarelor)
# E.g len() este o functie polimorfica pt ca poate fi apelata cu un numar indefinit de parametrii
print(len("abc"))
print(len([1, 2, 3, 4, 5]))


def suma_numere(*args):
    suma = 0
    for e in args:
        suma += e
    return suma


print(suma_numere(12, 89))
print(suma_numere(22, 0, 43))
print(suma_numere(3, 5, 10, 23))


# Polimorfism prin functii cu parametrii initializati cu valoare default
# Definim o functie cu comportament polimorfic pt ca am defint param y si z cu valoarea implicita 0
# Daca apelam functia cu 1 sau 2 params, nu vom primi eroare, pt ca acesti params vor lua val default 0 cand nu sunt
# declarate valori pt y si z ca si argumente
def add(x, y=0, z=0):
    return x + y + z


print(add(3))  # aici y va lua valoarea implicita 0, si z va lua valoarea implicita 0
print(add(3, 5))   # aici z va lua valoarea implicita 0
print(add(5, 7, 1))

# Polimorfism prim implementarea aceleasi metode in doua clase diferite
class America:
    # atribute
    limba = "engleza"
    dreapel = "drapel american"
    imn = "imnul americii"

    # metode
    def printeaza_limba(self):
        print(f'Limba care se vorbeste in America este {self.limba}')


class Romania:
    # atribute
    limba = "romana"
    drapel = "tricolor"
    imn = "Desteapta-te romane"

    # metode
    def printeaza_limba(self):
        print(f'Limba care se vorbeste in Romania este {self.limba}')


american = America()
roman = Romania()

american.printeaza_limba()
roman.printeaza_limba()

# Polimorfism prin reimplementarea metodei din clasa parinte in clasa copil
# definim clasa parinte
class Pasare:
    # metode
    def describe(self):
        print("Sunt o pasare")

    def zboara(self):
        print("Sunt o pasare, deci zbor")


# definim clasa copil
class Papagal(Pasare):
    def vorbeste(self):
        print("Sunt o pasare si vorbesc, deci sunt papagal.")


class Pinguin(Pasare):
    def zboara(self):
        print("Nu pot zbura, dar sunt imbracat frumos")


pasare_1 = Pasare()
pasare_1.describe()
pasare_1.zboara()
print("*****")

papagal_1 = Papagal()
papagal_1.describe()
papagal_1.zboara()
papagal_1.vorbeste()
print("*****")

pinguin_1 = Pinguin()
pinguin_1.describe()
pinguin_1.zboara()


# ABSTRACTIZARE
# O metoda abstracta e o metoda care nu are corp => avem doar linia aceea cu define
# Metodele sunt marcate ca si abstracte prin intermediul unui DCORATOR e.g. @abstractmethod
# La abstractizare nou cream un deplate pt anumite metode dintr-o clasa
# Abstractizarea poate fi un proces prin care ascundem implemenarea anumitor functionalitati/anumite parti de cod de
# utilizator
# Utilizatorul stie ce face metoda dar nu si cum face acel lucru, pt ca, corpul metodei nu este vizibil
# Orice clasa care mosteneste metode dintr-o clasa care are metde abstracte, sunt fortate sa aiba un anumit comportament

# Tipuri de abstractizare:
# Clasa se numeste INTERFATA: cand toate metodele sunt abstracte
# Clasa ABSTRACTA: cand doar unele/o parte din metode din clasa sunt abstracte

# ATENTIE: daca mostenim dintr-o clasa cu metode abstracte, iar acele metode in clasa copil nu urmeaza comportamentul
# metodei abstracte, vom primi o eroare

# Exista si decoratorul @staticmethod care defineste o clasa statica


# ENCAPSULARE => tipuri de accesare
# Posibilitatea ascunderii unor anumite atribute si restrictionarea utilizarii lor
# Kewywordurile Public(acces la atribute si metode de oriunde in program), Private(acces la atribute si metodde doar in
# interiorul clasei) si Protected(acces doar in cadrul aceluiasi pachet in care exista/se afla clasa)
# Keywordurile se folosesc in fata