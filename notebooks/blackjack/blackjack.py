from random import shuffle
from IPython.display import clear_output

nums = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

class Card:
    def __init__(self,num,suit):
        self.num = num
        self.suit = suit
        self.value = values[num]
        
    def __str__(self):
        return f'{self.num} of {self.suit}'

class Deck:
    
    def __init__(self):
        
        self.whole_deck = []
            
        for suit in suits:
            for num in nums:
                created_card = Card(num, suit)
                self.whole_deck.append(created_card)
    
    def __str__(self):
        return f'{len(self.whole_deck)} cards'
    
    def shuffle(self):
        return shuffle(self.whole_deck)
    
    def deal_one(self):
        return self.whole_deck.pop()

class Chips:
    
    def __init__(self, balance=100):
        self.balance = balance
    
    def __str__(self):
        return f'Account balance: {self.balance} chips'
    
    def deposit(self, deposit):
        self.balance += deposit
        print(f'New balance: {self.balance} chips')
        
    def withdraw(self, withdraw):
        if withdraw>self.balance:
            print('Chips Unavailable!')
        else:
            self.balance -= withdraw
            print(f'Accepted\nNew balance: {self.balance} chips')

class Hand:
    
    def __init__(self):
        self.cards_in_hand = []
        self.hand_value = 0
        
    def __str__(self):
        return f'Number of cards played: {len(self.cards_in_hand)}\nValue of hand: {self.hand_value}'
    
    def play_one(self, new_card):
        self.cards_in_hand.append(new_card)
        if new_card.num == 'Ace':
            if self.hand_value <= 10:
                new_card.value = 11
            else:
                new_card.value = 1
        self.hand_value += new_card.value
        print(new_card)
        
    def play_one_hidden(self, new_card):
        self.cards_in_hand.append(new_card)
        self.hand_value += new_card.value

def bet(chips):
    player_bet = True
    while player_bet:
        try:
            bet_amount = int(input('How much would you like to bet? Please enter a whole number: '))
            if bet_amount > chips.balance:
                print('Chips Unavailable!')
                continue
            player_bet = False
            break
        except ValueError:
            print('Please enter an integer')
            continue
    
    if bet_amount == 0:
        print('Game Ended')
        return bet_amount
    
    else:
        chips.withdraw(bet_amount)
        return bet_amount

def player_choice():
    valid = False
    
    while valid == False:
        choice = input('Would you like to hit or stay? ').lower()
    
        if choice[0] == 'h' or choice[0] == 's':
            valid = True
        else:
            print('Please enter either hit or stay')
            continue
            
    if choice[0] == 'h':
        return 'hit'
    else:
        return 'stay'

def win_check(marker, person, comp, chips, bet_amount):
    
    #print(person.hand_value)
    if person.hand_value > 21:
        print('You lose!')
        marker = False
        return marker
            
    elif person.hand_value == 21:
        print('You win: you receive double your bet!')
        chips.deposit(bet_amount*2)
        marker = False
        return marker
    
    else:
        pass

def comp_win_check(marker, person, comp, chips, bet_amount):
    
    if comp.hand_value > 21:
        print('You win: you receive double your bet!')
        chips.deposit(bet_amount*2)
        marker = False
        return marker
    
    elif comp.hand_value == 21:
        print('You lose!')
        marker = False
        return marker
    
    elif comp.hand_value > person.hand_value:
        print('Bust: you lose!')
        marker = False
        return marker
    
    elif comp.hand_value < person.hand_value:
        print('You win: you receive double your bet!')
        chips.deposit(bet_amount*2)
        marker = False
        return marker
    
    elif comp.hand_value == person.hand_value:
        print('Draw: you get your chips back')
        chips.deposit(bet_amount)
        marker = False
        return marker
    
    else:
        print('Error')

def play_again():
    answer = input('Would you like to play again? Please type y or n: ').lower()
    if answer == 'y':
        clear_output(wait=True)
        return True
    else: 
        return False
