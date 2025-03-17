ensemble_valide_C = {1, 2, 3, 6}  # Ensemble des valeurs valides pour C
SERVEURS = []
GROUPES = {}


def initialiser_serveurs(C_value):
    """ Initialise les serveurs et les groupes en fonction de C """
    global SERVEURS, GROUPES
    if C_value not in ensemble_valide_C:
        raise ValueError("C doit être un des éléments suivants: {1, 2, 3, 6}.")

    K = 12 // C_value  # Taille de chaque groupe
    SERVEURS = [0 for _ in range(12)]
    GROUPES = {i: [] for i in range(C_value)}

    for i in range(12):
        groupe = i // K
        GROUPES[groupe].append(i)

    return SERVEURS, GROUPES, K


def afficher_groupes():
    """Affiche chaque groupe et les serveurs qu'il contient."""
    for groupe, serveurs in GROUPES.items():
        print(f"Groupe {groupe}: {serveurs}")


# pas utilisé mais servira peut-être, tu peux supprimer si tu veux
def groupe_du_serveur(serveur_id):
    """
    Retourne le groupe auquel appartient un serveur donné.
    :param serveur_id: L'identifiant du serveur (entre 0 et 11)
    :return: L'index du groupe auquel appartient le serveur
    """
    for groupe, serveurs in GROUPES.items():
        if serveur_id in serveurs:
            return groupe
    return None


# pas utilisé mais servira peut-être, tu peux supprimer si tu veux
def get_serveurs_et_groupes():
    """Retourne les serveurs et leurs groupes actuels"""
    return SERVEURS, GROUPES
