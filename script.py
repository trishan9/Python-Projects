import os

projects = ["BMI-Calculator", "Love-Calculator", "PizzaBill-Calculator", "Treasure-Finding-Game", "Password-Generator", "Rock-Paper-Scissors", "Hangman-Game", "Kaun-Banega-Crorepati", "Auction", "BlackJack-Game", "Calculator", "Guess-The-Number", "Coffee-Machine", "Higher-Lower-Game", "Secret-Code", "Quiz-Game-OOP", "Turtle-Racing-Game"]

for project in projects:
    if not os.path.exists(project):
        os.mkdir(f"{project}")