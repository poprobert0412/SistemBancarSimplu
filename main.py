from ContBancar.cont_bancar import ContBancar
from Banca.banca import Banca

if __name__ == '__main__':
    cont_bancar1 = ContBancar(50, "Pop Robert", 1000)
    cont_bancar2 = ContBancar(51, "Maria Preda", 2000)
    banca1 = Banca("BRD")

    banca1.adauga_cont(cont_bancar1)
    banca1.adauga_cont(cont_bancar2)

    banca1.afiseaza_conturi()

    cont_bancar1.depunere(100)

    cont_bancar1.depunere(500)

    cont_bancar2.depunere(400)

    cont_bancar1.retragere(200)

    cont_bancar2.retragere(1000)

    print(cont_bancar1.sold_disponibil())

    print(cont_bancar2.sold_disponibil())

    banca1.efectueaza_transfer(50, 51, 50)

    print(cont_bancar1.sold_disponibil())

    print(cont_bancar2.sold_disponibil())
