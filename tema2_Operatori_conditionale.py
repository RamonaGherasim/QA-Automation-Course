# Tema 2: Operatori, conditionale

# 1. Explică cu cuvintele tale în cadrul unui comentariu cum funcționează un if else.
# Se testeaza conditia if. Daca aceasta este adevarata, se executa codul din cadrul acesteia. In caz contrar, daca
#conditia este falsa, se ruleaza codul din cadrul conditiei urmatoare (care aici este else)

# 2. Verifică și afișează dacă x este număr natural sau nu.
# nr natural = orice nr de la 1 la infinit, pozitiv si intreg!
x = int(input('number'))  # take data from the keyboard and store it in a variable, making sure it is an integer
if x > 0:  # defining the if condition
    print(f'{x} it\'s a natural number')

# 3. Verifică și afișează dacă x este număr pozitiv, negativ sau neutru.
x = int(input('number x'))
if x > 0:
    print(f'{x} is a positive number')
elif x < 0:
    print(f'{x} is a negative number')
else:
    print(f'{x} is a neutral number')  # this is the default if the if elif conditions are False

# 4. Verifică și afișează dacă x este între -2 și 13.
x = int(input('Add a number between -2 and 13'))
if -2 < x < 13:
    print(f'Correct! -2 < {x} < 13 ')

# 5. Verifică și afișează dacă diferența dintre x și y este mai mică de 5.
x = int(input('number x'))
y = int(input('number y'))
if (x - y) < 5:
    print(f'Correct! {x-y} < 5')

# 6. Verifică dacă x NU este între 5 și 27 - a se folosi ‘not’.
x = int(input('Add a number between 5 and 27'))
if not(5 < x < 27):  # not is checking for the opposite of the code in the parenthesis
    print('Wrong number, try again!')

# 7. x și y (int)
# Verifică și afișează dacă sunt egale, dacă nu afișează care din ele este mai mare.
x = int(input('number x'))
y = int(input('number y'))
if x == y:
    print(f'{x} is equal to {y}')
elif x > y:
    print(f'{x} is bigger than {y}')
else:
    print(f'{x} is smaller than {y}')

# 8. X, y, z - laturile unui triunghi.
# Afișează dacă triunghiul este isoscel, echilateral sau oarecare.
# isosceles = 2 equal sides
# equilateral = all 3 sides are equal
# scalene = all sides are different
x = int(input('side x'))
y = int(input('side y'))
z = int(input('side z'))
if x == y or x == z or y == z:
    print('Your triangle is isosceles')
elif x == y == z:
    print('Your triangle is equilateral')
else:
    print('Your triangle is a scalene triangle')

# 9. Citește o literă de la tastatură.
# Verifică și afișează dacă este vocală sau nu
letter = input('Type a random letter')
vowels = ['a', 'e', 'i', 'o', 'u']
if letter in vowels:
    print(f'{letter} is a vowel')
else:
    print(f'{letter} is a consonant')

# 10. Transformă și printează notele din sistem românesc în >
# Peste 9 => A
# Peste 8 => B
# Peste 7 => C
# Peste 6 => D
# Peste 4 => E
# 4 sau sub => F
grade = float(input('Choose your grade'))
if grade > 10:
    print('Please choose a grade between 0 and 10')
elif 9 < grade < 10:
    print('A')
elif grade > 8:
    print('B')
elif grade > 7:
    print('C')
elif grade > 6:
    print('D')
elif grade > 4:
    print('E')
elif 4 > grade > 0:
    print('F')
else:
    print('Please choose a grade between 0 and 10')