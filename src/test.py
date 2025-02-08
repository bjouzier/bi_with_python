def calculer_moyenne(liste):
    """
    Calcule la moyenne des éléments d'une liste.

    Arguments:
        liste (list): Une liste de nombres.

    Returns:
        float: La moyenne des nombres dans la liste.
    """
    if not liste:
        return 0
    return sum(liste) / len(liste)
