import random
from serveur import Serveur

class Groupe:
    def __init__(self, C, categorie):
        """ Initialise un groupe avec une catégorie et une liste de serveurs """
        if C not in {1, 2, 3, 6}:
            raise ValueError("C doit être un des éléments suivants: {1, 2, 3, 6}.")
        if categorie not in {1, 2, 3, 4, 5, 6}:
            raise ValueError("La catégorie doit être un des éléments suivants: {1, 2, 3, 4, 5, 6}.")
        
        self.categorie = categorie
        self.serveurs = [Serveur() for _ in range(12//C)]
    
    def __repr__(self):
        return f"Groupe(categorie={self.categorie}, serveurs={self.serveurs})"

    def afficher_details(self):
        """ Affiche la taille du groupe et la liste des serveurs """
        print(f"Groupe de catégorie {self.categorie} avec {len(self.serveurs)} serveurs:")
        for i, serveur in enumerate(self.serveurs, 1):
            print(f"  Serveur {self.categorie}_{i}: {serveur}")
