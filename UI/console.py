from Domain import carte
from Domain.carte import toString, getPret
from Logic.CRUD import adaugaCarte, stergeCarte, modificaCarte
from Logic.functionalitati import AplicareDiscount


def printMenu():
    print("1. Adaugare carte")
    print("2. Stergere carte")
    print("3. Modificare carte")
    print("4.Aplicare Discount")
    print("a. Afisare carti")
    print("x. Exit")


def uiAdaugaCarte(lista):
    id = input("Dati Id-ul")
    titlu = input("Dati titlul")
    gen = input("Dati genul")
    pret = float(input("Dati pretul: "))
    tip_reducere = input("Dati tipul reducerii")

    return adaugaCarte(id, titlu, gen, pret, tip_reducere, lista)


def uiStergeCarte(lista):
    id = input("dati id ul")
    return stergeCarte(id, lista)


def uiModificaCarte(lista):
    id = input("Dati noul Id-ul")
    titlu = input("Dati noul titlul")
    gen = input("Dati noul genul")
    pret = float(input("Dati noul pretul: "))
    tip_reducere = input("Dati  noul tip de  reducere")

    return modificaCarte(id, titlu, gen, pret, tip_reducere, lista)





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
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("optiune gresita")
