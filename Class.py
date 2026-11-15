import pyxel

class Joueur:
    def __init__(self, numero):
        self.numero = numero

class Forme:
    def __init__(self, joueur, ligne, colonne):
        self.joueur = joueur.numero
        self.ligne = ligne
        self.colonne = colonne

        self.image = 0
        self.v = 0
        self.largeur = 9
        self.hauteur = 9
        self.colkey = 0
        self.scale = 4

    def position(self):
        self.x = self.colonne
        self.y = self.ligne
        self.u = (self.joueur-1) * 9
        
    def affichage(self):
        pyxel.blt(self.x, self.y, self.image, self.u, self.v, self.largeur, self.hauteur, self.colkey, scale = self.scale)

class Grille:
    def __init__(self):
        self.x = 110
        self.y = 110
        self.image = 1
        self.u = 6
        self.v = 6
        self.hauteur = 37
        self.largeur = 37
        self.colkey = 0
        self.scale = 6

    def affichage(self):
        pyxel.blt(self.x, self.y, self.image, self.u, self.v, self.largeur, self.hauteur, self.colkey, scale = self.scale)