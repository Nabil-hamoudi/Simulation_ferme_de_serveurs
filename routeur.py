import heapq
import random
import numpy as np

#from requetes import attribuer_type_requete
from requetes import Requete

# capacité maximale
CAPACITE_MAX = 100
# perte maximale
PERTE_MAX = 0.05
# durée maximale
T_MAX = 10000

def duree_exp(lambda_requete):
    """ Génère une durée suivant la loi exponentielle en lambda """
    return np.random.exponential(1 / lambda_requete)

def simul_fifo(lambda_requete, C):
    """ Simule la file d'attente en fonction du taux d'arrivée lambda_requete """
    # Variables
    t = 0  # Temps actuel
    n = 0  # Nombre de clients à chaque instant
    echeancier = []  # Contient les événements à venir
    
    # On initialise l'échéancier avec l'arrivée du premier client
    heapq.heappush(echeancier, (0, Requete(C), "client"))
    
    # Evolution du nombre de clients au cours du temps
    n_t = []
    
    # Boucle principale de simulation
    while t < T_MAX:
        # On récupère les données à afficher
        n_t.append([t, n])
        
        # On extrait l'événement le plus proche dans le temps
        if not echeancier:
            break
        
        evt = heapq.heappop(echeancier)
        t = evt[0]
        
        if evt[2] == "service":
            # Un client termine son service
            n -= 1
            if n > 0:
                heapq.heappush(echeancier, (t + duree_exp(1), None, "service"))
        elif evt[2] == "client":
            # Un nouveau client arrive
            heapq.heappush(echeancier, (t + duree_exp(lambda_requete), Requete(C), "client"))
            n += 1
            if n == 1:
                heapq.heappush(echeancier, (t + duree_exp(1), None, "service"))
    
    # Retourne les statistiques mesurées
    return n_t
