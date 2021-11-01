""""
Midterm project for Python Programming. Make a simple blackjack game
"""

__author__ = "Anthony Kanellopoulos"

from random import shuffle
from abc import ABC, abstractmethod


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


    
    @abstractmethod
    def decide_play(card1, card2):
        """
        Documentation
        - decide whether to stay or whether to draw
        """
        pass

class HumanPlayer(Player):
    
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
          
        
    def decide_play(self, deck, card1, card2):
        """"
        Give the player an option to draw a card or stay
        """

        hand = card1 + card2

        print("Your hand is {}".format(hand))

        while hand < 21:

            decision = input("\nWhat would you like to do?\nDRAW [d]\nSTAY [s]\n".format(hand))
            
            #obviously you must do some input validation here
            if decision == 'd':
                
                card = deck.deal()
                hand += card.value

                print("Your hand value is {}".format(hand))
            
            elif decision == 's':

                print("That may (or may not) have been a wise decision. Only time will tell")
                break
                

        if hand == 21:
            print("You get a point!")
            self.score += 1
        
        elif hand > 21:
            print("sorry, you went bust!")
            #kick the player out of the game

        return hand
        


    def __str__(self):
        
        return "You currently have {} points in this game".format(self.score)
        
class ComputerPlayer(Player):
    """
    Computer player plays exactly like the dealer currently
    """
    
    
    def __init__(self) -> None:
        super().__init__()
        
        self.score = 0

    def decide_play(self, deck, card1, card2):
        """
        Control of dealer player decision

    
        """

        hand = card1 + card2
        print("computer's hand is {}".format(hand))

        while hand < 17:
            new_card = deck.deal()
            hand += new_card.value
            print("computer has {}".format(hand))

        
        if hand < 21:
            print("I stay")
        
        elif hand == 21:
            print("Yipee for me, I have 21!")
        
        elif hand >21:
            print("computer is bust")

        

        return hand

class Dealer(Player):
    
    def __init__(self) -> None:
        super().__init__()
        
        self.score = 0

    def decide_play(self, deck, card1, card2):
        """
        Control of dealer player decision

    
        """

        hand = card1 + card2
        print("Dealer's hand is {}".format(hand))

        while hand < 17:
            new_card = deck.deal()
            hand += new_card.value
            print("Dealer has {}".format(hand))

        
        if hand < 21:
            print("I stay")
        
        elif hand == 21:
            print("Yipee for me, I have 21!")
        
        elif hand >21:
            print("dealer is bust")

        

        return hand

class Game():
    """"
    Initialise a game of blackjack
    automatically add a human player, computer player and of course, always a dealer
    pass the computer player as default=1
    """
    
    def __init__(self, human_player=1, computer_player=1):
        self.human_player = HumanPlayer()

        for i in range(computer_player):
            ComputerPlayer()
        
        self.dealer = Dealer()
        

    def play():
        
        #create a deck
        deck = Deck()

        #shuffle the deck

        #deal first card to all players facing up

        #deal second card to all players, dealer's facing down

        #human player plays

        #computer player plays

        #dealer reveals his cards
        #dealer plays

        #keep score of what happens

        #ask if the player wants to play again
        

        

    def


def main():

    deck = Deck()
    # deck.print_deck()
    deck.shuffle()
    # deck.print_deck()


    player_1 = HumanPlayer()
    dealer = Dealer()
    com = ComputerPlayer()
    player_1.decide_play(deck, deck.deal(), deck.deal())
    com.decide_play(deck, deck.deal(), deck.deal())
    dealer.decide_play(deck, deck.deal(), deck.deal())

    print(deck.size())



if __name__ == "__main__":

    main()