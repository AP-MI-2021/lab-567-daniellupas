def creeazaCarte(id, titlu, gen, pret, tip_reducere):
    '''
    creeaza un dictionar ce reprezinta o carte
    :param id: string
    :param titlu_cate: string
    :param gen_carte: string
    :param pret: int
    :param tip_reducere: string
    :return: un dictionar ce creeaza o vanzare
    '''
    return  {

        "id": id,
        "titlu_carte": titlu,
        "gen_carte": gen,
        "pret": pret,
        "tip_reducere": tip_reducere
    }

def getid(carte):
    '''
    da id-ul unei carti
    :param carte: dictionar ce contine o carte
    :return: id-ul cartii
    '''
    return carte["id"]

def getTitlu_carte(carte):

    return carte["titlu_carte"]

def getGen_carte(carte):

    return carte["gen_carte"]

def getPret(carte):

    return carte["pret"]

def getTip_reducere(carte):

    return carte["tip_reducere"]

def toString(carte):
    return "id: {}, Titlu:{}, Gen:{}, Pret:{}, Tip-Reducere:{}".format(
        getid(carte),
        getTitlu_carte(carte),
        getGen_carte(carte),
        getPret(carte),
        getTip_reducere(carte)
    
    )