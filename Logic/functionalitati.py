from Domain.carte import getPret, getGen_carte, getTitlu_carte, getTip_reducere, creeazaCarte, getid



def AplicareDiscount(lista):
    '''
    aplicam un discount tuturor cartiilor care sunt din categoria gold sau silver
    :param lista: o lista care contine cartiile date
    :return: o noua lista cu discount-urile adaugate
    '''
    listaNoua = []

    for carte in lista:
        if getTip_reducere(carte) == "silver":
            carteNoua = creeazaCarte(getid(carte),
                                     getTitlu_carte(carte),
                                     getGen_carte(carte),
                                     getPret(carte) - (0.05 * getPret(carte)),
                                     getTip_reducere(carte)
                                     )

            listaNoua.append(carteNoua)
        elif getTip_reducere(carte) == "gold":
            carteNoua = creeazaCarte(getid(carte),
                                     getTitlu_carte(carte),
                                     getGen_carte(carte),
                                     getPret(carte) - (0.10 * getPret(carte)),
                                     getTip_reducere(carte)
                                     )

            listaNoua.append(carteNoua)
        else:
            listaNoua.append(carte)
    return listaNoua


def ModificareGen(lista, titlu, gen):
    '''
    Modificarea genului pentru un titlu dat.
    :param lista: lista data
    :param titlu: string
    :param gen: string
    :return: lista noua cu informatiile modificate
    '''
    listaNoua = []


    for carte in lista:
        if getTitlu_carte(carte) == titlu:
            carteNoua = creeazaCarte(getid(carte),
                                     getTitlu_carte(carte),
                                     gen,
                                     getPret(carte),
                                     getTip_reducere(carte)
                                     )

            listaNoua.append(carteNoua)
        else:
            listaNoua.append(carte)

    return listaNoua


def PretMinimPeGen(lista):
    '''
    Determinarea prețului minim pentru fiecare gen.
    :param lista: o lista care contine cartiile date
    :return: un dictionar care contine pretul minim pentru fiecare gen
    '''

    rezultat = {}

    for carte in lista:
        gen = getGen_carte(carte)
        pret = getPret(carte)

        if gen not in rezultat:
            rezultat[gen] = carte
        else:
            if pret < getPret(rezultat[gen]):
                rezultat[gen] = carte

    return rezultat


def OrdonareDupaPret(lista):
    '''
    Ordonarea vânzărilor crescător după preț.
    :param lista: o lista care contine cartiile date
    :return: o versiune sortata a listei dupa pret , in ordine crescatoare
    '''
    return sorted(lista, key=lambda carte: getPret(carte))


def DeterminareCartiCuTitluriDistincte(lista):
    '''
    Afișarea numărului de titluri distincte pentru fiecare gen.
    :param lista: o lista care contine cartiile date
    :return: un dictionar ce contine informatiile cerute
    '''

    genuri = {}
    titluri = {}

    for carte in lista:
        gen = getGen_carte(carte)
        titlu = getTitlu_carte(carte)
        if gen in genuri:
            if titlu not in titluri:
                genuri[gen] += 1
                titluri[titlu] = titlu
        else:
            genuri[gen] = 1
            titluri[titlu] = titlu

    return genuri


def undo(lista, undoList, redoList):
    redoList.append(lista)
    lista = undoList.pop()
    return lista, undoList, redoList


def redo(lista, undoList, redoList):
    undoList.append(lista)
    lista = redoList.pop()
    return lista, undoList, redoList