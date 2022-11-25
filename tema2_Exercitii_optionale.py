# Tema 1 - Exercitii Optionale

# 1. Verifică dacă x are minim 4 cifre (x e int).
# (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre).
x = input('Type an integer')  # get a number from the keyboard
# the .lstrip() method removes any leading characters (default is space)
# used this method to ensure that negative numbers can be introduced but minus is not counted towards number of digits
# minus sign is read as a string , therefore the .isdigit() method will always give False if a negative no is introduced
# use .lstrip in this case as well to ensure a negative number is accepted as a number.
if len(x.lstrip('-')) >= 4 and x.lstrip('-').isdigit():
    print(f'{x} has at least 4 digits')
elif len(x.lstrip('-')) < 4 and x.lstrip('-').isdigit():
    print(f'{x} has less than 4 digits')
else:  # used this condition to ensure that user gets a message if they introduce letters instead of number.
    print(f'{x} is not a valid number')

# 2. Verifică dacă x are exact 6 cifre.
x = input('Type a number')
if len(x.lstrip('-')) == 6 and x.lstrip('-').isdigit():
    print(f'{x} has exactly 6 digits')
elif len(x.lstrip('-')) != 6 and x.lstrip('-').isdigit():
    print(f'{x} has not got 6 digits')
else:  # used this condition to ensure that user gets a message if they introduce letters instead of number.
    print(f'{x} is not a valid number')

# 3. Verifică dacă x este număr par sau impar (x e int).
x = int(input('Type a number'))
if x % 2 == 0:  # even number => that number / 2 will have the remainder 0 => modulus 2 is 0
    print(f'{x} is an even number')
else:
    print(f'{x} is an odd number')

# 4. x, y, z (int)
# Afișează care este cel mai mare dintre ele?
x = int(input('number x'))
y = int(input('number y'))
z = int(input('number z'))
if x > y and x > z:
    print(f'{x} is the largest number')
elif y > x and y > z:
    print(f'{y} is the largest number')
else:
    print(f'{z} is the largest number')

# 5. X, y, z - reprezintă unghiurile unui triunghi
# Verifică și afișează dacă triunghiul este valid sau nu.
# a triangle is valid if the sum of the three angles is 180 degrees, angles are a positive value and are not 0.
x = int(input('Choose first angle'))
y = int(input('Choose second angle'))
z = int(input('Choose third angle'))
if x <= 0 or y <= 0 or z <= 0:
    print('Your angle cannot be negative or 0! Try again.')
elif x + y + z == 180:
    print('Your triangle is valid')
else:
    print('Your triangle is not valid')

# 6. Având stringul: 'Coral is either the stupidest animal or the smartest rock'
# ● Citiți de la tastatură un int x
# ● Afișează stringul fără ultimele x caractere
# Exemplu: daca ati ales 7 => 'Coral is either the stupidest animal or the smarte'
my_string = 'Coral is either the stupidest animal or the smartest rock'
characters = int(input('Type a random number'))
if characters <= 0:
    print(my_string)
    print('Perhaps try a number over 0.')
elif characters >= len(my_string):
    print('Nothing left of your sentence!')
else:
    print(my_string[:len(my_string)-characters])
# Are we considering the spaces as a character?

# 7. Același string. Declară un string nou care să fie format din primele 5 caractere + ultimele 5
# use slice operator
# slice - can take 3 parameters to help capture the needed characters from a string [start:stop:step]
# start = starting index position, it's inclusive of this charac. This is 0 by default
# stop = the ending index position, it's exclusive of thi charac. This also has a default, the very end of the string
# step = capture jump from start to end jumping at the step frequency. This is 1 by default.
# to capture first n charac from a string use the slice operator: my_string[:n]
# when a negative no is used for start or stop, the charac is counted from the end of the string => last character of
# a string has index-1, second last has index -2, etc.
# to capture last n charac from a string use the slice operator: my_string[-n:]
my_string = 'Coral is either the stupidest animal or the smartest rock'
first_five = my_string[:5]
last_five = my_string[-5:]
new_string = first_five + last_five
print(new_string)

# 8. Același string.
# ● Salvează într-o variabilă și afișează indexul de start al cuvântului rock (hint: este o funcție care te ajuta sa
# faci asta)
# ● Folosind această variabilă + slicing, afișează tot stringul până la acest
# cuvant
# ● output: 'Coral is either the stupidest animal or the smartest '
my_string = 'Coral is either the stupidest animal or the smartest rock'
rock_index = my_string.index('rock')  # use .index method to find the index of the start of the word and save it in a
# variable
print(rock_index)
print(my_string[0:rock_index])

# 9. Citește de la tastatura un string
# Verifică dacă primul și ultimul caracter sunt la fel. Se va folosi un assert
# Atentie: se dorește ca programul sa fie case insensitive - 'apA' e acceptat
my_string = input('Type a string here').casefold()  # transform all the letter in the str into lower case letters
assert my_string[0] == my_string[-1], 'The first and last characters are not the same' # assert if the first letter
# (letter with index 0) is the same as the last letter (letter with index -1)
print('The first and last characters are the same')

# 10. Avand stringul '0123456789'
# ● Afișați doar numerele pare
# ● Afișați doar numerele impare
# (hint: folositi slicing, controlați din pas)
my_string = '0123456789'
print(f'Numere pare: {my_string[::2]}')  # slice variable starting from 0 to 9, jumping 2 paces
print(f'Numere impare: {my_string[1::2]}')  # slice variable starting from 1 to 9, jumping 2 paces

