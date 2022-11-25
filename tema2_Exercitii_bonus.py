# Tema 2: Exercitii Bonus

# 11. Joc ghicit zarul
# Caută pe net și vezi cum se generează un număr random
# Ne imaginăm ca dai cu zarul și salvăm acest număr în dice_roll
# Luați un numărul ghicit de la utilizator
# Verificați și afișați dacă utilizatorul a ghicit
# Veți avea 3 opțiuni
# ● Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y
# ● Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y
# ● Ai ghicit. Felicitari! Ai ales x si zarul a fost y
import random  # importam random

dice_roll = random.randint(1, 6)  # get a random number from 1 to 6 from the computer and store it in a variable
number = int(input('Choose a number from 1 to 6'))  # get a number from user and make it int
if number < 1 or number > 6:
    print('Make sure your number is from 1 to 6!')
    number = int(input('Choose a number from 1 to 6'))
    if number < dice_roll:
        print(f'You chose a smaller number. You chose {number} but it was {dice_roll}')
    elif number > dice_roll:
        print(f'You chose a larger number. You chose {number} but it was {dice_roll}')
    else:
        print(f'Congratulations! You chose {number} and the dice rolled {dice_roll}')

