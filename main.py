from Logic.CRUD import adaugaCarte
from Tests.testAll import runAllTests
from UI.console import runMenu


def main():
    runAllTests()
    lista=[]

    lista = adaugaCarte("1", "Test1", "Actiune", 10, "silver",lista)
    lista = adaugaCarte("2", "Test2", "Comedie", 10, "gold",lista)
    runMenu(lista)


main()