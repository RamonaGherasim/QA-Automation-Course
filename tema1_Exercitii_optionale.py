# Exercitii optionale
# Tema 1 - Setup, Variabile, Tipuri de date

# 1. Exercițiu:
# - citește de la tastatură un string de dimensiune impară;
# - afișează caracterul din mijloc.
userString = input('Type a string here')  # we receive data from the keyboard
assert len(userString) % 2 != 0  # we assert if this is odd or even. Odd means that % 2 is not 0.
middle = len(userString) // 2  # we find the middle of the string by using the floor operation.
print(userString[middle])  # print the middle character

# # 2. Folosind assert, verifică dacă un string este palindrom.
# # Palindrome = the reverse of that string is the same as the original string.
myString = input('Type a word here')
assert myString == myString[::-1], 'Your string is not a palindrome!'  # [::-1] reverses the string. It starts from the
                                                                      # end going to the start taking each element.
print('Your string is a palindrome!')

# 3. Folosind o singură linie de cod :
# - citește un string de la tastatură (ex: 'alabala portocala');
# - salvează fiecare cuvânt într-o variabilă;
# - printează ambele variabile pentru verificare.
aString = input('Type a string here')  # take data from the keyboard which is a str by default
firstWord = aString.split()[0]  # save the first word into a var
secondWord = aString.split()[1]  # save the second word into a var
print(firstWord, secondWord)  # printing both variables to check
# As a one line code:
print(input('Type a string here').split()[0:2])  # as above, but in one line of code

# 4. Exercițiu:
# - citește un string de la tastatură (ex: alabala portocala);
# - salvează primul caracter într-o variabilă - indiferent care este el, încearcă
# cu 2 stringuri diferite;
# - capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul
# caracter => alAbAlA portocAla.
s = input('Type a string here')  # we get the data from the keyboard and store it in variable s
firstCharacter = s[0]  # we get the fist character of the string and store it in a variable
s = s[0] + s[1:-1].replace(firstCharacter, firstCharacter.upper()) + s[-1] # overwrite the s variable, keeping the first
# character as it is, replace that first character with uppercase everywhere else except the last one, adding the last
# character as it was originally written. Concatenate the string back with the new changes implemented
print(s)  # print the string in its final form

# 5. Exercițiu:
# - citește un user de la tastatură;
# - citește o parolă;
# - afișează: 'Parola pt user x este ***** și are x caractere';
# - ***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie să
# afișeze corect.
# eg: parola abc => ***
user = input('Type you username here')  # get the username info from the keyboard and save it into a variable
password = input('Type your password here')  # get the password info from the keyboard and save it into a variable
characters = int(len(password))  # find out the number of characters for the password
password = '*' * characters  # replace each character by *
print(f'The password for user {user} is {password} and has {characters} characters')  # print the desired string















