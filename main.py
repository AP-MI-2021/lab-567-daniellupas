from Logic.CRUD import adaugaCarte
from Tests.testAll import runAllTests
from UI.console import runMenu


def main():
    runAllTests()
    lista=[]

    lista = adaugaCarte("1", "Test1", "Actiune", 1120, "silver",lista)
    lista = adaugaCarte("2", "Test2", "Comedie", 12310, "gold",lista)
    lista = adaugaCarte("3", "Test2", "Comedie", 10123, "gold", lista)
    lista = adaugaCarte("4", "Test2", "Comedie", 102, "gold", lista)
    lista = adaugaCarte("6", "Test2", "Comedie", 1023, "gold", lista)
    lista = adaugaCarte("7", "Test2", "Comedie", 105, "gold", lista)
    lista = adaugaCarte("8", "Test2", "Comedie", 11230, "gold", lista)
    runMenu(lista)


main()