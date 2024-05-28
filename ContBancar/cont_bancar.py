"""Clasa ContBancar() cu metodele de depunere, retragere si sold disponibil"""

#definim clasa ContBancar

class ContBancar:
    #Definim un constructor care are 3 atribute

    def __init__(self, numar_cont, detinator, sold):
        self.numar_cont = numar_cont
        self.detinator = detinator
        self.sold = sold

    #Definim metoda depunere care o sa ia un parametru si la final o sa returneze suma care a fost depusa in cont

    def depunere(self, suma):
        if suma > 0:
            self.sold += suma
            return f"{suma} RON au fost depusi cu succes pe contul {self.numar_cont}. Soldul curent: {self.sold} RON."
        else:
            return "Suma trebuie sa fie pozitiva."

    #Definim metoda retragere care o sa ia un parametru si o sa afiseze cati bani sunt retrasi sau daca suma trebuie sa
    #fie pozitiva sau daca sunt fonduri insuficiente

    def retragere(self, suma_retragere):
        if 0 < suma_retragere <= self.sold:
            self.sold -= suma_retragere
            return (f"{suma_retragere} RON au fost retrasi cu succes de pe contul {self.numar_cont}. "
                    f"Sold curent: {self.sold} RON.")
        elif suma_retragere <= 0:
            return "Suma trebuie sa fie pozitiva"
        else:
            return "Fonduri insuficiente"

    #Definim metoda sold_disponibil care afiseaza sold ul contului

    def sold_disponibil(self):
        return f"Soldul curent al contului {self.numar_cont} este {self.sold} RON."
