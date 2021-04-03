from random import seed
from random import randrange
from datetime import datetime  

seed(datetime.now())  

# globals

kind = {"heart", "diamond", "spade", "club"}
number = {"ace", 2, 3, 4, 5, 6, 7, 8, 9, 10,"jack", "queen", "king"}

deck = {(k,n) for k in kind for n in number}


#functions

def player(player_cards):

    print("\n******Player's turn!******")
    
    
    for _ in range(2):
        card = deck.pop()
        player_cards.add(card)
    
    print(f"\nPlayer's cards: {player_cards}")

    sum_hand = hand_value(player_cards)   
    

    while True:
        print(f"\nYour total sum is: {sum_hand}.")
        if sum_hand == 21:
            return sum_hand
        elif sum_hand > 21:
            return sum_hand
        else:
            choice = input("\nDo you want another card? ('y': yes, 'n': no) ")
            if choice == 'y':
                card = deck.pop()
                print(card)
                print(player_cards)
                player_cards.add(card)
                sum_hand = hand_value(player_cards)
            elif choice == 'n':
                print(f"\nYou stopped with total sum: {sum_hand}")
                return sum_hand
            else:
                print("Error. You should give y for yes or n for no.")

    print(player_cards)
    print(sum_hand)



def hand_value(cards):
    cards_sum = 0
    ace = False

    for card in cards:
        if card[1] == "jack" or card[1] == "queen" or card[1] == "king":
            cards_sum += 10
        elif card[1] == "ace":
            ace = True
            cards_sum += 1
        else:
            cards_sum += int(card[1])
        
    if ace and cards_sum + 10 <= 21:
        cards_sum += 10


    return cards_sum


def computer(computer_cards, cards_player_sum):

    print("\n******Computer's turn!******")

    computer_cards.add(deck.pop())
    computer_cards.add(deck.pop())

    while True:
        
        computer_sum = hand_value(computer_cards)

        if computer_sum >= cards_player_sum:
            print(computer_cards)
            print(computer_sum)
            return computer_sum
        elif computer_sum < cards_player_sum:
            computer_cards.add(deck.pop())
        
        

# main


def main():

    rounds = 1
    score = [0, 0]

    while True:

        print(f"******Round {rounds}******")

        player_cards = set()
        computer_cards = set()
        
        player_cards_sum = player(player_cards)
        if(player_cards_sum == 21):
            print("\n***CONGRATULATIONS***. You won the round!!!")
            print("Nice play.")
            result = 'player'
        elif player_cards_sum > 21:
            print("\nYou lost.")
            print("Dont worry.")
            result = 'computer'
        else:
            computer_cards_sum = computer(computer_cards,player_cards_sum)
            if computer_cards_sum > 21:
                print("\nComputer is out.")
                print("***CONGRATULATIONS***. You won the round!!!")
                result = 'player'
            else:
                if computer_cards_sum > player_cards_sum:
                    print("\nComputer won!")
                    result = 'computer'
                if computer_cards_sum == player_cards_sum:
                    print("\nDeuce.")
                    result = 'deuce'

        if result == 'player':
            score[0] += 1
        elif result == 'computer':
            score[1] += 1
        elif result == 'deuce':
            pass
        else:
            print("Error")
        
        print("\n******Score******")
        print(f"\nPlayer's score: {score[0]} - Computer's score: {score[1]}")

        for card in player_cards:
            deck.add(card)

        for card in computer_cards:
            deck.add(card)
        
        
        while True:
            choice = input("\nDo you want to play again? ('y': yes, 'n': no) ")
            if choice == 'y':
                rounds += 1
                break
            elif choice == 'n':
                print("\n******Final Score******")
                print(f"Player's score: {score[0]} - Computer's score: {score[1]}")
                if score[0] > score[1]:
                    print("You are the winner!!! CONGRATS")
                elif score[0] < score[1]:
                    print("You lost to computer. Try again later.")
                else:
                    print("That's a deuce. Nice game!")
                print("\n***END GAME***")
                quit()
            else:
                print("Error. You should give y or n for yes and no!")
    
        

main()


