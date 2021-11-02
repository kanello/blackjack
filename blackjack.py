""""
Midterm project for Python Programming. Make a simple blackjack game
"""

__author__ = "Anthony Kanellopoulos"

from random import shuffle
from abc import ABC, abstractmethod
import random
from time import sleep
import os


class Card:
    def __init__(self, value, suit):

        self.value = value
        self.suit = suit


    #we'll need to define how addition works so that we can calculate the value of a hand (made up of two cards) later on
    def __add__(self, other):

        return self.value + other.value    

    def __str__(self) -> str:
        
        #would be nice to do some formatting here to make the cards look better to the user
        return "\n|{}|\n------\n{}\n".format(self.suit, self.value)
    
class Deck:

    def __init__(self):

        suits = ["hearts", "diamonds", "clubs", "spades"]


        #using list comprehension to keep compact #not using face values for ease
        self._deck = [Card(value, suit) for suit in suits for value in range(1,14)]


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
            print("Card is facing downwards")

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

class Hand:
    """
    This class will deal with all operations relating to a dealt hand
    - addition of cards
    - comparing hands to each other
    """

    def __init__(self, card1, card2):
        """
        
        """
        
        self.hand = card1.value + card2.value

    def highest_hand (self, other):
        """
        take multiple hands as input here
        try and get it to return the winning hand
        """

        if self.hand > other.hand:
            
            print("{} wins".format(self))

            return self
        
        if self.hand < other.hand:
            print("{} wins".format(other))
            return other
        
        else:
            print("it's a tie!")

        



    def __str__(self):
        return "{}".format(self.hand)

class Player(ABC):
    """
    Documentation
    - I want the player to have an attribute which is their hand
    """

    def __init__(self) -> None:
        super().__init__()
        card1 = 0
        card2 = 0
        self.hand = card1 + card2
        self.points = 0


    
    @abstractmethod
    def decide_play(self, deck):
        """
        Documentation
        - decide whether to stay or whether to draw
        """

        
        pass

class HumanPlayer(Player):
    
    def __init__(self) -> None:
        super().__init__()
              
    def decide_play(self, deck):
        """"
        Give the player an option to draw a card or stay
        """
       
        
        #ensure that the player is in the game
        self.hand = self.card1 + self.card2
        
        
        print("Your hand is {}".format(self.hand))

        while self.hand < 21:

            decision = input("\nWhat would you like to do?\nDRAW [d]\nSTAY [s]\n\n".format(self.hand))
            
            #obviously you must do some input validation here
            if decision == 'd':
                
                card = deck.deal()
                self.hand += card.value

                print("\nYour hand value is {}\n".format(self.hand))
            
            elif decision == 's':

                print("\nThat may (or may not) have been a wise decision. Only time will tell\n")
                break
                

        if self.hand == 21:
            print("You get a point!")
            self.points += 1
        
        elif self.hand > 21:
            print("sorry, you went bust!")

        return self.hand

    def __str__(self):
        
        return "You currently have {} points in this game".format(self.score)
        
class ComputerPlayer(Player):
    """
    Computer player plays exactly like the dealer currently
    """
    
    
    def __init__(self) -> None:
        super().__init__()
        

    def decide_play(self, deck):
        """
        Control of dealer player decision

    
        """

        self.hand = self.card1 + self.card2
        print("computer's hand is {}".format(self.hand))

        while self.hand < 17:
            new_card = deck.deal()
            self.hand += new_card.value
            print("computer has {}".format(self.hand))

        
        if self.hand < 21:
            print("I stay")
        
        elif self.hand == 21:
            print("Yipee for me, I have 21!")
        
        elif self.hand >21:
            print("computer is bust")

        

        return self.hand

class Dealer(Player):
    
    def __init__(self) -> None:
        super().__init__()
        
        self.score = 0

    def decide_play(self, deck):
        """
        Control of dealer player decision

    
        """

        self.hand = self.card1 + self.card2
        print("Dealer's hand is {}\n".format(self.hand))

        while self.hand < 17:
            new_card = deck.deal()
            self.hand += new_card.value
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

    def introduction(self):
        #initialise our playing deck
        self.deck.shuffle()

        #give some nice UI instructions for what's going to happen
        separator = "\n"+"_"*30
        print("\n\nLET'S PLAY BLACKJACK!{}".format(separator))
        sleep(1.5)
        print("\n\nThe aim of the game is simple...get as close to 21 as you can\n")
        sleep(2)
        print("* Each player gets dealt two cards at the start of a round. \n* Your goal is to get closer to 21 than the dealer does.\n* If you go over 21 you lose!\n")
        user_understands = input("Press ENTER to continue\n")
    
    def dealer_catchphrases(self):

        catch_phrases = ["Winner winner chicken dinner", "Feeling lucky?", "Jesus ... take the wheel!", "Are you fired up?" ]

        return random.choice(catch_phrases)

    def set_the_table(self):
        print("\nDealer is dealing the first cards\n")
        sleep(2)

        print("HUMAN")
        self.human_player.card1 = self.deck.deal()
        
        sleep(3)

        print("COMPUTER")
        self.computer_player.card1 = self.deck.deal()
        sleep(3)

        print("DEALER")
        self.dealer.card1 = self.deck.deal()
        sleep(2)

        print("First round of cards has been dealt. {}\n".format(self.dealer_catchphrases()))
        input("Press ENTER to continue to second round of cards\n")

        #deal second card, facing up for all except for dealer
        print("Dealing the second card\n")
        sleep(1)
        print("HUMAN")
        print(self.human_player.card1)
        self.human_player.card2 = self.deck.deal()
        sleep(3)

        print("COMPUTER")
        print(self.computer_player.card1)
        self.computer_player.card2 = self.deck.deal()
        sleep(3)

        print("DEALER")
        print(self.dealer.card1)
        self.dealer.card2 = self.deck.deal(hidden=True)
        sleep(3)

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
        

        self.introduction()
        sleep(2)
            
        separator = "\n"+"_"*30
        print(separator)

        while True:

            #dealing the first two cards to all players
            self.set_the_table()

            #now players decide if they want to hit or stay
            self.human_player.decide_play(self.deck)
            self.computer_player.decide_play(self.deck)

            #dealer reveals his cards
            print("Let's see, what did the dealer get?\n")
            sleep(1)
            print(self.dealer.card1)
            print(self.dealer.card2)
            self.dealer.decide_play(self.deck)

            print("HUMAN")
            self.winning_rules(self.human_player)
            sleep(2)

            print("\nCOMPUTER")
            self.winning_rules(self.computer_player)

            #our points are...
            print("\n\nHere's our points tally\n")
            print("Human: {}".format(self.human_player.points))
            print("Computer: {}".format(self.computer_player.points))
            print("Dealer: {}".format(self.dealer.points))


            x = input("Do you want to play again? Yes [y] or No [n]\n")

            if x == 'y':
                pass
                print("Ok, there are {} cards remaining in the deck".format(self.deck.size()))
            if x == 'n':
                exit


        
        


        
        
        
    
                

        

        #compare cards with whoever is still in the game

        #keep score of what happens

        #ask if the player wants to play again
        

    


def main():
    game = Game()
    game.play()
    



if __name__ == "__main__":

    main()
    