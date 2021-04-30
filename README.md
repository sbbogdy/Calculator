# Descriere
Un calculator pentru calcule usoare matematice, ideal pentru exercitii simple si scurte.

# GUI
Aplicatia a fost scrisa in Python, folosindu-ma de Tkinter pentru GUI.
M-am folosit de aplicatia PAGE pentru crearea schitei pentru GUI, pe care l-am modificat eu ulterior, luand decizia de a-l lasa sa arate mai vechi, reflectand simplicitatea, dar si limitele sale proiectului.

# Logica
Programul este bazat pe rescrierea calculelor scrise in interfata in forma lor postfix, astfel calculatorului fiindu-i mult mai usor sa faca in ordine corect matematic o multitudine de calcule.
Pentru a realiza asta, i-am oferit fiecarei operatii, o valoare in functie de ordinea in care aceasta are loc. O valoare mai mare inseamna o operatie de prioritate mai mare. Astfel, ridicarea la putere are valoare mai mare ca inmultirea, care are mai mare decat adunarea. Fiecare operatie prezenta intr-o sau mai multe paranteze isi are valoare crescuta in functie de numarul de paranteze in care este operatia.

# Pachete folosite
In realizarea proiectului, am folosit pachete:\
Pillow\
Pillow-PIL\
pip\
setuptools\
ttkthemes

# Limitari
Calculatorul are implementate numai operatile de baza: adunare, scadere, inmultire, impartire, ridicare la putere. Asta inseamna ca nu este de ajutor cand trebuie calculat un radical sau o functie trigonometrica. Pe langa asta, ridicare la putere este limitata la numere intregi. Daca un numar trebuie ridicat la un numar rational, rezultatul va fi o eroare.\
Alte limita au legatura cu scrisul si lungimea calculului. Codul necesita un calcul scris corect, fara parateze lasate deschise sau semne dupa semne, chiar daca ar fi un minus indicand un numar negativ, desi intele un numar langa o paranteza deschisa ca inmultire si n-are nevoie de 0 cat sa stie ca .5 e 0.5.



