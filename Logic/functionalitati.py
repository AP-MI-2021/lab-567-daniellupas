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





