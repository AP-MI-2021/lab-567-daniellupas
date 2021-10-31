from Domain.carte import creeazaCarte, getid, getTip_reducere, getPret


def adaugaCarte(id, titlu, gen, pret, tip_reducere, lista):
    '''
    adaugam o carte intr-o lista
    :param id: string
    :param titlu: string
    :param gen: string
    :param pret: int
    :param tip_reducere: string
    :param lista: returnam o lista de carti
    :return: lista care contine si elemente noi si elemente vechi
    '''
    if getById(id, lista) is not None:
        raise ValueError("id-ul exista deja!")

    carte = creeazaCarte(id, titlu, gen, pret, tip_reducere)
    return lista + [carte]


def getById(id, lista):
    '''
    da carte cu id-ul dat
    :param id:
    :param lista:
    :return: carte cu id-u dat din lista sau None , daca nu exista
    '''

    for carte in lista:
        if getid(carte) == id:
            return carte
    return None


def stergeCarte(id, lista):
    '''

    :param id:
    :param lista:
    :return: o lista de carti
    '''
    if getById(id, lista) is None:
        raise ValueError("Cartea pe care doresti sa o stergi nu exista!")

    return [carte for carte in lista if getid(carte) != id]


def modificaCarte(id, titlu, gen, pret, tip_reducere, lista):
    '''
    modifica o carte din lista
    :param id: string
    :param titlu: string
    :param gen: string
    :param pret: string
    :param tip_reducere: string
    :return:
    '''

    if getById(id,lista) is None:
        raise ValueError("Cartea pe care doresti sa o modifici nu exista")
    listaNoua = []

    for carte in lista:
        if getid(carte) == id:
            carteNoua = creeazaCarte(id, titlu, gen, pret, tip_reducere)
            listaNoua.append(carteNoua)
        else:
            listaNoua.append(carte)
    return listaNoua


