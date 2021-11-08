from Domain.carte import toString
from Logic.CRUD import stergeCarte, modificaCarte, adaugaCarte
from Logic.functionalitati import *
from UI.console import uiOrdonareDupaPret, uiAfisareDupaGenuri


def showAll(lista):
    for carte in lista:
        print(toString(carte))


def meniu_help_tool():
    print("Add , id, titlu , gen ,pret , tip reducere")
    print("Delete, id")
    print("Update, id , titlu , gen , pret , tip reducere")
    print("Discount")
    print("Modificare, titlu, gen")
    print("Ordonare")
    print("Afisare_g")
    print("undo")
    print("redo")
    print("ShowAll")
    print("Break")


def cmdMeniu(lista):
    undoList = []
    redoList = []

    while True:
        option = input()
        if option == 'Help':
            meniu_help_tool()
        else:
            words = option.split(";")
            if words[0] == 'Stop':
                break
            else:
                for elemente in words:
                    comenzi = elemente.split(',')
                    if comenzi[0] == 'Add':
                        try:
                            redoList.clear()
                            undoList.append(lista)
                            lista = adaugaCarte(comenzi[1], comenzi[2], comenzi[3], comenzi[4], comenzi[5], lista)
                        except ValueError as ve:
                            print("Eroare : {}".format(ve))
                    elif comenzi[0] == 'Delete':
                        try:
                            undoList.append(lista)
                            redoList.clear()
                            lista = stergeCarte(comenzi[1], lista)
                        except ValueError as ve1:
                            print("Eroare : {}".format(ve1))
                    elif comenzi[0] == "Modifica":
                        undoList.append(lista)
                        redoList.clear()
                        lista = modificaCarte(comenzi[1], comenzi[2], comenzi[3], comenzi[4], comenzi[5], lista)
                    elif comenzi[0] == 'ShowAll':
                        showAll(lista)

                    elif comenzi[0] == "Discount":
                        undoList.append(lista)
                        redoList.clear()
                        lista = AplicareDiscount(lista)
                    elif comenzi[0] == "Modificare":
                        undoList.append(lista)
                        redoList.clear()
                        lista = ModificareGen(lista, comenzi[1], comenzi[2])
                    elif comenzi[0] == "Ordonare":
                        undoList.append(lista)
                        redoList.clear()
                        uiOrdonareDupaPret(lista)
                    elif comenzi[0] == "Afisare_g":
                        undoList.append(lista)
                        redoList.clear()
                        uiAfisareDupaGenuri(lista)
                    elif comenzi[0] == 'undo':
                        if len(undoList) > 0:
                            lista, undoList, redoList = undo(lista, undoList, redoList)
                    elif comenzi[0] == 'redo':
                        if len(redoList) > 0:
                            lista, undolist, redolist = redo(lista, undoList, redoList)
                    else:
                        print("Optiune Gresita. Tasteaza Help si urmareste pasii explicati")
