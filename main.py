import random

class Hand:
    def __init__(self, dealer=False):
        self.cards = []
        self.value = 0
        self.dealer = dealer
        
    def add_card(self, card_list):
        self.cards.extend(card_list)
        self.calculate_value()
        
    def calculate_value(self):
        self.value = 0
        has_ace = False
        
        for card in self.cards:
            if card.rank['value'] == 11:
                has_ace = True
            
            self.value += int(card.rank['value'])
            
        if has_ace and self.value > 21:
            self.value -= 10
            
    def get_value(self):
        self.calculate_value()
        return self.value
    
    def is_blackjack(self):
        return self.get_value() == 21
    
    def display(self, show_all_dealer_cards=False):
        print(f'''{"Dealer's" if self.dealer else "Your"} hand:''')

        for index, card in enumerate(self.cards):
            if self.dealer and index == 0 and not show_all_dealer_cards \
            and not self.is_blackjack():
                print("**Card hidden**")
            else:
                print(card)
            
        if not self.dealer:
            print("Value:", self.get_value())
        print()

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return f"{self.rank['rank']} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = []
        suits = ['spades', 'clubs', 'hearts', 'diamonds']
        ranks = [
            {"rank": "A", "value": 11},
            {"rank": "2", "value": 2},
            {"rank": "3", "value": 3},
            {"rank": "4", "value": 4},
            {"rank": "5", "value": 5},
            {"rank": "6", "value": 6},
            {"rank": "7", "value": 7},
            {"rank": "8", "value": 8},
            {"rank": "9", "value": 9},
            {"rank": "10", "value": 10},
            {"rank": "J", "value": 10},
            {"rank": "Q", "value": 10},
            {"rank": "K", "value": 10}
        ]

        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))
        
    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)
        
    def deal(self, number):
        cards_dealed = []
        for i in range(number):
            if len(self.cards) > 0:
                cards_dealed.append(self.cards.pop())
        
        return cards_dealed

class Game:
    def check_winner(self, player_hand, dealer_hand, game_over=False):
        if game_over:
            if player_hand.get_value() > dealer_hand.get_value():
                print("You win!")
            elif player_hand.get_value() == dealer_hand.get_value():
                print("Tie")
            else:
                print("Dealer win!")
            
            return True
        
        if player_hand.get_value() > 21:
            print("You are busted. Dealer wins!")
            return True
        
        if dealer_hand.get_value() > 21:
            print("Dealer busted. You win!")
            return True
        
        if player_hand.is_blackjack() and dealer_hand.is_blackjack():
            print("Both players have blackjack. It's a tie!")
            return True
        
        if player_hand.is_blackjack():
            print("You have blackjack. You won!")
            return True
        
        if dealer_hand.is_blackjack():
            print("Dealer have blackjack. Dealer wins!")
            return True
        
        return False
    
    def play(self):
        game_number = 0
        games_to_play = 0
        
        print()
        print("################# BlackJack Game #################")
        print("############## created by Stavar Laurentiu #######")
        print("\n")

        while games_to_play <= 0:
            try:
                games_to_play = int(input("How many games do you want to play? "))
            except:
                print("You must enter a number!")
                
        while game_number < games_to_play:
            game_number += 1
            
            deck = Deck()
            deck.shuffle()
            
            player_hand = Hand()
            dealer_hand = Hand(dealer=True)
            
            for i in range(2):
                player_hand.add_card(deck.deal(1))
                dealer_hand.add_card(deck.deal(1))
                
            print()
            print("#" * 50)
            print(f"Game {game_number} out of {games_to_play}.")
            print()
            player_hand.display()
            dealer_hand.display()
            
            if self.check_winner(player_hand, dealer_hand):
                continue
            
            choice = ""
            while player_hand.get_value() < 21 and choice not in ["s", "stand"]:
                choice = input("Please choose 'Hit' or 'Stand': ").lower()

                print()
                while choice not in ["h", "hit", "s", "stand"]:
                    print("Enter a valid option! ('h'/'hit' or 's'/'stand')")
                    choice = input("Please choose 'Hit' or 'Stand': ").lower()

                if choice in ["h", "hit"]:
                    player_hand.add_card(deck.deal(1))
                    player_hand.display()
                    
            if self.check_winner(player_hand, dealer_hand):
                    continue
                
            player_hand_value = player_hand.get_value()
            dealer_hand_value = dealer_hand.get_value()
            
            while dealer_hand_value < 17 or dealer_hand_value < player_hand_value:
                print("Dealer deal a card....")
                
                dealer_hand.add_card(deck.deal(1))
                dealer_hand_value = dealer_hand.get_value()
            
            dealer_hand.display(show_all_dealer_cards=True)
                
            if self.check_winner(player_hand, dealer_hand):
                    continue
                
            print("Final results:")
            print("You're hand: ", player_hand_value)
            print("Dealer's hand: ", dealer_hand_value)
            
            self.check_winner(player_hand, dealer_hand, game_over=True)
            
        print("\nThanks for playing!")
        
g = Game()
g.play()