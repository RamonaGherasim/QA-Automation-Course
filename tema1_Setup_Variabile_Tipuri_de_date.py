# Tema 1: Setup, Variabile si Tipuri de date

# 1. In cadrul unui comentariu, explica cu cuvintele tale ce este o variabila.
# O variabila este o portiune de memorie careia ii este alocata o valoare.

# 2. Declară și initializează câte o variabilă din fiecare din următoarele tipuri de variabilă:
# - string
# - int
# - float
# - bool
# Observație: Valorile vor fi alese de tine după preferințe.
course_name = "Automated testing"  # this is a string
no_live_lessons = 15  # this is an integer
lesson_length = 2.5  # this is a float
online = True  # this is a boolean

# 3. Utilizează funcția type pentru a verifica dacă au tipul de date așteptat.
print(type(course_name))  # => <class 'str'> expected
print(type(no_live_lessons))  # => <class 'int'> expected
print(type(lesson_length))  # =>  <class 'float'> expected
print(type(online))  # => <class 'bool'> expected

# 4. Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în aceeași variabilă (suprascriere):
# - Verifică tipul acesteia.
lesson_length = round(lesson_length)
print(lesson_length)  # => this will now be 2 (2.5 rounded is 2)
print(type(lesson_length))  # => <class 'int'> expected

# 5. Folosește print() și printează în consola 4 propoziții folosind cele 4 variabile.
# Rezolvă nepotrivirile de tip prin ce modalitate dorești.
print(f'The course that I have registered to is called {course_name}.')
print(f'This course includes {no_live_lessons} live sessions.')
print(f'Each session is {lesson_length} hours long.')
if online:
    print('The session are currently held online')
else:
    print('The session are currently held in person')

# 6. Citește de la tastatură:
# - numele;
# - prenumele.
# Afișează: 'Numele complet are x caractere'.
surname = input('What is your surname?')
first_name = input('What is your firstname?')
print(f'Your full name has {len(surname + first_name)} characters')  # + operator concatenates the two strings into one
                                                                     # len() function counts the no of characters in the
                                                                      # newly created string

# 7. Citește de la tastatură:
# - lungimea;
# - lățimea.
# Afișează: 'Aria dreptunghiului este x'.
length = int(input('Type the length here'))  # we transform the info from keyboard in integer
width = int(input('Type the width here'))  # # we transform the info from keyboard in integer
print(f'The are of the rectangle is {length * width}')

# 8. Având stringul: 'Coral is either the stupidest animal or the smartest rock':
# - afișează de câte ori apare cuvântul 'the';
sentence = 'Coral is either the stupidest animal or the smartest rock'
print(sentence.count(' the '))  # => 2 expected
                                  # count() method takes the argument and returns the no of times those characters in
                                   # the argument appear/exist in the string associated with the method.
                                    # Note: if we have passed the argument 'the' the result would be 3 as word 'either'
                                     # has the characters 'the' in it. But the question was how many time the WORD 'the'
                                     # appears in the given string/sentence.

# 9. Același string.
# ● Afișează de câte ori apare cuvântul 'the';
# ● Printează rezultatul.
sentence = 'Coral is either the stupidest animal or the smartest rock'
a_sentence = sentence.split()
print(f'The word "the" appears {a_sentence.count("the")} times in your sentence')  # => The word "the" appears 2 times
                                                                                    # in your sentence - expected
                                                                                     # another method to ensure that
                                                                                      # only the WORD 'the' is counted

# 10. Același string.
# ● Folosiți un assert ca să verificați dacă acest string conține doar numere.
sentence = 'Coral is either the stupidest animal or the smartest rock'
assert sentence == int, 'Your sentence is not an integer'  # the message after the comma will be written if the code
                                                            # returns False.


