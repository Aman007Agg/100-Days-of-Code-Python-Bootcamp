import random
from art import logo

"""Our Blackjack Game House Rules
The deck is unlimited in size.
There are no jokers.
The Jack/Queen/King all count as 10.
The Ace can count as 11 or 1.
Use the following list as the deck of cards:

The cards in the list have equal probability of being drawn.
Cards are not removed from the deck as they are drawn.
The computer is the dealer.
"""


"""
Create a function called compare() and pass in the user_score and computer_score.
If the computer and user both have the same score, then it's a draw.
If the computer has a blackjack (0), then the user loses.
If the user has a blackjack (0), then the user wins.
If the user_score is over 21, then the user loses.
If the computer_score is over 21, then the computer loses.
If none of the above, then the player with the highest score wins.
"""


# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# player = random.choice(cards)
# dealer = random.choice(cards)

def deal_card():
    """ Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    # if 11 in cards and 10 in cards and len(cards) == 2:
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(u_score, comp_score):
    if u_score == comp_score:
        return "Draw"
    elif comp_score == 0:
        return "You Lose, opponent has BlackJack"
    elif u_score == 0:
        return "You Win, with a BlackJack"
    elif u_score > 21:
        return "You went over. You lose"
    elif comp_score > 21:
        return "Opponent went over. You win"
    elif u_score > comp_score:
        return "You win!"
    else:
        return "You lose!"

def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        # new_card = deal_card()
        # user_cards.append(new_card)
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first cards: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card , type 'n' to pass: ").lower()
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score,computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'no' ").lower() == "y":
    print("\n"*20)
    play_game()






