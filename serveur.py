class Serveur:
    def __init__(self):
        """ Initialise un serveur avec une file pouvant contenir une seule requête. """
        self.requete = None
    
    def est_occupe(self):
        """ Vérifie si le serveur est occupé. """
        return self.requete is not None
    
    def ajouter_requete(self, requete):
        """ Ajoute une requête au serveur si celui-ci est libre. """
        if self.est_occupe():
            raise Exception("Le serveur est déjà occupé.")
        self.requete = requete
    
    def liberer(self):
        """ Libère le serveur de sa requête. """
        self.requete = None
    
    def __repr__(self):
        return f"Serveur(occupe={self.est_occupe()}, requete={self.requete})"
