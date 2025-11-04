"""Module -> Quizify: Gestion des questions et des quiz"""


__author__ = "sales_r"


import os


def clear():
    """Nettoie l'écran du terminal (Windows / Mac / Linux)"""
    os.system('cls' if os.name == 'nt' else 'clear')