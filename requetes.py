import random

def attribuer_type_requete(C):
    """
    Génère un type de requête aléatoire entre 1 et C-1.
    
    :param C: Nombre total de catégories de requêtes (doit être dans {1, 2, 3, 6})
    :return: Un entier entre 0 et C-1 représentant le type de requête
    """
    if C not in {1, 2, 3, 6}:
        raise ValueError("C doit être un des éléments suivants: {1, 2, 3, 6}.")
    
    return random.randint(0, C-1)

# Exemple d'utilisation
if __name__ == "__main__":
    C = 6  # Exemple avec 3 catégories de requêtes (0, 1, 2)
    for _ in range(10):  # Générer 10 requêtes
        print(attribuer_type_requete(C))