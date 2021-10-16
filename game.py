"""Importer les bibliothèques/modules"""
import pygame  # Importer la bibliothèque Pygame

"""Définir la classe Game"""


class Game:  # Créer la classe Game
    def __init__(self, res):  # Définir les attributs de la classe Game
        self.res = res  # Définir la résolution de la fenêtre
        self.title = "SpaceShips Battle"  # Définir le titre de la fenêtre
        self.clock = pygame.time.Clock()  # Définir la clock du jeu
        self.is_running = True  # Signaler que le jeu est lancé
        self.start()  # Initialiser le jeu

    def start(self):  # Définir la méthode pour initialiser le jeu
        pygame.init()  # Lancer Pygame
        self.screen = pygame.display.set_mode(self.res)  # Créer une fenêtre
        pygame.display.set_caption(self.title)
        self.run()  # Lancer le jeu

    def run(self):  # Définir la méthode pour lancer le jeu
        while self.is_running:  # Répéter tant que le jeu est lancé
            for event in pygame.event.get():  # Signaler l'évènement
                self.manage_event(event)  # Géréer l'évènement
            self.update()  # Mettre à jour le jeu
        self.quit()

    def manage_event(self, event):  # Définir la méthode pour gérer les évènements
        if event.type == pygame.QUIT:  # Vérifier si le joueur veut quitter
            self.is_running = False  # Stopper le jeu

    def update(self):  # Définir la méthode pour mettre à jour le jeu
        self.screen.fill(50)  # Définir la couleur de la fenêtre
        self.clock.tick(50)  # Définir les fps
        pygame.display.update()  # Mettre à jour le jeu

    def quit(self):  # Définir la méthode pour quiter le jeu
        pygame.quit()  # Fermer Pygame
