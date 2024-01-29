import random

# Définir les questions et les réponses pour le quiz
questions = [
    {
        "question": "Quelle équipe a remporté la Coupe du Monde de Rugby 2019?",
        "options": ["Nouvelle-Zélande", "Afrique du Sud", "Angleterre", "Australie"],
        "correct_answer": "Afrique du Sud"
    },
    {
        "question": "Quelle équipe a le plus de victoires dans le Tournoi des Six Nations?",
        "options": ["France", "Angleterre", "Irlande", "Pays de Galles"],
        "correct_answer": "Angleterre"
    },
    {
        "question": "Combien de joueurs sont sur le terrain dans une équipe de rugby lors d'un match standard?",
        "options": ["11", "12", "13", "15"],
        "correct_answer": "15"
    },
    {
        "question": "Quelle équipe a remporté le Top 14 français en 2020-2021?",
        "options": ["Toulouse", "Clermont", "Racing 92", "La Rochelle"],
        "correct_answer": "Toulouse"
    },
    {
        "question": "Quelle nation a remporté le plus de Tournois des Six Nations jusqu'à présent?",
        "options": ["France", "Angleterre", "Irlande", "Pays de Galles"],
        "correct_answer": "Pays de Galles"
    },
    {
        "question": "Quelle équipe a remporté la première Coupe du Monde de Rugby en 1987?",
        "options": ["Nouvelle-Zélande", "Australie", "Afrique du Sud", "France"],
        "correct_answer": "Nouvelle-Zélande"
    },
    {
        "question": "Quelle équipe a remporté le Tournoi des Six Nations en 2021?",
        "options": ["France", "Angleterre", "Irlande", "Pays de Galles"],
        "correct_answer": "Pays de Galles"
    },
    {
        "question": "Combien de points vaut un essai au rugby?",
        "options": ["3 points", "5 points", "7 points", "10 points"],
        "correct_answer": "5 points"
    },
    {
        "question": "Quelle équipe nationale de rugby est surnommée les 'All Blacks'?",
        "options": ["Australie", "Afrique du Sud", "Nouvelle-Zélande", "Angleterre"],
        "correct_answer": "Nouvelle-Zélande"
    },
    {
        "question": "En quelle année a eu lieu la première Coupe du Monde de Rugby?",
        "options": ["1987", "1991", "1995", "2003"],
        "correct_answer": "1987"
    },
    {
        "question": "Quelle équipe a remporté le plus de titres de la Coupe du Monde de Rugby?",
        "options": ["Afrique du Sud", "Nouvelle-Zélande", "Australie", "Angleterre"],
        "correct_answer": "Nouvelle-Zélande"
    },
    {
        "question": "Combien de pays participent au Tournoi des Six Nations?",
        "options": ["4", "5", "6", "7"],
        "correct_answer": "6"
    },
    {
        "question": "Dans quelle ville se trouve le stade Twickenham, célèbre pour le rugby?",
        "options": ["Londres", "Paris", "Dublin", "Édimbourg"],
        "correct_answer": "Londres"
    },
    {
        "question": "Quelle équipe nationale de rugby est surnommée les 'Wallabies'?",
        "options": ["Afrique du Sud", "Australie", "Argentine", "Pays de Galles"],
        "correct_answer": "Australie"
    },
    {
        "question": "Quelle équipe a remporté le Tournoi des Six Nations en 2020?",
        "options": ["France", "Angleterre", "Irlande", "Pays de Galles"],
        "correct_answer": "Angleterre"
    },
    {
        "question": "Qui est le meilleur marqueur d'essais en Coupe du Monde de Rugby?",
        "options": ["Jonah Lomu", "Bryan Habana", "David Campese", "Shane Williams"],
        "correct_answer": "Jonah Lomu"
    },
    {
        "question": "Dans quelle ville se trouve le stade Aviva, utilisé pour les matches du Tournoi des Six Nations?",
        "options": ["Dublin", "Cardiff", "Édimbourg", "Rome"],
        "correct_answer": "Dublin"
    },
    {
        "question": "Quelle équipe a remporté la dernière édition du Tournoi des Six Nations avant la création de l'Écosse en 2000?",
        "options": ["Angleterre", "Irlande", "Pays de Galles", "France"],
        "correct_answer": "Pays de Galles"
    },
    {
        "question": "Quelle équipe a remporté la Coupe du Monde de Rugby en 2015?",
        "options": ["Australie", "Nouvelle-Zélande", "Afrique du Sud", "Angleterre"],
        "correct_answer": "Nouvelle-Zélande"
    },
    {
        "question": "Quelle équipe nationale de rugby est surnommée les 'Springboks'?",
        "options": ["Nouvelle-Zélande", "Australie", "Afrique du Sud", "Argentine"],
        "correct_answer": "Afrique du Sud"
    },
]

# Mélanger les questions pour plus de variété
random.shuffle(questions)

# Initialiser le score du joueur
score = 0

# Fonction pour poser une question et vérifier la réponse
def poser_question(question):
    print(question["question"])
    for i, option in enumerate(question["options"], 1):
        print(f"{i}. {option}")
    
    reponse_joueur = input("Votre réponse (1/2/3/4) : ")
    if reponse_joueur.isdigit() and 1 <= int(reponse_joueur) <= 4:
        index_reponse = int(reponse_joueur) - 1
        if question["options"][index_reponse] == question["correct_answer"]:
            print("Correct !")
            return True
        else:
            print(f"Faux. La réponse correcte était : {question['correct_answer']}")
            return False
    else:
        print("Réponse invalide. Veuillez choisir une option de 1 à 4.")
        return False

# Poser chaque question et mettre à jour le score
for question in questions:
    if poser_question(question):
        score += 1

# Afficher le score final
print(f"Score final : {score}/{len(questions)}")

