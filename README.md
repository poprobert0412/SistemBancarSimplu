# Sistem Bancar Simplu

Acest proiect implementează un sistem bancar simplu în Python, incluzând funcționalități de administrare a conturilor bancare și de realizare a transferurilor între acestea.

## Structura Proiectului

- `cont_bancar.py`: Definirea clasei `ContBancar` cu metode pentru depunere, retragere și verificare sold.
- `banca.py`: Definirea clasei `Banca` cu metode pentru administrarea conturilor bancare și realizarea transferurilor între conturi.
- `main.py`: Exemplu de utilizare a aplicației.

## Clasa `ContBancar`

### Atribute:
- `numar_cont`: String - Numărul contului.
- `detinator`: String - Numele titularului contului.
- `sold`: Float - Soldul curent al contului.

### Metode:
- `depunere(suma)`: Depune o sumă în cont. Returnează un mesaj de confirmare.
- `retragere(suma_retragere)`: Retrage o sumă din cont. Returnează un mesaj de confirmare sau de eroare dacă fondurile sunt insuficiente.
- `sold_disponibil()`: Returnează soldul curent al contului.

## Clasa `Banca`

### Atribute:
- `nume_banca`: String - Numele băncii.
- `conturi`: Dict - Dicționar care conține conturile bancare, cu numărul contului ca și cheie și obiectul `ContBancar` ca valoare.

### Metode:
- `adauga_cont(cont)`: Adaugă un cont bancar în bancă.
- `afiseaza_conturi()`: Afișează detaliile conturilor din bancă.
- `efectueaza_transfer(numar_cont_sursa, numar_cont_destinatie, suma)`: Efectuează un transfer între două conturi din bancă. Returnează mesajul rezultat al operațiunii.

## Exemplu de Utilizare

### `main.py`

```python
from cont_bancar import ContBancar
from banca import Banca

if __name__ == '__main__':
    # Instantiaza 2 obiecte din clasa ContBancar
    cont_bancar1 = ContBancar("50", "Pop Robert", 50000)
    cont_bancar2 = ContBancar("51", "Ionescu Maria", 30000)
    
    # Instantiaza 1 obiect din clasa Banca
    banca1 = Banca("BRD")

    # Adauga cele doua conturi bancare in banca
    banca1.adauga_cont(cont_bancar1)
    banca1.adauga_cont(cont_bancar2)
    
    # Afiseaza conturile
    banca1.afiseaza_conturi()
    
    # Depune suma de 100 lei in cont 1
    print(cont_bancar1.depunere(100))
    
    # Depune suma de 500 lei in cont 1
    print(cont_bancar1.depunere(500))
    
    # Depune suma de 400 lei in cont 2
    print(cont_bancar2.depunere(400))
    
    # Retrage suma de 200 lei din cont 1
    print(cont_bancar1.retragere(200))
    
    # Retrage suma de 1000 lei din cont 2
    print(cont_bancar2.retragere(1000))
    
    # Afiseaza soldul disponibil din contul 1
    print(cont_bancar1.sold_disponibil())
    
    # Afiseaza soldul disponibil din contul 2
    print(cont_bancar2.sold_disponibil())
    
    # Efectueaza un transfer din contul 1 in contul 2 de 50 lei
    print(banca1.efectueaza_transfer("50", "51", 50))
    
    # Afiseaza soldul disponibil dupa transfer din fiecare cont
    print(cont_bancar1.sold_disponibil())
    print(cont_bancar2.sold_disponibil())
```

## Instalare și Rulare

1. Clonează acest repository:
    ```sh
    git clone https://github.com/username/sistem-bancar-simplu.git
    ```
2. Navighează în directorul proiectului:
    ```sh
    cd sistem-bancar-simplu
    ```
3. Rulează scriptul principal:
    ```sh
    python main.py
    ```

## Contribuții

Contribuțiile sunt binevenite! Te rog să deschizi un issue pentru a discuta despre modificările pe care vrei să le faci. 
