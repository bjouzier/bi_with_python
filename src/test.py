import random

def calculer_moyenne(liste):
    """
    modifié le 08/02/25 à 17:11
    Calcule la moyenne des éléments d'une liste.

    Arguments:
        liste (list): Une liste de nombres.

    Returns:
        float: La moyenne des nombres dans la liste.
    """
    if not liste:
        return 0
    return sum(liste) / len(liste)

    def generer_nombre_aleatoire():
        """
        Génère un nombre aléatoire entre 0 et 11.

        Returns:
            int: Un nombre aléatoire entre 0 et 11.
        """
        return random.randint(0, 11)
    generer_nombre_aleatoire()