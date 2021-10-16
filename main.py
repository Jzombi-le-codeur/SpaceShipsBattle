"""Importer les bibliothèques/modules"""
import pygame  # Importer la bibliothèque Pygame
from game import *

resolution = (1280, 720)  # Défiir la résolution

if __name__ == "__main__":  # Exécuter quand le fihier est lancé
    Game(resolution)  # Lancer la classe Game
