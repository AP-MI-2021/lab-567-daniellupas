def creeazaCarte(id, titlu, gen, pret, tip_reducere):
    '''
    creeaza un dictionar ce reprezinta o carte
    :param id: string
    :param titlu: string
    :param gen: string
    :param pret: int
    :param tip_reducere: string
    :return: un dictionar ce creeaza o vanzare
    '''

    list = [id, titlu, gen, pret, tip_reducere]

    return list


def getid(carte):
    '''
    da id-ul unei carti
    :param carte: dictionar ce contine o carte
    :return: id-ul cartii
    '''
    return carte[0]


def getTitlu_carte(carte):
    '''
    da titlul unei carti
    :param carte: dictionar ce contine o carte
    :return: titlul cartii
    '''

    return carte[1]


def getGen_carte(carte):

    return carte[2]


def getPret(carte):

    return carte[3]


def getTip_reducere(carte):

    return carte[4]


def toString(carte):
    '''
    convertirea tuturor parametriilor in string
    :param carte: un dictionar ce contine informatiile unei carti
    :return: o afisare bine structurata
    '''
    return "id: {}, Titlu:{}, Gen:{}, Pret:{}, Tip-Reducere:{}".format(
        getid(carte),
        getTitlu_carte(carte),
        getGen_carte(carte),
        getPret(carte),
        getTip_reducere(carte)
    
    )


def get_str(carte):
    '''
    o metoda de afisare intr-o forma convenabila
    :param carte:
    :return:
    '''
    return f'Cartea cu id-ul  {getid(carte)}, cu titlul {getTitlu_carte(carte)} ' \
           f' , genul {getGen_carte(carte)}, pretul: {getPret(carte)} , tipul reducerii: {getTip_reducere(carte)}.'
