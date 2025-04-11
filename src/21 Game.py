import random

card_values = {
    'A': 11,
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 10, 'Q': 10, 'K': 10
}
cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
player_hand = []
dealer_hand = []
win_count = 0

def get_hand_value(hand):
    value = 0
    aces = 0
  
    #Adds up the value of the cards in the hand list and counts number of aces
    for card in hand:
        if card == 'A':
            aces += 1
        value += card_values[str(card)]
    
    # if the value of the hand is greater than 21 and there is an ace in the hand, the ace is worth 1 instead of 11
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

def setup():
    print("\nWelcome to Blackjack!")
    print("\nYou are dealt: ")
    player_hand.clear()
    player_hand.append(random.choice(cards))
    player_hand.append(random.choice(cards))
    print(*player_hand, "\nYour total is: ", get_hand_value(player_hand))

    dealer_hand.clear()
    dealer_hand.append(random.choice(cards))
    print("\nDealer is dealt:")
    print(*dealer_hand, "\nDealer's total is: ", get_hand_value(dealer_hand))
    
def player_turn(win_count):
    #Players starting 2 cards is Blackjack
    if get_hand_value(player_hand) == 21:
        print("\nYou Win!")
        return win_count + 1
    
    #while Players cards is less than 21
    while get_hand_value(player_hand) < 21:
      
        #Player is asked if they would like to HIT or STAY
        x = input("\nDo you HIT or STAY: ")
        if x == "HIT":
            player_hand.append(random.choice(cards))
            print(*player_hand, "\nYour total is: ", get_hand_value(player_hand))
            
            #Check if player busts or has blackjack
            if get_hand_value(player_hand) > 21:
                print("\nYou BUST!")
                print("\nDealer Wins!")
                return win_count
            elif get_hand_value(player_hand) == 21:
                print("\nYou Win!")
                return win_count + 1
              
        #If the player stays
        elif x == "STAY":
            print("You STAY with: ", get_hand_value(player_hand), "\n")
            return None

def dealer_turn(win_count):
  
  #Dealer must hit until their cards is >=16
  while get_hand_value(dealer_hand) < 16:
    dealer_hand.append(random.choice(cards))
    print("\nDealer's hand is: ", *dealer_hand, "\nDealer's total is: ", get_hand_value(dealer_hand))

  #If dealer busts
  if get_hand_value(dealer_hand) > 21:
      print("Dealer Busts!")
      print("You Win!")
      win_count += 1
      return win_count
  
  #If dealer reaches 21
  elif get_hand_value(dealer_hand) == 21:
      print("\nDealer Wins!")
      return win_count

  #If dealer beats player
  elif get_hand_value(dealer_hand) > get_hand_value(player_hand):
      print("\nDealer Wins!")
      return win_count

  #If player beats dealer
  elif get_hand_value(dealer_hand) < get_hand_value(player_hand):
      print("\nYou Win!")
      win_count += 1
      return win_count
      

  #If dealer and player tie
  elif get_hand_value(dealer_hand) == get_hand_value(player_hand):
      print("\nTie!\n")
      home(win_count)

def home(win_count):
    while True:
        print("\nWin Counter:", win_count)
        y = input("Do you want to play Blackjack? (Y/N): ")
        
        if y == "Y":
            setup()
            player_result = player_turn(win_count)
            
            if player_result is not None:
                win_count = player_result
            else:
                dealer_result = dealer_turn(win_count)
                if dealer_result is not None:
                    win_count = dealer_result
            
            continue
        elif y == "N":
            print("Final Win Count:", win_count)
            exit()
        else:
            print("Please enter Y or N")

home(win_count)