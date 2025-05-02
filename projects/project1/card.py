from dataclasses import dataclass
from enum import Enum
import random
from datastructures.bag import Bag

class CardSuit(Enum):
    HEARTS = "❤️"
    SPADE = "♠️"
    CLUBS = "♣️"
    DIAMONDS = "♦️"

class CardFace(Enum):
    ONE = "1"
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE = "5"
    SIX = "6"
    SEVEN = "7"
    EIGHT = "8"
    NINE = "9"
    TEN = "10"
    JACK = "J"
    QUEEN = "Q"
    KING = "K"
    ACE = "A"

    def face_value(self) -> int:
        match self:
            case CardFace.JACK | CardFace.QUEEN | CardFace.KING:
                return 10
            case CardFace.ACE:
                return 11
            case _:
                return int(self.value)

@dataclass
class Card:
    face: CardFace
    suit: CardSuit

@dataclass
class MultiDeck:
    def __init__(self, num_decks: int):
        self.cards = Bag()
        self.num_decks = num_decks
        self.initialize_deck()

    def initialize_deck(self):
        deck = [Card(face, suit) for _ in range(self.num_decks)
            for suit in CardSuit for face in CardFace]
        random.shuffle(deck)
        for card in deck:
            self.cards.add(card)

    def draw_card(self):
        if len(self.cards) == 0:
            raise ValueError("The deck is empty")
        card = random.choice(list(self.cards.bag_dict.keys()))
        self.cards.remove(card)
        return card
    
@dataclass
class Game:
    def __init__(self):
        self.deck_count = random.choice([2, 4, 6, 8])
        self.multi_deck = MultiDeck(self.deck_count)
        self.player_hand = []
        self.dealer_hand = []

    def deal_initial_cards(self):
        self.player_hand = [self.multi_deck.draw_card(), self.multi_deck.draw_card()]
        self.dealer_hand = [self.multi_deck.draw_card(), self.multi_deck.draw_card()]
    
    def calculate_hand_value(self, hand):
        value = sum(card.face.face_value() for card in hand)
        ace_count = sum (1 for card in hand if card.face == CardFace.ACE)
        while value > 21 and ace_count > 0:
            value -= 10
            ace_count -= 1
        return value
    
    def show_hands(self, reveal_dealer=False):
        player_cards = ', '.join(f"{card.face.value}{card.suit.value}" for card in self.player_hand)
        dealer_cards = ', '.join(f"{card.face.value}{card.suit.value}" for card in self.dealer_hand)
        print(f"\nPlayer's Hand: {player_cards} (Value: {self.calculate_hand_value(self.player_hand)})")
        if reveal_dealer:
            print(f"Dealer's Hand: {dealer_cards} (Value: {self.calculate_hand_value(self.dealer_hand)})")
        else:
            print(f"Dealer's Hand: {self.dealer_hand[0].face.value}{self.dealer_hand[0].suit.value}, ?")

    def player_turn(self):
        while True:
            self.show_hands()
            choice = input("Do you want to 'hit' or 'stand'? ").strip().lower()
            if choice == 'hit':
                self.player_hand.append(self.multi_deck.draw_card())
                if self.calculate_hand_value(self.player_hand) > 21:
                    print("\nYou busted! Dealer wins.")
                    return False
            elif choice == 'stand':
                break
            else:
                print("Invalid choice. Please type 'hit' or 'stand'.")
        return True
    
    def dealer_turn(self):
        print("\nDealer's turn...")
        self.show_hands(reveal_dealer=True)
        while self.calculate_hand_value(self.dealer_hand) < 17:
            self.dealer_hand.append(self.multi_deck.draw_card())
            self.show_hands(reveal_dealer=True)
        if self.calculate_hand_value(self.dealer_hand) > 21:
            print("\nDealer busted! You win.")
            return False
        return True
    
    def determine_winner(self):
        player_score = self.calculate_hand_value(self.player_hand)
        dealer_score = self.calculate_hand_value(self.dealer_hand)
        print(f"\nFinal Scores - Player: {player_score}, Dealer: {dealer_score}")
        if player_score > dealer_score:
            print("You win!")
        elif dealer_score > player_score:
            print("Dealer wins")
        else:
            print("It's a tie")

    def play(self):
        while True:
            print(f"\nStarting a new round with {self.deck_count} decks...")
            self.multi_deck = MultiDeck(self.deck_count)  
            self.deal_initial_cards()
            if not self.player_turn():
                if input("\nPlay again? (y/n): ").strip().lower() != 'y':
                    break
                continue
            if not self.dealer_turn():
                if input("\nPlay again? (y/n): ").strip().lower() != 'y':
                    break
                continue  
            self.determine_winner()
            if input("\nPlay again? (y/n): ").strip().lower() != 'y':
                break
