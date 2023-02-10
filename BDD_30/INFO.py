"""
    BACKGROUND = O modalitate prin care putem sa dam un context general testelor noastre
    Functioneaza in pereche cu Given
    Punem in Background orice element de context care este valabil pentru toate
    scenariile din feature file.
    ============================================================================================================

    TAGs = daca vrem sa separam testele pe care le rulam si sa le executam individual sau grupate.
            atunci folosim conceptul de tag-uri
    => tag-urile incep cu @ si sunt urmate de free text (este recomandat ca acesta sa fie sugestiv)
    => un scenariu poate fi identificat prin mai multe tag-uri
    => in momentul rularii scriem astfel, atunci cand folosim si tag-uri:
      e.g. "behave -f html -o behave-report.html --tags=T1"
      --> Acesta va rula primul scenariu
      e.g. "behave -f html -o behave-report.html --tags=functional"
      --> Va rula al doilea scenariu
      e.g. "behave -f html -o behave-report.html --tags=BDD"
      --> Va rula ambele scenarii
    ============================================================================================================

    SCENARIO OUTLINE = O modalitate prin care putem sa rulam acelasi test de mai multe ori avand
                       input diferit
    => testul se va rula cate o data pentru fiecare input prezent in examples

    Sesiunile de scenario outline examples se pot si ele grupa la randul lor folosind tag-uri
    La fiecare examples se poate adauga cate un tag
    """