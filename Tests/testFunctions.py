from Domain.carte import getPret, getGen_carte, getid
from Logic.CRUD import adaugaCarte
from Logic.functionalitati import AplicareDiscount, ModificareGen, PretMinimPeGen, OrdonareDupaPret, \
    DeterminareCartiCuTitluriDistincte
from Logic.functionalitati import *


def testAplicaDiscount():
    '''


    :return:
    '''

    lista = []
    lista = adaugaCarte("1", "Test1", "Comedie", 12, "gold", lista)
    lista = adaugaCarte("2", "Test2", "Actiune", 12, "silver", lista)
    lista = adaugaCarte("3", "Test3", "Drama", 12, "gold", lista)

    listaNoua = AplicareDiscount(lista)

    assert getPret(listaNoua[0]) == 10.8
    assert getPret(listaNoua[1]) == 11.4
    assert getPret(listaNoua[2]) == 10.8


def testModificareGen():
    lista = []
    lista = adaugaCarte("1", "Test1", "Comedie", 112, "gold", lista)
    lista = adaugaCarte("2", "Test2", "Comedie", 12, "gold", lista)
    lista = adaugaCarte("3", "Test3", "Comedie", 12, "gold", lista)

    lista = ModificareGen(lista, "Test1", "Actiune")

    assert getGen_carte(lista[0]) == "Actiune"
    assert getGen_carte(lista[1]) == "Comedie"
    assert getGen_carte(lista[2]) == "Comedie"


def testPretMinimPeGen():
    lista = []
    lista = adaugaCarte("1", "Test1", "Comedie", 112, "gold", lista)
    lista = adaugaCarte("2", "Test2", "Actiune", 1221, "gold", lista)
    lista = adaugaCarte("3", "Test3", "Comedie", 1442, "gold", lista)
    lista = adaugaCarte("4", "Test2", "Actiune", 1211, "gold", lista)

    rezultat = PretMinimPeGen(lista)

    assert len(rezultat) == 2


def testOrdonareDupaPret():
    lista = []
    lista = adaugaCarte("1", "Test1", "Actiune", 1120, "silver", lista)
    lista = adaugaCarte("12", "Test2", "Actiune", 11120, "silver", lista)
    lista = adaugaCarte("23", "Test3", "Dra", 11220, "silver", lista)

    rezultat = OrdonareDupaPret(lista)

    assert getid(rezultat[0]) == "1"
    assert getid(rezultat[1]) == "12"
    assert getid(rezultat[2]) == "23"


def testDeterminareCartiCuTitluriDistincte():
    lista = []
    lista = adaugaCarte("1", "Test1", "Comedie", 112, "gold", lista)
    lista = adaugaCarte("2", "Test2", "Actiune", 1221, "gold", lista)
    lista = adaugaCarte("3", "Test3", "Comedie", 1442, "gold", lista)
    lista = adaugaCarte("4", "Test2", "Actiune", 1211, "gold", lista)

    rezultat = DeterminareCartiCuTitluriDistincte(lista)

    assert len(rezultat) == 2


def test_undo_si_redo():
    lista = []
    lista_mare = []
    undoList = []
    redoList = []
    lista = creeazaCarte(1, 'Test1', 'Comedie', 123, 'silver')
    undoList.append(lista_mare)
    redoList.clear()
    lista_mare = lista_mare + [lista]

    assert lista_mare == [[1, 'Test1', 'Comedie', 123, 'silver']]

    lista = creeazaCarte(2, 'Test2', 'Comedie', 12, 'silver')
    undoList.append(lista_mare)
    redoList.clear()
    lista_mare = lista_mare + [lista]

    assert lista_mare == [[1, 'Test1', 'Comedie', 123, 'silver'], [2, 'Test2', 'Comedie', 12, 'silver']]

    lista = creeazaCarte(3, 'Test3', 'Actiune', 122, 'gold')
    undoList.append(lista_mare)
    redoList.clear()
    lista_mare = lista_mare + [lista]

    assert lista_mare == [[1, 'Test1', 'Comedie', 123, 'silver'], [2, 'Test2', 'Comedie', 12, 'silver'],
                          [3, 'Test3', 'Actiune', 122, 'gold']]
    redoList.append(lista_mare)
    lista_mare = undoList.pop()

    assert lista_mare == [[1, 'Test1', 'Comedie', 123, 'silver'], [2, 'Test2', 'Comedie', 12, 'silver']]

    redoList.append(lista_mare)
    lista_mare = undoList.pop()

    assert lista_mare == [[1, 'Test1', 'Comedie', 123, 'silver']]
    redoList.append(lista_mare)
    lista_mare = undoList.pop()

    assert lista_mare == []

    redoList.append(lista_mare)
    if len(undoList) > 0:
        lista_mare = undoList.pop()

    assert lista_mare == []

    lista = creeazaCarte(1, 'Test1', 'Comedie', 123, 'silver')
    undoList.append(lista_mare)
    redoList.clear()
    lista_mare = lista_mare + [lista]
    lista = creeazaCarte(2, 'Test2', 'Comedie', 12, 'silver')
    undoList.append(lista_mare)
    redoList.clear()
    lista_mare = lista_mare + [lista]
    lista = creeazaCarte(3, 'Test3', 'Actiune', 122, 'gold')
    undoList.append(lista_mare)
    redoList.clear()
    lista_mare = lista_mare + [lista]


    assert lista_mare == [[1, 'Test1', 'Comedie', 123, 'silver'], [2, 'Test2', 'Comedie', 12, 'silver'], [3, 'Test3', 'Actiune', 122, 'gold']]



    if len(redoList) > 0:
        undoList.append(lista_mare)
        lista_mare = redoList.pop()



    assert lista_mare == [[1, 'Test1', 'Comedie', 123, 'silver'], [2, 'Test2', 'Comedie', 12, 'silver'],
                          [3, 'Test3', 'Actiune', 122, 'gold']]

    redoList.append(lista_mare)
    lista_mare = undoList.pop()

    redoList.append(lista_mare)
    lista_mare = undoList.pop()



    if len(redoList) > 0:
        undoList.append(lista_mare)
        lista_mare = redoList.pop()

    assert lista_mare == [[1, 'Test1', 'Comedie', 123, 'silver'], [2, 'Test2', 'Comedie', 12, 'silver']]


    if len(redoList) > 0:
        undoList.append(lista_mare)
        lista_mare = redoList.pop()

    assert lista_mare == [[1, 'Test1', 'Comedie', 123, 'silver'], [2, 'Test2', 'Comedie', 12, 'silver'],
                          [3, 'Test3', 'Actiune', 122, 'gold']]

    redoList.append(lista_mare)
    lista_mare = undoList.pop()

    redoList.append(lista_mare)
    lista_mare = undoList.pop()

    lista = creeazaCarte(4, 'Test4', 'Actsiune', 122, 'golsad')
    undoList.append(lista_mare)
    redoList.clear()
    lista_mare = lista_mare + [lista]
    assert lista_mare == [[1, 'Test1', 'Comedie', 123, 'silver'], [4, 'Test4', 'Actsiune', 122, 'golsad']]

    if len(redoList) > 0:
        undoList.append(lista_mare)
        lista_mare = redoList.pop()
    assert lista_mare == [[1, 'Test1', 'Comedie', 123, 'silver'], [4, 'Test4', 'Actsiune', 122, 'golsad']]

    redoList.append(lista_mare)
    lista_mare = undoList.pop()
    assert lista_mare == [[1, 'Test1', 'Comedie', 123, 'silver']]

    redoList.append(lista_mare)
    lista_mare = undoList.pop()
    assert lista_mare == []

    if len(redoList) > 0:
        undoList.append(lista_mare)
        lista_mare = redoList.pop()

    if len(redoList) > 0:
        undoList.append(lista_mare)
        lista_mare = redoList.pop()
    assert lista_mare == [[1, 'Test1', 'Comedie', 123, 'silver'], [4, 'Test4', 'Actsiune', 122, 'golsad']]

    if len(redoList) > 0:
        undoList.append(lista_mare)
        lista_mare = redoList.pop()
    assert lista_mare == [[1, 'Test1', 'Comedie', 123, 'silver'], [4, 'Test4', 'Actsiune', 122, 'golsad']]






