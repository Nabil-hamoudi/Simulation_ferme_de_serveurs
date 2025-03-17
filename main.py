import heapq
import numpy as np
from routeur import simul_fifo, duree_exp
from serveurs import SERVEURS, C
from requetes import attribuer_type_requete  # Importation du fichier requetes

# Paramètres de simulation
lambda_requete = 0.5  # Taux d'arrivée des requêtes
C_value = 2  # Nombre de groupes de serveurs (doit être dans {1, 2, 3, 6})

def main():
    """Initialise un groupe de 12 serveurs et simule la file d'attente avec C=1"""
    global SERVEURS
    SERVEURS = [0 for _ in range(12)]  # Initialisation des serveurs

    # Taille d'un groupe de serveurs
    K = 12 // C_value  # Chaque groupe contient K serveurs

    # Lancer la simulation
    stats = simul_fifo(lambda_requete, C_value)

    # Affichage des statistiques avec suivi des groupes et attribution des requêtes
    for time, clients in stats[:100]:  # Affichage des 100 premiers résultats
        type_requete = attribuer_type_requete(C_value)  # Affectation d'un type de requête
        groupe_index = type_requete  # Le groupe correspond directement au type de requête
        serveur_index = groupe_index * K + (clients - 1) % K if clients > 0 else None  # Sélection d'un serveur dans le groupe

        if serveur_index is not None:
            SERVEURS[serveur_index] += 1  # Mise à jour du serveur recevant la requête

        print(f"\nTemps: {time:.2f}, Nombre de clients dans la file ou en service: {clients}, "
              f"\nGroupe de serveurs: {groupe_index}, "
              f"Serveur attribué: {serveur_index if serveur_index is not None else 'Aucun'}, "
              f"Type de requête: {type_requete}")
    
if __name__ == "__main__":
    main()
