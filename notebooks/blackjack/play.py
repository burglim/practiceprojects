from blackjack import Chips, Hand, Card, Deck
from blackjack import bet, player_choice, win_check, comp_win_check, play_again

def game_play():
    
    print('Welcome to Blackjack!')
    print()
    playing = True
    player_chips = Chips()
    
    while playing:
        player = Hand()
        computer = Hand()
  
        print(f'You have {player_chips.balance} chips')
        amount = bet(player_chips)
        if amount == 0:
            return 

        game_deck = Deck()
        game_deck.shuffle()

        print()
        print('PLAYER CARDS:')
        player.play_one(game_deck.deal_one())
        player.play_one(game_deck.deal_one())
        print(f'Total hand value: {player.hand_value}')
        print()
            
        print('COMPUTER CARDS:')
        computer.play_one(game_deck.deal_one())
        computer.play_one_hidden(game_deck.deal_one())
        print('***Hidden card***')
        print('Total computer hand value: unknown')
        print()
            
        game_on = True
        player_turn = True
        
        while game_on:
            if win_check(game_on, player, computer, player_chips, amount) == False:
                break

            while player_turn:
                if win_check(player_turn, player, computer, player_chips, amount) == False:
                    break

                choice = player_choice()
                print()
                if choice == 'hit':
                    player.play_one(game_deck.deal_one())
                    print(f'Total hand value: {player.hand_value}')
                else:
                    break
            game_on = False

        if player.hand_value < 21:
            comp_turn = True

            while comp_turn:
                if computer.hand_value < 16:
                    print('COMPUTER TURN:')
                    computer.play_one(game_deck.deal_one())
                    continue
                else:
                    print(f'Total computer hand value: {computer.hand_value}')
                    comp_win_check(comp_turn, player, computer, player_chips, amount)
                    break
        
        if player_chips.balance == 0:
            playing = False
            print('Game Ended: You have run out of chips!')
            break           
        elif play_again() == False:
            playing = False
            print('Game Ended: Thank you for playing!')
            break
        else:
            continue
    pass

print(1)
game_play()