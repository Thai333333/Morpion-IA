import pyxel

class Joueur:
    def __init__(self, numero):
        self.numero = numero

class Forme:
    def __init__(self, joueur, ligne, colonne):
        self.joueur = joueur
        self.ligne = ligne
        self.colonne = colonne

        self.image = 0
        self.v = 0
        self.largeur = 9
        self.hauteur = 9
        self.colkey = 0
        self.scale = 5

    def position(self):
        self.x = (self.colonne - 1) * 73 + 50
        self.y = (self.ligne - 1) * 74 + 50
        self.u = (self.joueur - 1) * 11

        
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

class Case:
    def __init__(self,numero):
        self.numero = numero

        self.x = 0
        self.y = 0

    def position(self):
        if self.numero < 4:
            self.x = (self.numero - 1) * 73 + 20
            self.y = 20
        elif self.numero < 7:
            self.x = (self.numero - 4) * 73 + 20
            self.y = 94
        else:
            self.x = (self.numero - 7) * 73 + 20
            self.y = 165

    def est_clique(self) -> bool:
        if (self.x <= pyxel.mouse_x <= self.x + 71
            and self.y <= pyxel.mouse_y <= self.y + 72
            and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT)
        ):
            return True

    def ligne_et_colonne(self):
        if self.numero < 4:
            self.ligne = 1
        elif self.numero < 7:
            self.ligne = 2
        else:
            self.ligne = 3

        if self.numero in [1,4,7]:
            self.colonne = 1
        elif self.numero in [2,5,8]:
            self.colonne = 2
        else:
            self.colonne = 3

    def affichage(self):
        pyxel.rect(self.x, self.y, 71, 72, 0)

class Verificateur:
    def verifier_condition_de_victoire(tableau):
        for i in range(3):
            if ((tableau[i][0] and tableau[i][1] and tableau[i][2]) != None
                and tableau[i][0].joueur == tableau[i][1].joueur == tableau[i][2].joueur 
                ):
                    return True
            
        for i in range(3):
            if ((tableau[0][i] and tableau[1][i] and tableau[2][i]) != None
                and tableau[0][i].joueur == tableau[1][i].joueur == tableau[1][i].joueur 
                ):
                    return True
            
        if ((tableau[0][0] and tableau[1][1] and tableau[2][2]) != None
            and tableau[0][0].joueur == tableau[1][1].joueur == tableau[2][2].joueur 
            ):
                return True
        
        if ((tableau[0][2] and tableau[1][1] and tableau[2][0]) != None
            and tableau[0][2].joueur == tableau[1][1].joueur == tableau[2][0].joueur 
            ):
                return True