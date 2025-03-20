import numpy as np

class Requete:
    def __init__(self, C):
        """ Initialise une requête avec une catégorie attribuée aléatoirement. """
        if C not in {1, 2, 3, 6}:
            raise ValueError("C doit être un des éléments suivants: {1, 2, 3, 6}.")
        self.categorie = np.random.randint(1, C + 1)  # Génère une catégorie entre 1 et C inclus

    def __repr__(self):
        return f"Requete(categorie={self.categorie})"

    def get_categorie(self):
        """ Retourne la catégorie de la requête. """
        return self.categorie
