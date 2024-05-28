"""Definim clasa Banca() care are ca si metode: adauga_cont, afiseaza_conturi"""
from ContBancar.cont_bancar import ContBancar

class Banca():
    #am definit clasa Banca cu un constructor care are 2 atribute
    def __init__(self, nume_banca):
        self.nume_banca = nume_banca
        self.conturi = {}

    #Definim metoda adauga_cont care primeste un parametru din clasa cont bancar

    def adauga_cont(self, cont):
        if isinstance(cont, ContBancar):
            self.conturi[cont.numar_cont] = cont
        else:
            raise TypeError("Parametrul trebuie sa fie un obiect de tip ContBancar")

    def afiseaza_conturi(self):
        for numar_cont, cont in self.conturi.items():
            print(f"Numar cont: {cont.numar_cont} \n"
                  f"Titularul contului: {cont.detinator} \n"
                  f"Soldul contului : {cont.sold}")

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
