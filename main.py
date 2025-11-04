"""Module -> Quizify: Gestion des questions et des quiz"""


__author__ = "sales_r"


from tabulate import tabulate
from quiz import Banque_questions
from user import UserStore
from datetime import date
from utils import clear
import time


if __name__ == "__main__":
    banque = Banque_questions.charger_questions("data/questions.json")
    print("Nombre de questions chargées:", len(banque.questions))
    banque_users = UserStore("data/utilisateurs.json")

    clear()
    nom_utilisateur = input("Quel est votre nom d'utilisateur ?")
    print(f"Bonjour {nom_utilisateur} !")

    while True:
        clear()
        print("\n-|_|-|_|-|_|-|_|-|_|-|_| MENU PRINCIPAL -|_|-|_|-|_|-|_|-|_|-|_| \n")
        print("--- 1: Jouer ----- 2: Scores ----- 3: Quitter :( ---\n")
        choix_menu = input("Faites votre choix (numero): ")
        while choix_menu not in ["1", "2", "3"]:
            print("Vous devez choisir un nombre correspondant a une action")
            choix_menu = input("Votre choix (numero): ")

        if choix_menu == "1":
            themes = banque.lister_theme()
            print("choisissez un theme :\n")
            for i, theme in enumerate(themes, start=1):
                print(f"{i}: {theme}\n")
            choix = input("Votre choix (numero): ")
            nbr_themes = len(themes)
            while not choix.isdigit() or int(choix) not in range(1, nbr_themes + 1):
                print("Vous devez choisir un nombre correspondant a un theme")
                choix = input("Votre choix (numero): ")
            theme_choisi = themes[int(choix) - 1]
            print(f"Vous avez chosi le theme : {theme_choisi}")


            print("pour quitter le jeu taper 0 en reponse et valide")


            question_theme = banque.question_par_theme(theme_choisi)
            nbr_questions = 0
            score = 0
            for q in question_theme:
                print(f"{q.question} \n")
                count = 1
                nbr_questions += 1
                for o in q.options:
                    print(f"Option {count}: {o}")
                    count += 1
                reponse_client = input("Choisissez votre reponse (numero): ")
                while reponse_client not in ["1", "2", "3", "4", "0"]:
                    print("Vous devez choisir un nombre correspondant a une reponse, ou 0")
                    reponse_client = input("Votre choix (numero): ")
                if reponse_client == "0":
                    print("Merci, au revoir !")
                    break
                
                print(f"Vous avez choisi : {q.options[int(reponse_client) - 1]}")
                if q.reponse == q.options[int(reponse_client) - 1]:
                    print("Bravo, bonne reponse")
                    score += 1
                else:
                    print(f"Dommage .. La reponse etait : {q.reponse}")
                print(f"Votre score est de : {score} \n")

            if nbr_questions > 1:
                score_pc = (score / nbr_questions) * 100
                if score_pc >= 50:
                    print(f"Bravo champion ! \nScore final {score_pc}% de bonnes reponses")
                else:
                    print(f"{score_pc}% de bonne reponse ? \nPas ouf la perf ... ")

                print("Sauvegarde en cours ...")

                today = date.today().isoformat()
                banque_users.ajouter_score(nom_utilisateur, theme_choisi, score_pc, today)
                banque_users.sauvegarder()
                print("Score sauvegarde !")
                input("Appuyer sur Entree pour revenir au menu..")
            else:
                clear()
                print("Vous avez quitte avant la ppremiere question : \n Aucune sauvegarde")
                input("Appuyer sur Entree pour revenir au menu..")

        elif choix_menu == "2":
            for u in banque_users.users:
                count = 0
                accumulateur = 0
                data_tableau = []
                if u == nom_utilisateur:
                    for p in banque_users.users[u]["scores"]:
                        count += 1
                        accumulateur += p["score"]
                        partie = []
                        partie.append(count)
                        partie.append(p["theme"])
                        partie.append(p["score"])
                        partie.append(p["date"])
                        data_tableau.append(partie)
                    print(tabulate(data_tableau, headers=["Numero", "Themes", "Scores", "date"]))
                    if count > 0:
                        score_moyen = accumulateur / count
                        print(f"Score moyen: {score_moyen} \n")
                    input("Appuyer sur Entree pour revenir au menu ..")
                        
        elif choix_menu == "3":
            clear()
            print(f"Merci {nom_utilisateur}, A bientot !")
            break

        
  