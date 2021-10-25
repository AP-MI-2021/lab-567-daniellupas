from Domain.carte import getid, getTitlu_carte, getGen_carte, getPret, getTip_reducere
from Logic.CRUD import adaugaCarte, getById, stergeCarte, modificaCarte


def testAdaugaCarte():
    '''
    verificam daca o carte adaugata este adaugata corect
    :return:
    '''
    lista = []
    lista = adaugaCarte("1", "Test1", "Actiune", 10, "gold", lista)

    assert getid(getById("1", lista)) == "1"
    assert getTitlu_carte(getById("1", lista)) == "Test1"
    assert getGen_carte(getById("1", lista)) == "Actiune"
    assert getPret(getById("1", lista)) == 10
    assert getTip_reducere(getById("1", lista)) == "gold"


def testStergeCarte():
    lista = []
    lista = adaugaCarte("1", "Test1", "Actiune", 10, "gold", lista)
    lista = adaugaCarte("2", "Test2", "Comedie", 10, "gold", lista)

    lista = stergeCarte("1", lista)

    assert len(lista) == 1
    assert getById("1", lista) is None
    assert getById("2", lista) is not None

def testModificaCarte():
    lista = []
    lista = adaugaCarte("1", "Test1", "Actiune", 10, "gold", lista)
    lista = adaugaCarte("2", "Test2", "Comedie", 10, "gold", lista)

    lista = modificaCarte("1", "da", "ok", 12, "silver", lista)

    CarteUpdatata = getById("1", lista)
    assert getid(getById("1", lista)) == "1"
    assert getTitlu_carte(getById("1", lista)) == "da"
    assert getGen_carte(getById("1", lista)) == "ok"
    assert getPret(getById("1", lista)) == 12
    assert getTip_reducere(getById("1", lista)) == "silver"

    CarteNeupdatata = getById("1", lista)
    assert getid(getById("1", lista)) == "1"
    assert getTitlu_carte(getById("1", lista)) == "Test1"
    assert getGen_carte(getById("1", lista)) == "Actiune"
    assert getPret(getById("1", lista)) == 10
    assert getTip_reducere(getById("1", lista)) == "gold"


