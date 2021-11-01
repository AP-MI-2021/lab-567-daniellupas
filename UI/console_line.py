from Domain.carte import toString, creeazaCarte
from Logic.CRUD import stergeCarte, modificaCarte, adaugaCarte


def showAll(lista):
    for carte in lista:
        print(toString(carte))


def meniu_help_tool():
    print("Add , id, titlu , gen ,pret , tip reducere")
    print("Delete, id")
    print("Update, id , titlu , gen , pret , tip reducere")
    print("ShowAll")
    print("Break")



def cmdMeniu(lista):

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
                    comenzi=elemente.split(',')
                    if comenzi[0]=='Add':
                        try:
                            lista=adaugaCarte(comenzi[1],comenzi[2],comenzi[3],comenzi[4],comenzi[5],lista)
                        except ValueError as ve:
                            print("Eroare : {}".format(ve))
                    elif comenzi[0]=='Delete':
                        try:
                            lista=stergeCarte(comenzi[1],lista)
                        except ValueError as ve1:
                            print("Eroare : {}".format(ve1))
                    elif comenzi[0] == "Modifica":
                        lista= modificaCarte(comenzi[1],comenzi[2],comenzi[3],comenzi[4],comenzi[5],lista)
                    elif comenzi[0]=='ShowAll':
                        showAll(lista)
                    else:
                        print("Optiune Gresita. Tasteaza Help si urmareste pasii explicati")


