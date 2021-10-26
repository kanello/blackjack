""""
Midterm project for Python Programming. Make a simple backgammon game
"""

__author__ = "Anthony Kanellopoulos"

from random import shuffle



class Card:
    def __init__(self, value, suit):

        self.value = value
        self.suit = suit

        

    def __str__(self) -> str:
        
        #would be nice to do some formatting here to make the cards look better to the user
        return "\n{}\n------\n{}\n".format(self.suit, self.value)




class Deck:

    def __init__(self):

        suits = ["hearts", "diamonds", "clubs", "spades"]


        #using list comprehension to keep compact #not using face values for ease
        self._deck = [Card(value, suit) for suit in suits for value in range(1,14)]


    def deal(self, hidden = False):
        """"
        Return a random card from the deck. Pop the card from the deck to ensure it does not get dealt again

        Parameters
        ----------
        hidden: bool
            True --> do not print the value of the card
            False --> print the value of the card [deafult] 

        Returns
        -------
        - a random card from the deck
        - prints the value and the suit
        """

        pass


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


def main():

    deck = Deck()
    deck.print_deck()
    deck.shuffle()
    deck.print_deck()


if __name__ == "__main__":

    main()