import heapq
import numpy as np
from groupe import Groupe
from routeur import simul_fifo, duree_exp
# from serveurs import liste_serveurs
import serveur

# Paramètres de simulation
lambda_requete = 0.5  # Taux d'arrivée des requêtes
ENSEMBLE_VALIDE_C = {1, 2, 3, 6}
# Nombre de groupes de serveurs (doit être dans ensemble_valide_C = {1, 2, 3, 6})
C = 2


def main():
    """Initialise un groupe de 12 serveurs et simule la file d'attente avec C donné"""
    if C not in ENSEMBLE_VALIDE_C:
        raise ValueError("C doit être un des éléments suivants: {1, 2, 3, 6}.")

    # Initialisation des serveurs et des groupes
    liste_groupes = []
    for categorie in range(1, C + 1):
        groupe = Groupe(C, categorie)
        liste_groupes.append(groupe)
        groupe.afficher_details()

    # Lancer la simulation
    stats = simul_fifo(lambda_requete, C, liste_groupes)

    taux_perte = 0
    # Affichage des statistiques avec suivi des groupes et attribution des requêtes


if __name__ == "__main__":
    main()
