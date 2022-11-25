# Tema 3: Exercitii optionale

'''
1. Ne imaginăm o echipă de fotbal pt teren sintetic.
3 Schimbări maxime admise:

● Declară o Listă cu 5 jucători
● Schimbari_efectuate = te joci tu cu valori diferite
● Schimbari_max = 3
Dacă Jucătorul x e în teren și mai avem schimbări la dispoziție
- Efectuează schimbarea

- Șterge jucătorul scos din listă
- Adaugă jucătorul intrat
- Afișaza a intra x, a ieșit y, mai ai z schimbări
Dacă jucătorul nu e în teren:
- Afișază ‘ nu se poate efectua schimbarea deoarece jucătorul x nu e în
teren’
- Afișază ‘mai ai z schimbări’
Testează codul cu diferite valori

Google search hint
“how to check if item îs în list python”
'''

jucatori = ["Roro", "Alex", "Mimi"]
schimbari_efectuate = 3
schimbari_max = 3
jucator_scos = "Alex"
jucator_intrat = "Dumi"

# Scoate-l pe "Alex" si adauga-l pe "Dumi"
if schimbari_efectuate < schimbari_max:
    if jucator_scos in jucatori:
        schimbari_efectuate += 1
        jucatori.insert(jucatori.index(jucator_scos), jucator_intrat)
        jucatori.remove(jucator_scos)
        print(f"A intrat {jucator_intrat}, a iesit {jucator_scos}, mai ai {schimbari_max - schimbari_efectuate} schimbari")
    else:
        print(f"Nu se poate efectua schimbarea deoarece jucatorul {jucator_scos} nu e in teren")
        print(f"Mai ai {schimbari_max - schimbari_efectuate} schimbari")
else:
    print("Nu mai ai schimbari disponibile!")

# SAU raspuns de la tutore
SCHIMBARI_MAXIME = 3
schimbari_efectuate = 2
# calculam si initializam schimbari ramase
schimbari_ramase = SCHIMBARI_MAXIME - schimbari_efectuate
lista_jucatori_teren = ['j1', 'j2', 'j3', 'j4', 'j5']
lista_jucatori_rezerva = ['j6','j7','j8','j9','j10']
lista_jucatori_scosi = []
jucator_in = 'j6'
jucator_out = 'j1'

# daca jucatorul e in tere SI daca mai am schimbari
if jucator_out in lista_jucatori_teren and schimbari_ramase > 0:
    if jucator_in in lista_jucatori_rezerva and jucator_in not in lista_jucatori_teren: # eliminam cazul cand jucatorul este deja in teren
        lista_jucatori_teren.remove(jucator_out)  # scoatem jucatorul
        lista_jucatori_scosi.append(jucator_out)
        lista_jucatori_teren.add(jucator_in)  # adaugam jucatorul nou
        lista_jucatori_rezerva.remove(jucator_out)
        schimbari_ramase = schimbari_ramase - 1  # contorizam schimbarea
        print(f'Schimbare efectuata cu succes!')
        print(f'A intrat {jucator_in}, a iesit {jucator_out}, mai aveti {schimbari_ramase} schimbari')
else:
    if schimbari_ramase <= 0:
        print('Nu mai ai schimbari')
    else:
        print(f'Nu se poate efectua schimbarea deoarece jucatorul {jucator_out} nu e in teren')
print(f'Actuala echipa este {echipa}')
print(f"Jucatorii care au fost scosi sunt: {lista_jucatori_scosi}")

