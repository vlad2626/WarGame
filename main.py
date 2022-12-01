import random
from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 11 12 13 14'.split()


class Card:

    def __init__(self):
        self.deck = [(value, color) for value in RANKS for color in SUITE]

    def __str__(self):
        return "deck is {}".format(self.deck)

    def shuffle(self):
       return shuffle(self.deck)

    def cut(self):
        return self.deck[:26],self.deck[26:]
    def getSize(self):
        return len(self.deck)
    def getNextCard(self):
        return self.deck.pop()

    #returns a list of 7 cards
    def initialHand(self):
        Hand = []
        for i in range(6):
            card = self.deck.pop()
            Hand.append(card)
        return Hand



class Hand:
    def __init__(self, numCard):
        self.numCard= numCard

    def addCard(self):
        pass

deck = Card()
def main():
    player1= input("Enter player 1 :")
    player2 = "AI"
    deck = Card()
    deck.shuffle()
    player1Hand= deck.initialHand()
    player2Hand= deck.initialHand()
    playGame(player1Hand, player2Hand)




def playGame(player1Hand, player2Hand):
    numCards1 = len(player1Hand)-1
    numCards2 = len(player2Hand)-1
    score1=0
    score2=0
    field = []

    while (deck.getSize() > 10):
        print("Player 1 hand"+str(player1Hand))

        if(len(player1Hand)) ==0 and deck.getSize() >14:
            player1Hand = deck.initialHand()
            player2Hand = deck.initialHand()
        if  deck.getSize() < 14:
            if score1 > score2:
                print("winner is player 1" + str(score1) + "\n" + " player 2 had " + str(score2))
            else:
                print("Winner is player 2" + str(score2) + "\n" + " player 1 had " + str(score1))

        userAnswer= input("Which card you would like to play( Index)")
        field.append(player1Hand[int(userAnswer)])
        del player1Hand[int(userAnswer)]

        play2 = random.randint(0, len(player2Hand)-1)
        print("Player 2 hand" + str(player2Hand))
        field.append(player2Hand[play2])
        del player2Hand[play2]



        winner =compare(field)
        if winner=="Player1":
            score1 += 1
        else:
            score2 += 1


def compare(field):
    num1= field[0][0]
    num2 = field[1][0]
    if num1 > num2:
        return"Player1"
    else:
        return"Player2"
main()