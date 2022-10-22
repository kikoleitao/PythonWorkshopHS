from random import choices
simbols = ["#", "$", "%", "&", "@", "£", "€"]
weights = [50/156, 40/156, 30/156, 20/156, 10/156, 5/156, 1/156]


""" Francisco Leitão, 103898
Slot Machine:
1. Quando iniciada pergunta ao utilizador quantos créditos quer depositar;

2. Antes de cada rodada pergunta ao utilizador se quer parar de jogar;

3. Se a decisao for para continuar pergunta quantos créditos vão ser
apostados, se não houver créditos suficientes o jogador é informado e repete-se a pergunta;

4. Uma Rodada consiste em gerar 3 simbolos de um conjunto de 7 símbolos ("#", "$", "%", "&", "@", "£", "€");

5. Os simbolos têm as seguintes probabilidades:
#: 50/156; $: 40/156; %:30/156; &: 20/156; @: 10/156; £: 5/156; €: 1/156;

6. Se os 3 símbolos forem iguais então o utilizador ganha créditos em função da sua aposta e do simbolo que aposta:
#: 5 * aposta; $: 10 * aposta; %: 20 * aposta; &: 70 * aposta; @: 200 * aposta; £: 1000 * aposta; €: 100_000 * aposta;

7. Se o utilizador ficar sem créditos acaba o programa
"""


class Player:
    credits = 0.0
    def __init__(self, credits):
        self.credits = credits


def play(player):
    """
    Plays until player wants or until he's out of credits
    """
    keep_playing_answer = keep_playing(player)
    while(keep_playing_answer and player.credits > 0):
        answer = input("How many credits do you want to bet?")
        while(not_valid_entry(answer) or float(answer) > player.credits):
            print("Invalid answer")
            answer = input("How many credits do you want to bet?")
        bet = float(answer)
        round(player, bet)
        keep_playing_answer = keep_playing(player)
        

def keep_playing(player):
    """
    Asks the player if he wants to keep playing: (Yes/yes) or (No/no)
    """

    keep_playing_question = input("Do you wanna keep playing? (Yes/No)")
    match(keep_playing_question.lower()):
        case "yes":
            return True
        case "no":
            return False
        case _:
            print("Wrong input")
            return keep_playing(player)
            

def round(player, bet):
    """
    Spins the three wheels and updates player's credits
    """
    player.credits -= bet

    firstWheel = choices(simbols, weights) 
    secondWheel = choices(simbols, weights)
    thirdWheel = choices(simbols, weights)
    wheels = firstWheel + secondWheel + thirdWheel
    print(*wheels, sep = "  ||  ")
    if(firstWheel == secondWheel == thirdWheel):
        match(wheels[0]):
            case "#":
                player.credits += 5 * bet
            case "$":
                player.credits += 10 * bet
            case "%": 
                player.credits += 20 * bet
            case "&":
                player.credits += 70 * bet
            case "@":
                player.credits += 200 * bet
            case "£":
                player.credits += 1000 * bet
            case "€":
                player.credits += 100_000 * bet
        print(f"You won! You have now {player.credits}$")
    else:
        print(f"You lost... You have now {player.credits}$")
    

def not_valid_entry(answer):
    return (not answer.isdigit()) or float(answer) <= 0


print("Welcome to HackerSchool's Slot Machine! :)")
answer = input("How many credits would you like to deposit?")
while(not_valid_entry(answer)):
    print("Invalid answer")
    answer = input("How many credits would you like to deposit?")
ini_credits = float(answer)
player = Player(ini_credits)
play(player)
