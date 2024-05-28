from ContBancar.cont_bancar import ContBancar

if __name__ == '__main__':
    cont_bancar = ContBancar(50, "Pop Robert", 50000)
    #TESTARE obiecte din clasa ContBancar()
    print(cont_bancar.depunere(-100))
    print(cont_bancar.depunere(0))
    print(cont_bancar.depunere(5000))

    print(cont_bancar.retragere(10000000))
    print(cont_bancar.retragere(0))
    print(cont_bancar.retragere(-1000))
    print(cont_bancar.retragere(10000))

    print(cont_bancar.sold_disponibil())

    #Testare cu succes