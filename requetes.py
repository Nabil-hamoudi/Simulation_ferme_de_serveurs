import random

class Requete:
    def __init__(self, C):
        """Initialise une requête avec une catégorie attribuée aléatoirement."""
        if C not in {1, 2, 3, 6}:
            raise ValueError("C doit être un des éléments suivants: {1, 2, 3, 6}.")
        self.categorie = random.randint(1, C)
    
    def __repr__(self):
        return f"Requete(categorie={self.categorie})"
