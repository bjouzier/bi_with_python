
def calculer_moyenne(liste):
    """
    modifié le 12/02/25 à 11:06
    Calcule la moyenne des éléments d'une liste.

    Arguments:
        liste (list): Une liste de nombres.

    Returns:
        float: La moyenne des nombres dans la liste.
    """
    if not liste:
        return 0
    return sum(liste) / len(liste)

