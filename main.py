from Logic.CRUD import adaugaCarte
from Tests.testAll import runAllTests
from UI.console import runMenu
from UI.console_line import cmdMeniu


def main():
    runAllTests()
    lista = []

    lista = adaugaCarte("1", "Test1", "Actiune", 1120, "silver", lista)
    lista = adaugaCarte("12", "Test2", "Actiune", 1120, "silver", lista)
    lista = adaugaCarte("23", "Test3", "Dra", 1120, "silver", lista)
    lista = adaugaCarte("2", "Test4", "Actiune", 12310, "gold", lista)
    lista = adaugaCarte("3", "Test5", "Comedie", 10123, "gold", lista)
    lista = adaugaCarte("4", "Test6", "Comedie", 102, "gold", lista)
    lista = adaugaCarte("6", "Test7", "Actiune", 1023, "gold", lista)
    lista = adaugaCarte("7", "Test8", "Comedie", 105, "gold", lista)
    lista = adaugaCarte("8", "Test9", "Actiune", 11230, "gold", lista)
    print("1.Meniu vechi")
    print("2.Meniu tip cmd")

    optiune = input("Alege tipul de meniu pe care doresti sa il utilizezi: ")
    if optiune == "1":
        runMenu(lista)
    elif optiune == "2":
        cmdMeniu(lista)
    else:
        print("optiune gresita")


main()
