import heapq
import numpy as np

# Valeur C accepter
C_VAL = (1, 2, 3, 6)

# Expodentiel
EXPODEN_C = {1: 4/20, 2: 7/20, 3: 10 / 20, 6: 14 / 20}

# capacité maximale
CAPACITE_MAX = 100
# nombre de serveurs
NBR_SERVEURS = 12
# Taux de rejet maximum
TAUX_REJET_MAX = 0.05


def duree_exp(lambda_requete):
    """ Génère une durée suivant la loi exponentielle en lambda """
    return np.random.exponential(1 / lambda_requete)


def typeserveur(C):
    """Genere une valeur correspondant au type de serveur"""
    return np.random.randint(0, C)


def tempmoyenclient(depart, arrive):
    """Cacul le temp moyen d'attente avec les arrivé et depart client"""
    temp_moyen = 0
    arrive.sort()
    depart.sort()
    for i in arrive:
        for j in range(0, len(depart)):
            if depart[j] >= i:
                temp_moyen += min(depart[j:]) - i
                del depart[j]
                break
    return temp_moyen * (1/len(arrive))


def simul_fifo(lambda_requete, C, T_MAX):
    """ Simule la file d'attente en fonction du taux d'arrivée lambda_requete """
    if C not in C_VAL:
        return None
    # On initialise le nombre de serveur par type
    nombre_serveurs_type = NBR_SERVEURS // C
    # On initialise si serveur dispo ou non
    serveurs = [0 for _ in range(C)]
    # temp de traitement routeur
    temp_routeur = (C - 1) / C

    # Variables
    t = 0  # Temps actuel
    n = 0  # Nombre de clients à chaque instant

    type_serv = None  # dis quel type de serveur est le prochain
    n_tot = 0  # nombre client total
    n_drop = 0  # Nombre de clients drop
    routeur_dispo = True # dis si le routeur est dispo
    echeancier = []  # Contient les événements à venir
    # On initialise l'échéancier avec l'arrivée du premier client
    heapq.heappush(echeancier, (0, None, "client"))
    n += 1
    n_tot += 1
    # Evolution du nombre de clients au cours du temps
    n_t = []
    # stock les arrivé et sortie client pour temp moyen
    arrive = []
    depart = []
    # dis si la simulation est rejetter car le taux de rejet max depasser
    rejeter = False

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
            serveurs[evt[1]] -= 1
            depart.append(t)
        elif evt[2] == "client":
            # regarde si la file est pleine
            n_tot += 1
            if n < CAPACITE_MAX:
                n += 1
                arrive.append(t)
                # verifie que routeur ne soit pas bloque
                if type_serv is None:
                    type_serv = typeserveur(C)
                if (serveurs[type_serv] < nombre_serveurs_type) and routeur_dispo:
                    serveurs[type_serv] += 1
                    heapq.heappush(
                        echeancier, (t + temp_routeur, type_serv, "routeur"))
                    type_serv = None
                    routeur_dispo = False
            else:
                n_drop += 1
            # Un nouveau client arrive
            heapq.heappush(
                echeancier, (t + duree_exp(lambda_requete), None, "client"))
        elif evt[2] == "routeur":
            n -= 1
            routeur_dispo = True
            heapq.heappush(
                echeancier, (t + duree_exp(EXPODEN_C[C]), evt[1], "service"))
            if n > 0:
                # calcul prochain routeur
                # verifie que routeur ne soit pas bloque
                if type_serv is None:
                    type_serv = typeserveur(C)
                if (serveurs[type_serv] < nombre_serveurs_type) and routeur_dispo:
                    serveurs[type_serv] += 1
                    heapq.heappush(
                        echeancier, (t + temp_routeur, type_serv, "routeur"))
                    type_serv = None
                    routeur_dispo = False

    # Retourne les statistiques mesurées
    return {"nombre_client et temp" : n_t, "temp_moyen_attente_client" : tempmoyenclient(depart, arrive), "taux_rejet" : n_drop / n_tot}
