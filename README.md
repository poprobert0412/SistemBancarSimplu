### Structura Fișierelor
```
sistem-bancar-simplu/
│
├── ContBancar/
│   └── cont_bancar.py
│
├── Banca/
│   └── banca.py
│
└── main.py
```

### `cont_bancar.py`
```python
class ContBancar:
    def __init__(self, numar_cont, detinator, sold):
        self.numar_cont = numar_cont
        self.detinator = detinator
        self.sold = sold

    def depunere(self, suma):
        if suma > 0:
            self.sold += suma
            return f"{suma} RON au fost depusi cu succes pe contul {self.numar_cont}. Soldul curent: {self.sold} RON."
        else:
            return "Suma trebuie sa fie pozitiva."

    def retragere(self, suma_retragere):
        if 0 < suma_retragere <= self.sold:
            self.sold -= suma_retragere
            return (f"{suma_retragere} RON au fost retrasi cu succes de pe contul {self.numar_cont}. "
                    f"Sold curent: {self.sold} RON.")
        elif suma_retragere <= 0:
            return "Suma trebuie sa fie pozitiva"
        else:
            return "Fonduri insuficiente"

    def sold_disponibil(self):
        return f"Soldul curent al contului {self.numar_cont} este {self.sold} RON."
```

### `banca.py`
```python
from cont_bancar import ContBancar

class Banca:
    def __init__(self, nume_banca):
        self.nume_banca = nume_banca
        self.conturi = {}

    def adauga_cont(self, cont):
        if isinstance(cont, ContBancar):
            self.conturi[cont.numar_cont] = cont
        else:
            raise TypeError("Parametrul trebuie sa fie un obiect de tip ContBancar")

    def afiseaza_conturi(self):
        for numar_cont, cont in self.conturi.items():
            print(f"Numar cont: {cont.numar_cont} \n"
                  f"Titularul contului: {cont.detinator} \n"
                  f"Soldul contului: {cont.sold} RON")

    def efectueaza_transfer(self, numar_cont_sursa, numar_cont_destinatie, suma):
        if numar_cont_sursa in self.conturi and numar_cont_destinatie in self.conturi:
            cont_sursa = self.conturi[numar_cont_sursa]
            cont_destinatie = self.conturi[numar_cont_destinatie]
            
            rezultat_retragere = cont_sursa.retragere(suma)
            if "RON au fost retrasi cu succes" in rezultat_retragere:
                rezultat_depunere = cont_destinatie.depunere(suma)
                return rezultat_retragere + "\n" + rezultat_depunere
            else:
                return rezultat_retragere
        else:
            return "Conturi invalide"
```

### `main.py`
```python
from ContBancar.cont_bancar import ContBancar
from Banca.banca import Banca

if __name__ == '__main__':
    # Instantiaza 2 obiecte din clasa ContBancar
    cont_bancar1 = ContBancar("50", "Pop Robert", 1000)
    cont_bancar2 = ContBancar("51", "Maria Preda", 2000)
    
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

### README.md
```markdown
# Sistem Bancar Simplu

Acest proiect implementează un sistem bancar simplu în Python, incluzând funcționalități de administrare a conturilor bancare și de realizare a transferurilor între acestea.

## Structura Proiectului

- `ContBancar/cont_bancar.py`: Definirea clasei `ContBancar` cu metode pentru depunere, retragere și verificare sold.
- `Banca/banca.py`: Definirea clasei `Banca` cu metode pentru administrarea conturilor bancare și realizarea transferurilor între conturi.
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
from ContBancar.cont_bancar import ContBancar
from Banca.banca import Banca

if __name__ == '__main__':
    # Instantiaza 2 obiecte din clasa ContBancar
    cont_bancar1 = ContBancar("50", "Pop Robert", 1000)
    cont_bancar2 = ContBancar("51", "Maria Preda", 2000)
    
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
