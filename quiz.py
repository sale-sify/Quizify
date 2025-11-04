"""Module -> Quizify: Gestion des questions et des quiz"""


__author__ = """sales_r"""


import json


class Question:
    """Definie la classe de l'ensemble des questions"""
    def __init__(self,
                 id: int,
                 theme: str,
                 question: str,
                 options: list,
                 reponse: str
                 ):
        """
        Definie les caracteristiques des questions
        5 params :
        id type int
        theme type str
        question type str
        options type str
        reponse type str
        """
        self.id = id
        self.theme = theme
        self.question = question
        self.options = options
        self.reponse = reponse


class Banque_questions:
    """definie une liste d'objet question et la garde en memoire"""
    def __init__(self, questions):
        """
        Definie les caracteristiques des questions
        1 params :
        questions type liste d'objets
        """
        self.questions = questions

    @classmethod
    def charger_questions(cls, fichier: str):
        """
        Definie les caracteristiques des questions
        1 params :
        fichiers type str
        """
        try:
            with open(fichier, "r", encoding="utf-8") as f:
                donnees = json.load(f)
        except Exception as e:
            print("erreur de chargement du fichier JSON : ", e)
            return cls([])
        questions = []
        for i in donnees:
            q = Question(
                id=i["id"],
                theme=i["theme"],
                question=i["question"],
                options=i["options"],
                reponse=i["reponse"]
            )
            questions.append(q)
        return cls(questions)

    def lister_theme(self):
        """Liste les themes des questions de la banque"""
        themes = set()
        for q in self.questions:
            if q.theme not in themes:
                themes.add(q.theme)
        return list(themes)
    
    def question_par_theme(self, theme: str):
        """Lister toutes les questions d'un theme"""
        banque_theme = []
        for q in self.questions:
            if theme == q.theme:
                banque_theme.append(q)
        return banque_theme


if __name__ == "__main__":
    q = Question(1, "Test", "Ceci est une question ?", ["oui", "non"], "oui")
    print(q.theme)
    print(q.options)
