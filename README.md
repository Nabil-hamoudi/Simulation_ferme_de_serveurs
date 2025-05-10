# Simulation Ferme De Serveurs

Mars-Mai 2025.

Nabil Hamoudi (22006316) \
Nicolas Chaumont (21914689)

## Repertoire du projet

https://github.com/Nabil-hamoudi/Simulation_ferme_de_serveurs

## Prérequis

Jupyter, Python 3.11.8 minimum, Numpy, matplotlib

## Structure du code:

### Routeur.py

Code principal de notre projet, il contient le code permettant de faire une simulation du système.

#### duree_exp(lambda_requete) :

Génère un nombre aléatoire flottant suivant la loi exponentielle de paramètre lambda_requete.

#### typeserveur(C) :

Prend en entrée C le nombre de types de serveur.

Génère un type de serveur un nombre entier entre 0 et C-1 de manière uniforme pour chaque type de serveur possible.

#### tempmoyenclient(depart, arrive) :

Prend en entrée la liste des dates de départ et la liste des dates d'arrivée

Calcule le temps moyen pour tous les clients avant d'avoir reçu une réponse à leur requête, selon la formule suivante:

$$ \frac1n \sum_{i=1}^{n}D_i  $$
où $D_i$ est le temps d'attente du i-ème client
$$D_i = \min_{j \geq 1}\{T_j^d : T_j^d \geq T_i^a \} - T_{i}^a $$
$T^d$ sont les dates de départ. \
$T^a$ sont les dates d'arrivée.


#### simul_fifo(lambda_requete, C, T_MAX) :

Prend en entrée lambda_requete le taux de clients arrivant dans le routeur.

C le nombre de type de serveurs.

T_MAX la durée maximale de la simulation.

Simule le système en adéquation avec le projet.

### main.ipynb

Pour le main, nous avons pris la décision d'utiliser un notebook. En effet, nous pensons que cela permettra d'améliorer la clarté de notre code ainsi que d'expliquer celui-ci dans le notebook lui-même.