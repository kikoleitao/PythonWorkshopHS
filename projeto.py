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
    credits = 0
    def __init__(self, credits):
        self.credits = credits


    def play(self):
        """
        Plays until player wants or until he's out of credits
        """
        while(self.keep_playing() and self.credits > 0):
            answer_bet = input("How many credits do you want to bet?")
            while(invalid_credit_answer(answer_bet) or int(answer_bet) > self.credits):
                print("Invalid answer")
                answer_bet = input("How many credits do you want to bet?")
            self.round(int(answer_bet))
            

    def keep_playing(self):
        """
        Asks the player if he wants to keep playing: (Yes/yes) or (No/no)
        """
        answer = input("Do you wanna keep playing? (Yes/No)")
        while invalid_keep_playing_answer(answer):
            print("Wrong input")
            answer = input("Do you wanna keep playing? (Yes/No)")

        match(answer.lower()):
            case "yes":
                return True
            case "no":
                return False
                

    def round(self, bet):
        """
        Spins the three wheels and updates player's credits
        """
        self.credits -= bet

        firstWheel = choices(simbols, weights) 
        secondWheel = choices(simbols, weights)
        thirdWheel = choices(simbols, weights)
        print(firstWheel[0],secondWheel[0],thirdWheel[0], sep = "   ||   " )
        if(firstWheel == secondWheel == thirdWheel):
            match(firstWheel[0]):
                case "#":
                    self.credits += 5 * bet
                case "$":
                    self.credits += 10 * bet
                case "%": 
                    self.credits += 20 * bet
                case "&":
                    self.credits += 70 * bet
                case "@":
                    self.credits += 200 * bet
                case "£":
                    self.credits += 1000 * bet
                case "€":
                    self.credits += 100_000 * bet
            print(f"You won! You have now {self.credits}$")
        else:
            print(f"You lost... You have now {self.credits}$")
        

def invalid_credit_answer(answer):
    """
    Auxiliar function to play method:
    returns true if answer is not numeric or negative
    """
    return (not answer.isdigit()) or int(answer) <= 0

def invalid_keep_playing_answer(answer):
    """
    Auxiliar function to keep_playing method:
    returns true if answer is not Yes/yes or No/no
    """
    return answer.lower() not in ["yes", "no"]



print("Welcome to HackerSchool's Slot Machine! :)")
answer_credits = input("How many credits would you like to deposit?")
while(invalid_credit_answer(answer_credits)):
    print("Invalid answer")
    answer_credits = input("How many credits would you like to deposit?")
player = Player(int(answer_credits))
player.play()
