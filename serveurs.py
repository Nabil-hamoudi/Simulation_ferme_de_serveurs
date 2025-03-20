ENSEMBLE_VALIDE_C = {1, 2, 3, 6}  # Ensemble des valeurs valides pour C
liste_serveurs = []
groupes = {}

def initialiser_serveurs(C_value):
    """ Initialise les serveurs et les groupes en fonction de C """
    liste_serveurs = []
    groupes = {}
    if C_value not in ENSEMBLE_VALIDE_C:
        raise ValueError("C doit être un des éléments suivants: {1, 2, 3, 6}.")
    
    k = 12 // C_value  # Taille de chaque groupe
    liste_serveurs = [0 for _ in range(12)]
    groupes = {i: [] for i in range(C_value)}
    
    for i in range(12):
        groupe = i // k
        groupes[groupe].append(i)

    return liste_serveurs, groupes, k

def afficher_groupes(groupes):
    """Affiche chaque groupe et les serveurs qu'il contient."""
    for groupe, serveurs in groupes.items():
        print(f"Groupe {groupe}: {serveurs}")

# pas utilisé mais servira peut-être, tu peux supprimer si tu veux
def groupe_du_serveur(serveur_id):
    """
    Retourne le groupe auquel appartient un serveur donné.
    :param serveur_id: L'identifiant du serveur (entre 0 et 11)
    :return: L'index du groupe auquel appartient le serveur
    """
    for groupe, serveurs in groupes.items():
        if serveur_id in serveurs:
            return groupe
    return None

# pas utilisé mais servira peut-être, tu peux supprimer si tu veux
def get_serveurs_et_groupes():
    """Retourne les serveurs et leurs groupes actuels"""
    return liste_serveurs, groupes
