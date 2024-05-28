"""
EXERCITII WORKSHOP (Sesiunea 12)
"""

"""
MINI PROJECT 2 – Sistem bancar simplu in Python
 

Proiectele sunt foarte importante in dezvoltarea ta si cimentarea cunostiintelor acumulate
de-a lungul sesiunilor de curs.
Acestea sunt foarte apreciate si de asemenea necesare pentru angajare.

In dezvoltarea mini-proiectului “Sistem bancar simplu in Python” vei exersa cunostiintele acumulate la curs, precum:
-	Afisarea mesajelor in consola
-	Formatarea string-urilor folosind f-strings
-	Utilizarea operatorilor
-	Utilizarea if-urilor, ciclurilor repetitive
-	Variabile, strucuri de date
-	Utilizarea notiunilor de OOP (clase, obiecte, atribute, metode)
"""


"""
1.	Defineste clasa ContBancar:
- Aceasta va avea in constructor, trei atribute: numar_cont, detinator, sold.
- Toti cei trei parametri vor primi o valoarea in momentul crearii obiectelor din clasa ContBancar.
Metode:
- metoda numita depunere:
    - Va lua un parametru, si anume suma care se doreste a fi depusa in cont;
    - Verificam daca suma care se doreste a fi depusa in cont este mai mare decat zero;
    - Daca da, o adaugam in atributul sold (crestem valoarea atributului sold cu suma aferenta) si returnam mesajul 
“{suma} RON au fost depusi cu succes pe contul {numar_cont}. Soldul curent: {sold} RON.” 
NOTA: Suma, numar_cont si sold, se vor insera dinamic in string-ul returnat.
    - Daca nu, returnam mesajul “Suma trebuie sa fie pozitiva.”

- metoda numita retragere:
    - Va lua un parametru, si anume suma care se doreste a fi retrasa din cont;
    - Daca suma luata ca si parametru este mai mare decat zero si daca este mai mica sau egala
decat sold-ul curent, se va scadea suma din sold si se va returna mesajul 
“{suma} RON au fost retrasi cu succes de pe contul {numar_cont}. Sold curent: {sold} RON.” 
NOTA: Suma, numar_cont si sold se vor insera dinamic in string-ul returnat.
    - Daca suma e mai mica sau egala decat zero, returnam mesajul
 “Suma trebuie sa fie pozitiva”.
    - Daca suma e mai mare decat soldul curent, returnam mesajul “Fonduri insuficiente”.

- metoda sold_disponibil:
    - returneaza mesajul “Soldul curent al contului {numar_cont} este {sold} RON.” 
NOTA: Soldul si numar_cont se vor insera dinamic in string-ul returnat.
"""


"""
2.	Defineste clasa Banca:
- Aceasta va avea in constructor, doua atribute: nume_banca si conturi.
- nume_banca va primi o valoarea in momentul crearii obiectelor din clasa Banca.
- conturi va fi un dictionar gol.

Metode:
- metoda adauga_cont:
    - primeste un parametru numit cont, care va fi un obiect din clasa Cont Bancar.
    - Adauga contul luat ca parametru in atributul conturi al clasei Banca, adaugand
o noua pereche cheie valoare in dictionar, cu cheia fiind atributul numar_cont al obiectului
cont si valoarea obiectul respectiv.
- metoda afiseaza_conturi:
    - itereaza prin conturile salvate in atributul conturi si afiseaza un mesaj cu detaliile despre fiecare.
- metoda efectueaza_transfer:
    - ia 3 parametri: numar_cont_sursa, numar_cont_destinatie, suma
    - se verifica daca numar_cont_sursa si numar_cont_destinatie apartin de conturile bancii curente. 
    - daca da, se apeleaza metoda retragere pe obiectul cont_sursa si metoda reducere pe contul destinatie
si se returneaza rezultatele acestora.
    - daca nu, se returneaza mesajul “Conturi invalide”
"""


"""
3.	Folosire aplicatie:
-	Instantiaza 2 obiecte din clasa ContBancar
-	Instantiaza 1 obiect din clasa Banca
-	Adauga cele doua conturi bancare in banca.
-	Afiseaza conturile.
-	Depune suma de 100 lei in cont 1.
-	Depunde suma de 500 lei in cont 1.
-	Depune suma de 400 lei in cont 2.
-	Retrage suma de 200 lei din cont 1.
-	Retrage suma de 1000 lei in cont 2.
-	Afiseaza soldul disponibil din contul 1.
-	Afiseaza soldul disponibil din contul 2.
-	Efectueaza un transfer din contul 1 in contul 2 de 50 lei.
-	Afiseaza soldul disponibil dupa transfer din fiecare cont.
"""
