from abc import abstractmethod, ABC
# ******** 4. ABSTRACTIZARE  ********

# => Posibilitatea templetizarii anumitor metode dintr-o clasa
# => Un proces prin care putem sa ascundem o anumita functionalitate specifica fata de un utilizator si de asemenea de a
# putea forta un anumit comportament in clasele mostenitoare
# => Utilizatorul stie ce face functionalitatea, dar nu si cum o face
# => Orice clasa care mosteneste o clasa abstracta va fi obligata sa implementeze un comportament definit in clasa
# abstracta

# Exista doua forme de abstractizare:
   # * cand toate metodele din clasa sunt abstracte (=> clasa se va numi interfata si va contine doar functii abstracte)
   # * cand doar unele metode din clasa sunt abstracte (=> clasa se va numi clasa abstracta si va contine atat functii
#      abstracte cat si functii proprii, definite)

# !!! Atentie, daca definim o clasa copil care mostenste o clasa abstracta / interfata si nu implementam metodele
# abstracte, atunci vom primi o eroare !!!

# => O metoda abstracta = o metoda care nu are corp
# => Metodele sunt marcate ca si abstracte prin intermediul unui DECORATOR
#      Decorator este un set de instructiuni grupate sub un nume care pot sa schimbe comportamentul unei functii
#        @abstractmethod = este un decorator care marcheaza o functie ca fiind abstracta;
#        @staticmethod = este un decorator care marcheaza o functie ca fiind statica (adica poate fi accesata prin
#        intermediul clasei)


from abc import ABC, abstractmethod  # avem nevoie de importurile acestea pentru abstractizare in python
from functools import wraps


# Definim clasa Car care mosteneste conceptul de abstractizare (fara mostenirea asta nu o putem face abstracta)
class Car(ABC):

    @abstractmethod  # am folosit un decorator ca sa marcam metoda ca abstracta
    def accelerate(self):  # am inceput definirea metodei abstracte = metode fara corp (logica interna)
        # in general metodele abstracte nu trebuie sa aiba logica, si atunci pentru a nu avea erori avem doua optiuni:
        # scriem pas SAU raise.
        # raise NotImplementedError - ridicam o exceptie de NotImplemented
        pass

    # O clasa abstracta poate sa contina si metode normale (care au logica interna). Definim o metoda normala.
    # Nu este obligatoriu sa implementam metodele de clasa, cu logica, in clasele mostenitoare
    # Decoratorul classmethod e optional, dar de regula il punem pentru claritate
    def stop(self):
        print("STOP!")


# Aici am definit o clasa noua numita Ferrari care mosteneste clasa abstracta Car, ceea ce inseamna ca noi vom fi
                        # fortati sa implementam metoda abstracta accelerate

def upper_case(func):
    @wraps(func)
    def func_wrapper(text):
        return func().upper()
    return func_wrapper


@upper_case
def accelerate(text):
    print(text)


accelerate("text")


class Ferrari(Car):
    culoare = None

    def accelerate(self):  # daca nu am avea metoda asta definita, am primi o exceptie de tip NotImplementedError
        print("test")  # puteti sa incercati sa o comentati sa vedeti ce se intampla

    def stop(self):  # poly
        print("I'm a F, I can't stop")


# Am implementat din nou o clasa care mosteneste clasa abstracta Car. Aici de asemenea suntem obligati sa implementam
# metoda accelerat
class Lastun(Car):
    def accelerate(self):
        print("I'm accelerating from 0 to 100 in 15 seconds")


f = Ferrari()
# f.accelerate()
f.stop()

l = Lastun()
l.accelerate()
l.stop()


# Mai jos am definit o Interfata - adica o clasa abstracta in care toate metodele sunt abstracte (An interface is a completely "abstract class")
# Obliga clasele mostenitoare sa implementeze functiile, e ca o reteta pentru subclase
class Animal(ABC):  # unde ABC  =  Abstract Base Class

    @abstractmethod  # decorator care marcheaza metoda ca fiind abstracta
    def sound(self):
        raise NotImplementedError

    #  pass = cuvant cheie care defineste faptul ca corpul metodei nu are o logica efectiva, dar este folosit pentru ca
    #         acea metoda sa poata sa aiba un corp
    #  raise NotImplementedError = modalitate prin care putem sa fortam in mod explicit exceptia de not implemented

    @abstractmethod
    def sleep(self):
        pass


# Atunci cand o clasa mosteneste o alta clasa de tip interfata sau clasa abstracta, spunem ca o implementeaza
class Dog(Animal):

    def sound(self):
        print('Ham Ham!')

    def sleep(self):
        print('zzzzzzzzz')

    def describe(self):
        print('I have an owner')


class Cat(Animal):
    def sound(self):
        print('Miau Miau!')

    def sleep(self):
        print('prrrrr')

    def describe(self):
        print('I own a human')

azorel = Dog()
tom = Cat()

azorel.sleep()
azorel.sound()
azorel.describe()

tom.sleep()
tom.sound()
tom.describe()