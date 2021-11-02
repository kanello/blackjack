""""
Midterm project for Python Programming. Make a simple blackjack game
"""

__author__ = "Anthony Kanellopoulos"

from random import shuffle
from abc import ABC, abstractmethod
import random
from time import sleep




class Card:
    """A card from a standard deck of cards. Ranging from 2-10, incl. A,K,Q,J. 

    Attributes
    ----------
    face: str
        The number or face rank of the card. e.g. K or 4
    value: int
        The number value of a card. From 2-10, the face value is used. K,Q,J are worth 10. A is worth 11
    suit: str
        The suit of a card. Options are [hearts, diamonds, clubs, spades]
    
    """

    def __init__(self, face, suit):
        """Construct a card
        """

        self.face = face
        self.suit = suit
        self.value = face

        if face in ["J", "K", "Q"]:
            self.value = 10
        if face == 'A':
            self.value = 11
        elif face in range(1,10):
            self.value = int(face)

    #we might need to access the ace as either a 1 or an 11
    def flip_ace(self, direction):
        """Allow the game to use the Ace as 1 or 11
        
        Paremeters
        ----------
        direction: str
            Accepts up/down and accordingly sets the Ace card as 1 or 11
        
        """
        if direction == 'up':
            self.value = 11
        elif direction == 'down':
            self.value == 1

    #we'll need to define how addition works so that we can calculate the value of a hand (made up of two cards) later on
    def __add__(self, other):
        """Addition of the values of cards

        Parameters
        ----------
        other: obj
            Another card object, identical object type to the card object in 'self'

        Returns
        -------
        self.value + other.value: int
            Add the value attributes of the current object and another card object. Return the sum
        """
        return int(self.value) + int(other.value)

    #need to override the print so we can use it to show the user what a card was
    def __str__(self):
        """Print the face and suit of a card
        
        Returns
        -------
        str
            Face | Suit of a card
        """
        #would be nice to do some formatting here to make the cards look better to the user
        return "\n{} | {}\n ".format(self.face, self.suit)
    
class Deck:
    """A standard deck of 52 cards. Each card is a Card obj.

    Attributes
    ----------
    _deck: list
        A list of 52 card objects containing all combinations of faces/values and suits

    """
    def __init__(self):
        """Constructs a deck of cards
        """

        suits = ["HEARTS", "DIAMONDS", "CLUBS", "SPADES"]
        face = [n for n in range(2, 10)]
        face += ["J", "Q", "K", "A"]


        #using list comprehension to keep compact #not using face values for ease
        self._deck = [Card(value, suit) for suit in suits for value in face]

    def deal(self, hidden = False):
        """"Deals the top card from the deck. Pop the card from the deck to ensure it does not get dealt again.
        It prints the face of the card and the suit, unless hidden = True (used for dealer's second card)
        

        Parameters
        ----------
        hidden: bool
            True --> do not print the value of the card
            False --> print the value of the card [deafult] 

        Returns
        -------
        dealt_card: obj
            A card obj from the top of the deck. It als
        """
        
        #deal the first card of the deck
        dealt_card = self._deck.pop(0)

        #the dealer's second card must be hidden
        if hidden == False:
            print(dealt_card)
        else:
            print("Card 2 is facing downwards")

        return dealt_card
        
    def shuffle(self):
        """Shuffle the list of cards that make up the deck

        Parameters
        ----------
        None

        Return
        ------
        _deck: list
            The deck list with cards shuffled
        """

        shuffle(self._deck)

    def size(self):
        """Show how many cards remain in the deck

        Parameters
        ----------
        None

        Returns
        -------
        len(_deck): int
            The number of items in the _deck list
        """
        return len(self._deck)

class Player(ABC):
    """Abstract base class representing a player of blackjack

    Atttributes
    -----------
    points: int
        The points accumulated by a player over a number of rounds of blackjack
    
    name: str
        The name of the player. So we can distinguish them and interact with the user
    
    cards: list
        Contains all the cards dealt to a single player

    hand: int
        Calculate the hand of a player. Sums the card.value for each card inside the 'cards' attribute 
    """

    def __init__(self) -> None:
        """Construct the Player
        """
        super().__init__()
        self.points = 0
        self.name = None
        self.cards = []
        self.hand = 0
  
    def deal_card(self, deck, hidden= False):
        """Deals a card to a player


        Parameters
        ----------
        deck: obj
            A deck of cards
        
        hidden: bool
            To hide a dealt card from the users

        Returns
        -------
        cards: list
            list of card objects
        hand: int
            the sum of card values for each card in the list of cards
        """
        
        #pass the hidden through so we can toggle it down the line
        new_card = deck.deal(hidden)
        self.cards.append(new_card)
        
        #calculate the hand
        self.hand += new_card.value
    
    @abstractmethod
    def decide_play(self, deck):
        """Player decision on what to do

        The options are that either the player will draw a card or they will stay
        It should result in either the player staying on a card going bust
        """

        
        pass

    @abstractmethod
    def set_name(self):
        """Set the name of the players
        """
        
        pass

    def show_name(self):
        """Prints the name of a player
        
        Returns
        -------
        name: str
            The name of each player
        """
        print(self.name)

class HumanPlayer(Player):
    """A derived class from Player. Allows a person to control decisions from the console

    Atttributes
    -----------
    points: int
        The points accumulated by a player over a number of rounds of blackjack
    
    name: str
        The name of the player. So we can distinguish them and interact with the user
    
    cards: list
        Contains all the cards dealt to a single player

    hand: int
        Calculate the hand of a player. Sums the card.value for each card inside the 'cards' attribute
    """
    
    def __init__(self) -> None:
        super().__init__()
        
    def set_name(self):
        """Give a name to the human player

        Returns
        -------
        name:str
            Asks the user what name they'd like to give to the Player obj
        """
        
        self.name = input("Please input player name:\t")
              
    def decide_play(self, deck):
        """"A human player decides to stay or draw a card

        Paramters
        ---------
        deck: obj
            The deck that we are playing the game with

        Returns
        -------
        hand: int
            The sum of values of all the cards inside the cards list
        """
       
        #give the user an idea of what they have, so they can make an educated decision
        print("\nYour hand is {}".format(self.hand))

        #the user should can only draw if they are below 21
        while self.hand < 21:

            decision = input("\nWhat would you like to do?\nDRAW [d]\nSTAY [s]\n\n".format(self.hand))
            
            #deal the user a card
            if decision == 'd':
                
                self.deal_card(deck)
                
                #update the user on what their hand is
                print("\nYour hand value is {}\n".format(self.hand))
            
            #user stays
            elif decision == 's':

                print("\nThat may (or may not) have been a wise decision. Only time will tell\n")
                break

        #the user should automatically get a point if they get 21 - their turn ends
        if self.hand == 21:
            print("You get a point!")
            self.points += 1
        
        #inform the user they are bust - their turn ends
        elif self.hand > 21:
            print("sorry, you went bust!")

        #pause until the user confirms they'd like to move on. Feels jarring if things move along quicklu on their own
        input("Press ENTER to move to next player")

        return self.hand

    def __str__(self):
        """Show the user how many points they have accumulated over the rounds

        Returns
        -------
        score: int
            The sum of all the points accumulated over the rounds
        """
        return "You currently have {} points in this game".format(self.score)
        
class ComputerPlayer(Player):
    """A derived class from Player. Decision making can be modified via the decide play method

    Atttributes
    -----------
    points: int
        The points accumulated by a player over a number of rounds of blackjack
    
    name: str
        The name of the player. So we can distinguish them and interact with the user. Gets assigned during contruction
    
    cards: list
        Contains all the cards dealt to a single player

    hand: int
        Calculate the hand of a player. Sums the card.value for each card inside the 'cards' attribute 
    """
    
    
    def __init__(self) -> None:
        super().__init__()
        
        #give the computer player a name during construction
        self.set_name()
        
    def set_name(self):
        """Give the computer player a name
        
        Returns
        -------
        name: str
            Randomly selected from a list of uncommon baby names found here - https://hubbleconnected.com/blogs/news/50-least-and-most-common-baby-names-for-boys-and-girls
        """

        #uncommon baby names
        names = ["Jago", "Leroy", "Fabio", "Soren", "Brida", "Aubrie", "Mika", "Roxanne", "Ingrid", "Archie", "Benedict", "Margo", "Jad", "Harper", "Paola", "Ezra", "Idris"]
        
        #choose randomly
        self.name = random.choice(names)
        
    def decide_play(self, deck):
        """Computer decisions on how to play
        
        Rules: draw until you reach 17, then stop drawing

        Parameters
        ----------
        deck: obj
            The deck of cards we use for the game

        Returns
        -------
        hand: int
            The sum of values of all the cards inside the cards list
        """

        print("{}'s hand is {}".format(self.name, self.hand))

        #set some delays to make the game play easier to follow
        while self.hand < 17:
            sleep(1)
            
            #inform the other players I'll be taking a card
            print("{}: Hit me!".format(self.name))
            sleep(1.5)
            
            self.deal_card(deck)
            
            #tell users what my hand is worth
            print("{} has {}".format(self.name, self.hand))
            sleep(1.5)

        
        if self.hand < 21:
            print("I stay")
        
        elif self.hand == 21:
            print("Yipee for me, I have 21!")
            self.points =+ 1
            
        
        elif self.hand >21:
            print("{} is bust".format(self.name))
        sleep (2)

        return self.hand

class Dealer(Player):
    """A derived class from Player. Decision making can be modified via the decide play method

    Atttributes
    -----------
    points: int
        The points accumulated by a player over a number of rounds of blackjack
    
    name: str
        The name of the player. So we can distinguish them and interact with the user. Gets assigned during contruction
    
    cards: list
        Contains all the cards dealt to a single player

    hand: int
        Calculate the hand of a player. Sums the card.value for each card inside the 'cards' attribute 
    
    """
    
    def __init__(self) -> None:
        super().__init__()
        
        self.score = 0

    def set_name(self):
        """Standard name for dealer

        Returns
        -------
        name: str
            Dealer
        """
        self.name = "Dealer"
        return super().set_name()

    def decide_play(self, deck):
        """A dealer decides to stay or draw a card


        Rules: draw until you reach 17, then stop drawing

        Paramters
        ---------
        deck: obj
            The deck that we are playing the game with

        Returns
        -------
        hand: int
            The sum of values of all the cards inside the cards list
        """

        #dealer reveals their cards
        print("Let's see, what did the dealer get?\n")
        sleep(1)
        
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
    """"Start a game of blackjack.

    Attributes
    ----------
    dealer: obj
        Spin up a dealer
    
    deck: obj
        spin up a deck of cards

    human_player_number: int [default = 1]
        how many human players will we have

    computer_player_number: int [default = 1]
        how many computer players will we have
    
    players: list
        adds the human and computer player objects into a list
    """
    
    def __init__(self, human_player=1, computer_player=1):
        """Construct a game of blackjack
        """
        #add a dealer
        self.dealer = Dealer()
        
        #add a deck
        self.deck = Deck()
        
        #how many humans and computers do we want playing
        self.human_player_number = human_player
        self.computer_player_number = computer_player
        
        self.players  = []

    def refresh_deck(self):
        """spin up a new deck

        Returns
        -------
        deck: obj
            new deck of cards
        """
        self.deck = Deck()

    def introduction_screen(self):
       """"Prints introductory messages to the user
       
       Returns
       -------
       None
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
        """Prepare the blackjack game by spinning up the required players (set by the contructor)


        Parameters
        ----------
        None

        Returns
        -------
        players: list
            players list is populated by the amout of players requested in the constructor
        """

        print("First thing's first. Who will be playing? We have {} human players and {} computer players\n".format(self.human_player_number, self.computer_player_number))
        sleep(1)
        print("Let's start with you...humans\n_______________________________\n")
        sleep(1)

        #create the human players in this loop and ask for names for human players
        for number in range(self.human_player_number):
            print("For human player {}".format(number+1))
            
            #spin up a human player and request a name
            a = HumanPlayer()
            a.set_name()
            print("\n")

            #put them into the players list for later interaction
            self.players.append(a)
            sleep(1)

        sleep(1)
        print("ok, thank you\n")
        print("\n_______________________\nNow for our computer players we will have\n\n")
        sleep(2)
        
        #create computer players in the loop
        for number in range(self.computer_player_number):
            a = ComputerPlayer()
            
            #show the names of the players created
            print(a.name+"\n")

            #add them to the list
            self.players.append(a)
            sleep(1)
        
        sleep(2)
        
        #recap which players are in the game
        print("__________________________")
        print("Here are all our players:\n")
        for player in self.players:
            print(player.name)

        input("\nPress ENTER to continue\n")

    def dealer_catchphrases(self):
        """Silly catchphrases that the dealer can "throw" in the mix

        Returns
        -------
        catchphrase: str
            A string with a predefined catchphrase, randomly selected from the list
        """

        catch_phrases = ["Winner winner chicken dinner", "Feeling lucky?", "Jesus ... take the wheel!", "Are you fired up?" ]

        return random.choice(catch_phrases)

    def set_the_table(self):
        """Set the table by dealing the first two cards to each player

        Loop through the players list and deal them a card. Do that twice. In the second card loop, dealers second card faces down
        Calculate the value of the hand and show it to the users
        
        Returns
        -------
        None
        """
        #dealer is shuffling the deck; could also add a nice visual here and add a sleep too
        self.refresh_deck()
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

        #show what the dealer had
        print("\nDEALER\n")
        print("Card 1")
        print(player.cards[0])

        #dealers second card must always be hidden. Pass True to parameter
        self.dealer.deal_card(self.deck, True)        
    
    def winning_rules(self):
        """Decide who wins the round
        Add all the players into a list and sort by their score. Pick the top score

        Returns
        -------
        None
        """

        #initialise list to be used later
        final_ranking = []

        #add only the non-bust players into the list
        for player in self.players:
            if player.hand < 22:
                each_player = []
                each_player = [player, player.name, player.hand]
            
                final_ranking.append(each_player)

        #add the dealer to the list if they didn't go bust
        if self.dealer.hand <22:
            final_ranking.append([self.dealer, self.dealer.name, self.dealer.hand])

        #order the final ranking list by the hand
        final_ranking = sorted(final_ranking, key= lambda x:x[2], reverse=True)
        
        #select the winner and give them a point
        winner = final_ranking[0][0]
        winner.points +=1 

        print("{} wins!".format(winner.name))
    
    def clean_table(self):
        """Reset the cards and hand values for the next round
        """
        for player in self.players:
            player.hand = 0
        
        self.dealer.hand = 0
        self.dealer.cards = []

    def play(self):
        """Main function running the blackjack game

        Flow
        ----
        * introduce game
        * spawn up the players
        * deal them in
        * they decide to stay or draw
        * determine winner
        * give winner a point
        * ask to play again
        """
        
        #Give the users instructions for how the game is to be played
        self.introduction_screen()
        sleep(2)
        
        #get the user names and create them
        self.set_players()
        sleep(2)

        #main playing loop. Breaks when the user exits after a round
        while True:
            
            #reset everyone's hand value and wipe their cards
            self.clean_table()
            
            #dealing the first two cards to all players
            self.set_the_table()

            #now players decide if they want to hit or stay
            #remember --> dealer is not in the list of players
            for player in self.players:
                player.decide_play(self.deck)
          
            #dealer always plays last
            self.dealer.decide_play(self.deck)

            #now let's tally up scores and decide winners
            self.winning_rules()

            #our points are...
            print("\n\nHere's our points tally\n")
            for player in self.players:

                print("{}: {}".format(player.name, player.points))
            
            #print dealer points below
            print("Dealer: {}".format(self.dealer.points))

            #does the human player want to play again? anyone can answer this
            x = input("Do you want to play again? Yes [y] or No [n]\n")

            if x == 'y':
                pass
                print("Ok, starting up a new deck for you.")
            if x == 'n':
                break
        
        print("\nThanks for playing, see you next time")


    


def main():

    game = Game(human_player=1, computer_player=2)
    game.play()
    



if __name__ == "__main__":

    main()
    