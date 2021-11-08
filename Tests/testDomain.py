from Domain.carte import creeazaCarte, getid, getTitlu_carte, getGen_carte, getPret, getTip_reducere


def testCarte():
    carte = creeazaCarte("1", "Singur pe Lume", "Aventura", 35, "silver")

    assert getid(carte) == "1"
    assert getTitlu_carte(carte) == "Singur pe Lume"
    assert getGen_carte(carte) == "Aventura"
    assert getPret(carte) == 35
    assert getTip_reducere(carte) == "silver"
