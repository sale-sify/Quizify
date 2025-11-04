"""Module -> Quizify: Gestion des questions et des quiz"""


__author__ = "sales_r"


import json


class UserStore:
    """Defnie l'ensemble des utilisateurs"""
    def __init__(self, fichier: str):
        """
        Definie les utilisateurs
        params :
            fichier type str
        """
        self.fichier = fichier
        self.users = self.charger_utilisateurs()

    def charger_utilisateurs(self):
        """Charge un utilisateur et ses donnees"""
        try:
            with open(self.fichier, "r", encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def ajouter_score(self, user: str, theme: str, score: int, date: str):
        """
        Ajoute un score au users
        4 params: 
            user type str
            theme type str
            score type int
            date type str
        """
        if user not in self.users:
            self.users[user] = {"scores": []}
        self.users[user]["scores"].append(
            {
                "theme": theme,
                "score": score,
                "date": date
            }
        )

    def sauvegarder(self):
        """Enregistre les score dans le fichier JSON"""
        try:
            with open(self.fichier, "w", encoding="utf-8") as f:
                json.dump(self.users, f, ensure_ascii=False, indent=2)
        except FileNotFoundError:
            return "Erreur, le fichier est introuvable"


    