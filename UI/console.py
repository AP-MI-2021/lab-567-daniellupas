from Domain import carte
from Domain.carte import toString, getPret, get_str
from Logic.CRUD import adaugaCarte, stergeCarte, modificaCarte
from Logic.functionalitati import AplicareDiscount, ModificareGen, PretMinimPeGen


def printMenu():
    print("1. Adaugare carte")
    print("2. Stergere carte")
    print("3. Modificare carte")
    print("4. Aplicare Discount")
    print("5. Modificare genul cartii")
    print("6. Ordonarea pretului dupa gen")
    print("a. Afisare carti")
    print("x. Exit")


def uiAdaugaCarte(lista):
    try:
        id = input("Dati Id-ul")
        titlu = input("Dati titlul")
        gen = input("Dati genul")
        pret = float(input("Dati pretul: "))
        tip_reducere = input("Dati tipul reducerii")

        return adaugaCarte(id, titlu, gen, pret, tip_reducere, lista)
    except ValueError as ve:
        print("Eroare:  {} ".format(ve))
        return lista


def uiStergeCarte(lista):
    try:
        id = input("dati id ul")
        return stergeCarte(id, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))


def uiModificaCarte(lista):
    try:
        id = input("Dati noul Id-ul")
        titlu = input("Dati noul titlul")
        gen = input("Dati noul genul")
        pret = float(input("Dati noul pretul: "))
        tip_reducere = input("Dati  noul tip de  reducere")

        return modificaCarte(id, titlu, gen, pret, tip_reducere, lista)
    except ValueError as ve:
        print("Eroare : {} ".format(ve))


def ModificaGen(lista):
    titlu = input("Introdu titlul cartii la care doresti sa ii schimbi titlul: ")
    gen = input("Introduceti noul gen: ")

    return ModificareGen(lista, titlu , gen)

def uiOrdonareDupaPret(lista):
    rezultat = PretMinimPeGen(lista)

    for gen in rezultat:
        print(f'{gen}: {get_str(rezultat[gen])}')


def showAll(lista):
    for carte in lista:
        print(toString(carte))


def runMenu(lista):
    while True:
        printMenu()
        optiune = input("Dati optiune: ")

        if optiune == "1":
            lista = uiAdaugaCarte(lista)
        elif optiune == "2":
            lista = uiStergeCarte(lista)
        elif optiune == "3":
            lista = uiModificaCarte(lista)
        elif optiune == "4":
            lista = AplicareDiscount(lista)
        elif optiune == "5":
            lista = ModificaGen(lista)
        elif optiune == "6":
            lista = uiOrdonareDupaPret(lista)
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("optiune gresita")
