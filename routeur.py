import random
import numpy as np

# capacité maximal
CAPACITE_MAX = 100
# perte maximal
PERTE_MAX = 0.05
# duree maximal
T_MAX = 10000

def duree_exp(lambda):
    """ Genere une durée suivant la loi expodentiel en \"lambda\"
        @param lambda parametre de la loi expodentiel
    """
    return np.random.expodential(1/lambda)

def categorie_uni(C):
    """ Genere une categorie suivant la loi uniforme en fonction de \"C\"
        @param C nombre de groupe ou de categorie
    """   
    return np.random.uniform(1, C)

def simul_fifo(lambda, C):
    """ simule la file d'attente en fonction du taux d'arrivée lam
    retourne les statistiques mesurées"""

    # les variables
    t = 0 # temps
    n = 0 # nombre de clients à chaque date
    echeancier = [] # contient les événements à venir
    # On initialise l'échéancier en ajoutant un client
    heappush(echeancier, (0, categorie_uni(C),"client"))
    # evolution du nombre de clients au cours du temps
    n_t = [] 
    
    # boucle principale
    while t < T_MAX:
        # on récupère les données à afficher
        n_t.append([t, n])
        # on extrait l'événement le plus proche dans le temps
        evt = heappop(echeancier)
        # on met à jour la date
        t = evt[0]
        # on traite l'événement
        match evt[2]:
            case "service":
                # un client part
                n -= 1
                # si il reste un client, il commence son service
                if n > 0:
                    heappush(echeancier, evt[1], (t + duree_exp(1), "service"))
            case "client":
                # on calcule la date d'arrivée du prochain client
                heappush(echeancier, categorie_uni(C), (t + duree_exp(lam), "client"))
                n += 1
                # si la file était vide, on commence un service
                if n == 1:
                    heappush(echeancier, evt[1], (t + duree_exp(1), "service"))

    # on retourne les statistiques mesurées 
    return n_t