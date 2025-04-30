import heapq
import numpy as np

# from requetes import attribuer_type_requete
from requetes import Requete

# capacité maximale
CAPACITE_MAX = 100
# perte maximale
PERTE_MAX = 0.05
# durée maximale
T_MAX = 100
# nombre de serveurs
NBR_SERVEURS = 12


def duree_exp(lambda_requete):
    """ Génère une durée suivant la loi exponentielle en lambda """
    return np.random.exponential(1 / lambda_requete)


def typeserveur(C):
    """Genere une valeur correspondant au type de serveur"""
    return np.random.randint(0, C)


def simul_fifo(lambda_requete, C):
    """ Simule la file d'attente en fonction du taux d'arrivée lambda_requete """
    # On initialise le nombre de serveur par type
    nombre_serveurs_type = NBR_SERVEURS // C
    # On initialise si serveur dispo ou non
    serveurs = [0 for _ in range(C)]

    # Variables
    t = 0  # Temps actuel
    n = 0  # Nombre de clients à chaque instant

    n_tot = 0  # nombre client total
    n_drop = 0  # Nombre de clients drop
    echeancier = []  # Contient les événements à venir
    # On initialise l'échéancier avec l'arrivée du premier client
    heapq.heappush(echeancier, (0, typeserveur(C), "client"))
    n += 1
    n_tot += 1
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
            serveurs[evt[1]] -= 1
        elif evt[2] == "client":
            # regarde si plein
            if serveurs[evt[1]] > nombre_serveurs_type:
                n_drop += 1
            else:
                serveurs[evt[1]] += 1
                heapq.heappush(
                    echeancier, (t + duree_exp(1), evt[1], "service"))
            # Un nouveau client arrive
            heapq.heappush(
                echeancier, (t + duree_exp(lambda_requete), typeserveur(C), "client"))
            n += 1

    # Retourne les statistiques mesurées
    return n_t
