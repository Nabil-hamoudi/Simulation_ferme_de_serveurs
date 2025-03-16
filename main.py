import heapq
import numpy as np
from routeur import simul_fifo, duree_exp
from serveurs import SERVEURS, C

# Paramètres de simulation
lambda_requete = 0.5  # Taux d'arrivée des requêtes
C_value = 1  # Nombre de groupes de serveurs

def main():
    """Initialise un groupe de 12 serveurs et simule la file d'attente avec C=1"""
    global SERVEURS
    SERVEURS = [0 for _ in range(12)]  # Initialisation des serveurs
    
    # Lancer la simulation
    stats = simul_fifo(lambda_requete, C_value)
    
    # Affichage des statistiques
    for time, clients in stats[:100]:  # Affichage des 10 premiers résultats
        print(f"Temps: {time:.2f}, Nombre de clients: {clients}")
    
if __name__ == "__main__":
    main()
