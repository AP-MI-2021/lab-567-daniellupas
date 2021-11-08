from Domain import carte
from Domain.carte import toString, getPret, get_str
from Logic.CRUD import adaugaCarte, stergeCarte, modificaCarte
from Logic.functionalitati import AplicareDiscount, ModificareGen, PretMinimPeGen, OrdonareDupaPret, \
    DeterminareCartiCuTitluriDistincte


def printMenu():
    print("1. Adaugare carte")
    print("2. Stergere carte")
    print("3. Modificare carte")
    print("4. Aplicare Discount")
    print("5. Modificare genul cartii")
    print("6. Ordonarea pretului dupa gen")
    print("7. Ordonarea vanzarilor crescator dupa pret")
    print("8. Afisarea numarului de carti de accelasi gen")
    print("a. Afisare carti")
    print("u. Undo")
    print("r. Redo")
    print("x. Exit")


def uiAdaugaCarte(lista, undoList, redoList):
    try:
        id = input("Dati Id-ul")
        titlu = input("Dati titlul")
        gen = input("Dati genul")
        pret = float(input("Dati pretul: "))
        tip_reducere = input("Dati tipul reducerii")

        rezultat = adaugaCarte(id, titlu, gen, pret, tip_reducere, lista)
        redoList.clear()
        undoList.append(lista)
        return rezultat
    except ValueError as ve:
        print("Eroare:  {} ".format(ve))
        return lista


def uiStergeCarte(lista, undoList, redoList):
    try:
        id = input("dati id ul")
        rezultat = stergeCarte(id, lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))


def uiModificaCarte(lista, undoList, redoList):
    try:
        id = input("Dati noul Id-ul")
        titlu = input("Dati noul titlul")
        gen = input("Dati noul genul")
        pret = float(input("Dati noul pretul: "))
        tip_reducere = input("Dati  noul tip de  reducere")

        rezultat = modificaCarte(id, titlu, gen, pret, tip_reducere, lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare : {} ".format(ve))


def ModificaGen(lista):
    titlu = input("Introdu titlul cartii la care doresti sa ii schimbi titlul: ")
    gen = input("Introduceti noul gen: ")

    return ModificareGen(lista, titlu, gen)


def uiOrdonareDupaPret(lista):
    rezultat = PretMinimPeGen(lista)

    for gen in rezultat:
        print(f'{gen}: {get_str(rezultat[gen])}')


def uiOrdonarePretCrescator(lista):
    showAll(OrdonareDupaPret(lista))


def uiAfisareDupaGenuri(lista):
    try:
        rezultat = DeterminareCartiCuTitluriDistincte(lista)
        for gen in rezultat:
            print("Genul : {} are {} titluri distincte".format(gen,rezultat[gen]))
    except ValueError as ve:
        print("Eroare: {}".format(ve))

    return lista


def showAll(lista):
    for carte in lista:
        print(toString(carte))


def runMenu(lista):

    undoList=[]
    redoList=[]

    while True:
        printMenu()
        optiune = input("Dati optiune: ")

        if optiune == "1":
            lista = uiAdaugaCarte(lista, undoList, redoList)
        elif optiune == "2":
            lista = uiStergeCarte(lista, undoList, redoList)
        elif optiune == "3":
            lista = uiModificaCarte(lista, undoList, redoList)
        elif optiune == "4":
            lista = AplicareDiscount(lista)
        elif optiune == "5":
            lista = ModificaGen(lista)
        elif optiune == "6":
            uiOrdonareDupaPret(lista)
        elif optiune == "7":
            uiOrdonarePretCrescator(lista)
        elif optiune == "8":
            uiAfisareDupaGenuri(lista)
        elif optiune == "a":
            showAll(lista)
        elif optiune == "u":
            if len(undoList) >0:
                redoList.append(lista)
                lista = undoList.pop()
            else:
                print("Nu se poate efectua operatia ")
        elif optiune == "r":
            if len(redoList)>0:
                undoList.append(lista)
                lista = redoList.pop()
            else:
                print("Nu se poate aplica asa ceva")


        elif optiune == "x":
            break
        else:
            print("optiune gresita")
