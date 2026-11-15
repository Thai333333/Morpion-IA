import pyxel
import Class

class App:
    def __init__(self):
        pyxel.init(256,256)
        pyxel.load("Assemblage.pyxres")

        self.jeu = True

        self.grille = Class.Grille()
        self.liste_formes = []

        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        pyxel.cls(15)

        if self.jeu:
            self.grille.affichage()

App()