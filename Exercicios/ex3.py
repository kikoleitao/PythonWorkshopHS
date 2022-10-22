from random import randrange

class Dice:
    sides = 6
    top_side = 1
    def __init__(self, sides):
        self.sides = sides
        self.top_side = self.roll()

    def __str__(self):
        return f"{self.top_side} em {self.sides} possíveis"
        #ou (pior)
        #return str(self.top_side) + " em " + str(self.sides) + " possíveis."

    def roll(self):
        self.top_side = randrange(1, self.sides+1)
our_dice = Dice(20)
our_dice.roll()
print(our_dice.top_side)
print(our_dice)