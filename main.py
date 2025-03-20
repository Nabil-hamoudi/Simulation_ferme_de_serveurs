import heapq
import numpy as np
from routeur import simul_fifo, duree_exp
from serveurs import liste_serveurs
#from requetes import attribuer_type_requete
import serveurs

# Paramètres de simulation
lambda_requete = 0.5  # Taux d'arrivée des requêtes
ENSEMBLE_VALIDE_C = {1, 2, 3, 6}
C = 2  # Nombre de groupes de serveurs (doit être dans ensemble_valide_C = {1, 2, 3, 6})

def main():
    """Initialise un groupe de 12 serveurs et simule la file d'attente avec C donné"""
    if C not in ENSEMBLE_VALIDE_C:
        raise ValueError("C doit être un des éléments suivants: {1, 2, 3, 6}.")
    
    # Initialisation des serveurs et des groupes
    liste_serveurs, groupes, K = serveurs.initialiser_serveurs(C)
    serveurs.afficher_groupes(groupes)

    # Lancer la simulation
    stats = simul_fifo(lambda_requete, C)

    taux_perte = 0
    # Affichage des statistiques avec suivi des groupes et attribution des requêtes
    for time, clients in stats[:100]:  # Affichage des 100 premiers résultats
        """ type_requete = attribuer_type_requete(C)  # Affectation d'un type de requête
        groupe_index = type_requete  # Le groupe correspond directement au type de requête
        serveur_index = groupe_index * K + (clients - 1) % K if clients > 0 else None  # Sélection d'un serveur dans le groupe
        if serveur_index is None:
            taux_perte += 1

        print(f"\nTemps: {time:.2f} \nNombre de clients dans la file ou en service: {clients} "
              f"\nGroupe de serveurs: {groupe_index}, "
              f"Serveur attribué: {serveur_index if serveur_index is not None else 'Aucun'}, "
              f"Type de requête: {type_requete}") """
                
    print("taux de perte ", taux_perte/100)
if __name__ == "__main__":
    main()
