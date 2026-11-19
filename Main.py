import pyxel
import Class
import random

class App:
    def __init__(self):
        pyxel.init(256,256)
        pyxel.load("Assemblage.pyxres")

        self.jeu = True

        self.grille = Class.Grille()
        self.tableau_formes : list[list[Class.Forme]] = [[None, None, None],
                                                         [None, None, None],
                                                         [None, None, None]
                                                         ]
        self.liste_case : list[Class.Case] = []

        for i in range (9):
            self.liste_case.append(Class.Case(i+1))

        self.tour_joueur = random.choice([1,2])

        pyxel.run(self.update, self.draw)

    def update(self):
        for case in self.liste_case:
            case.position()
            case.ligne_et_colonne()
            if case.est_clique() and self.tableau_formes[case.ligne-1][case.colonne-1] == None:
                self.tableau_formes[case.ligne-1][case.colonne-1] = (Class.Forme(self.tour_joueur,case.ligne,case.colonne))
                self.tour_joueur = sum(self.tour_joueur == 1
                                       for i in range(1)) + 1

        for liste_forme in self.tableau_formes:
            for forme in liste_forme:
                if not forme == None:
                    forme.position()

        if Class.Verificateur.verifier_condition_de_victoire(self.tableau_formes):
            print("gagné")

    def draw(self):
        pyxel.cls(15)
        pyxel.mouse(True)

        for case in self.liste_case:
            case.affichage()

        if self.jeu:
            self.grille.affichage()

        for liste_forme in self.tableau_formes:
            for forme in liste_forme:
                if not forme == None:
                    forme.affichage()

App()