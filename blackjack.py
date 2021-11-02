""""
Midterm project for Python Programming. Make a simple blackjack game
"""

__author__ = "Anthony Kanellopoulos"

from random import shuffle
from abc import ABC, abstractmethod
import random
from time import sleep



class Card:
    def __init__(self, face, suit):

        self.face = face
        self.suit = suit
        self.value = face

        if face in ["J", "K", "Q"]:
            self.value = 10
        if face == 'A':
            self.value = 11
        elif face in range(1,10):
            self.value = int(face)



    #we'll need to define how addition works so that we can calculate the value of a hand (made up of two cards) later on
    def __add__(self, other):

        return int(self.value) + int(other.value)

    def __str__(self):
        
        #would be nice to do some formatting here to make the cards look better to the user
        return "\n{} | {}\n ".format(self.face, self.suit)
    
class Deck:

    def __init__(self):

        suits = ["HEARTS", "DIAMONDS", "CLUBS", "SPADES"]
        face = [n for n in range(2, 10)]
        face += ["J", "Q", "K", "A"]


        #using list comprehension to keep compact #not using face values for ease
        self._deck = [Card(value, suit) for suit in suits for value in face]


    def deal(self, hidden = False):
        """"
        Return the top card from the deck. Pop the card from the deck to ensure it does not get dealt again.
        Deals a single card

        Parameters
        ----------
        hidden: bool
            True --> do not print the value of the card
            False --> print the value of the card [deafult] 

        Returns
        -------
        - the top card from the deck
        - prints the value and the suit (if hidden = False)
        """
        
        #debuger to know the number of cards before we deal one
        # print("number of cards is {}".format(len(self._deck)))

        dealt_card = self._deck.pop(0)

        if hidden == False:
            print(dealt_card)
        else:
            print("Card 2 is facing downwards")

        #debugger to show that the number of cards has been reduced by one
        # print("number of cards is {}".format(len(self._deck)))

        return dealt_card
        
    def shuffle(self):
        """
        Shuffle the list of cards that make up the deck

        Parameters
        ----------
        None

        Return
        ------
        - the deck list with cards shuffled
        """

        shuffle(self._deck)

    def print_deck(self):
        for card in self._deck:
            print(card)

    def size(self):
        return len(self._deck)


class Player(ABC):
    """
    Documentation
    - I want the player to have an attribute which is their hand
    """

    def __init__(self) -> None:
        super().__init__()
        self.card1 = None
        self.card2 = None
        self.points = 0
        self.name = None
        self.cards = []
        self.hand = 0
  
    def deal_card(self, deck, Hidden= False):
        new_card = deck.deal(Hidden)
        self.cards.append(new_card)
        
        #calculate the hand
        self.hand += new_card.value
    
    @abstractmethod
    def decide_play(self, deck):
        """
        Documentation
        - decide whether to stay or whether to draw
        """

        
        pass

    @abstractmethod
    def set_name(self):
        
        pass

    def show_name(self):
        print(self.name)

class HumanPlayer(Player):
    
    def __init__(self) -> None:
        super().__init__()
        
    def set_name(self):
        
        self.name = input("Please input player name:\t")
              
    def decide_play(self, deck):
        """"
        Give the player an option to draw a card or stay
        """
       
        print("\nYour hand is {}".format(self.hand))

        while self.hand < 21:

            decision = input("\nWhat would you like to do?\nDRAW [d]\nSTAY [s]\n\n".format(self.hand))
            
            #obviously you must do some input validation here
            if decision == 'd':
                
                self.deal_card(deck)
                print("\nYour hand value is {}\n".format(self.hand))
            
            elif decision == 's':

                print("\nThat may (or may not) have been a wise decision. Only time will tell\n")
                break
                
        if self.hand == 21:
            print("You get a point!")
            self.points += 1
        
        elif self.hand > 21:
            print("sorry, you went bust!")

        input("Press ENTER to move to next player")

        return self.hand

    def __str__(self):
        
        return "You currently have {} points in this game".format(self.score)
        
class ComputerPlayer(Player):
    """
    Computer player plays exactly like the dealer currently
    """
    
    
    def __init__(self) -> None:
        super().__init__()
        self.set_name()
        
    def set_name(self):

        names = ["Jago", "Leroy", "Fabio", "Soren", "Brida", "Aubrie", "Mika", "Roxanne"]
        self.name = random.choice(names)
        
    def decide_play(self, deck):
        """
        Control of dealer player decision

    
        """

        print("{}'s hand is {}".format(self.name, self.hand))

        while self.hand < 17:
            sleep(1)
            print("{}: Hit me!".format(self.name))
            sleep(1.5)
            self.deal_card(deck)
            print("{} has {}".format(self.name, self.hand))
            sleep(1.5)

        
        if self.hand < 21:
            print("I stay")
        
        elif self.hand == 21:
            print("Yipee for me, I have 21!")
        
        elif self.hand >21:
            print("{} is bust".format(self.name))
        sleep (2)

        return self.hand

class Dealer(Player):
    
    def __init__(self) -> None:
        super().__init__()
        
        self.score = 0

    def set_name(self):
        return super().set_name()

    def decide_play(self, deck):
        """
        Control of dealer player decision

    
        """
        
        print("Dealer's cards are")
        for card in self.cards:
            print(card)

        print("The hand is worth {}".format(self.hand))

        #from the third card onwards, we can see the dealer's card immediately
        while self.hand < 17:
            self.deal_card(deck)
            print("Dealer has {}".format(self.hand))

        
        if self.hand < 21:
            print("I stay\n")
        
        elif self.hand == 21:
            print("Yipee for me, I have 21!\n")
        
        elif self.hand >21:
            print("dealer is bust\n")
        
class Game():
    """"
    Initialise a game of blackjack
    automatically add a human player, computer player and of course, always a dealer
    pass the computer player as default=1
    """
    
    def __init__(self, human_player=1, computer_player=1):
        self.human_player = HumanPlayer()
        self.computer_player = ComputerPlayer()
        self.dealer = Dealer()
        self.deck = Deck()
        
        self.human_player_number = human_player
        self.computer_player_number = computer_player
        
        self.players  = []
        
    def introduction_screen(self):
       """"
       This does not interact with any user number - it's just a print screen
       """
       
       #explain to the human player how the game is played, what the rules are and how to interact with the game
       separator = "\n"+"_"*30
       print("\n\nLET'S PLAY BLACKJACK!{}".format(separator))
       sleep(1.5)
       print("\n\nThe aim of the game is simple...get as close to 21 as you can\n")
       sleep(2)
       print("* Each player gets dealt two cards at the start of a round\n* You can choose to draw a card or stay after that \n* Your goal is to get closer to 21 than the dealer does. You want to beat the dealer\n* If you go over 21 you lose a point!\n* If you beat the dealer you get a point \n* If you draw with the dealer you don't lose points\n")
       user_understands = input("Press ENTER to continue\n_______________________________\n")  

    def set_players(self):

        print("First thing's first. Who will be playing? We have {} human players and {} computer players\n".format(self.human_player_number, self.computer_player_number))
        sleep(1)
        #create the players in this loop and ask for names for human players
        print("Let's start with you...humans\n_______________________________\n")

        sleep(1)
        for number in range(self.human_player_number):
            print("For human player {}".format(number+1))
            a = HumanPlayer()
            a.set_name()
            print("\n")
            self.players.append(a)
            sleep(1)

        sleep(1)
        print("ok, thank you\n")
        print("\n_______________________\nNow for our computer players we will have\n\n")
        sleep(2)
        for number in range(self.computer_player_number):
            a = ComputerPlayer()
            print(a.name+"\n")
            self.players.append(a)
            sleep(1)
        
        sleep(2)
        print("__________________________")
        print("Here are all our players:\n")
        for player in self.players:
            print(player.name)

        input("\nPress ENTER to continue\n")

    def dealer_catchphrases(self):

        catch_phrases = ["Winner winner chicken dinner", "Feeling lucky?", "Jesus ... take the wheel!", "Are you fired up?" ]

        return random.choice(catch_phrases)

    def set_the_table(self):
        
        #dealer is shuffling the deck; could also add a nice visual here and add a sleep too
        self.deck.shuffle()
        
        print("\nDealer is dealing the first cards\n")
        sleep(2)

        
        #deal the first card to all players
        for player in self.players:
            print("\n{}\n".format(player.name))

            sleep(1)

            player.deal_card(self.deck)

            sleep(2)
        
        #deal a card for the dealer
        print("\nDEALER")
        self.dealer.deal_card(self.deck)

        print("First round of cards has been dealt. {}\n".format(self.dealer_catchphrases()))
        input("Press ENTER to continue to second round of cards\n_______________________________\n")

        #deal the second round of cards
        for player in self.players:
            
            #show the player their second card
            print("\n{}\n".format(player.name))
            sleep(1)
            print("Card 2")
            player.deal_card(self.deck)
            
            #to remind the player what their first hand was
            print("Card 1")
            print(player.cards[0])
            sleep(2)

        print("\nDEALER\n")
        print("Card 1")
        print(player.cards[0])
        self.dealer.deal_card(self.deck, True)        
    
    def winning_rules(self, player):

        if self.dealer.hand > 21:
            if player.hand >21:
                print("You are bust so is the dealer. Phew!")
            
            if player.hand < 21:
                print("The dealer is bust and you're still in it. Nice one :) ")
                player.points += 1
        
        else:
            if player.hand  > 21:
                print("You are bust and the dealer is still in the game :( You lose a point for that")
                player.points -= 1
            
            elif player.hand > self.dealer.hand:
                print("You beat the dealer! You get a point")
                player.points += 1
            
            elif player.hand == self.dealer.hand:
                print("No points for tying")

            elif player.hand < self.dealer.hand:
                print("The dealer has beat you by {}. That's -1 point".format(abs(self.dealer.hand - player.hand)))
                player.points -= 1
    
    def play(self):
        
        #turn this off for now, to debug faster
        # self.introduction_screen()
        sleep(2)
        self.set_players()
        sleep(2)
            

        while True:

            #dealing the first two cards to all players
            self.set_the_table()

            #now players decide if they want to hit or stay
            #remember --> dealer is not in the list of players
            for player in self.players:
                player.decide_play(self.deck)

    

            #dealer reveals his cards
            print("Let's see, what did the dealer get?\n")
            sleep(1)
    
            self.dealer.decide_play(self.deck)

            print("{}".format(self.human_player.name))
            self.winning_rules(self.human_player)
            sleep(2)

            print("\n{}".format(self.computer_player.name))
            self.winning_rules(self.computer_player)

            #our points are...
            print("\n\nHere's our points tally\n")
            print("{}: {}".format(self.human_player.name, self.human_player.points))
            print("{}: {}".format(self.computer_player.name, self.computer_player.points))
            print("Dealer: {}".format(self.dealer.points))


            x = input("Do you want to play again? Yes [y] or No [n]\n")

            if x == 'y':
                pass
                print("Ok, there are {} cards remaining in the deck".format(self.deck.size()))
            if x == 'n':
                exit


    


def main():
    game = Game(1, 1)
    game.play()
    



if __name__ == "__main__":

    main()
    