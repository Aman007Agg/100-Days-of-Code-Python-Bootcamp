from random import random

from art import logo, vs
from game_data import data
import random


def compare_insta_followers():
    print(logo)
    final_score = 0
    is_correct_answer = True

    A = random.choice(data)
    while is_correct_answer:

        B = random.choice(data)

        print(f"Compare A:{A['name']}, {A['description']}, from {A['country']}")
        print(vs)
        print(f"Against B:{B['name']}, {B['description']}, from {B['country']}")
        answer = input("Who has more followers? Type 'A' or 'B' ").upper()
        output = " "

        if A['follower_count'] > B['follower_count']:
            output = "A"
        else:
            output = "B"
            A = B
        if answer == output:
            is_correct_answer = True
            final_score += 1
        else:
            is_correct_answer = False
            print(f"Sorry, that's wrong. Final score: {final_score}")


compare_insta_followers()

#
# from art import logo, vs
# from game_data import data
# import random
#
#
# def get_random_account():
#     return random.choice(data)
#
#
# def format_account(account):
#     return f"{account['name']}, {account['description']}, from {account['country']}"
#
#
# def check_answer(user_guess, followers_a, followers_b):
#     if followers_a > followers_b:
#         return user_guess == "A"
#     else:
#         return user_guess == "B"
#
#
# def compare_insta_followers():
#     print(logo)
#
#     score = 0
#     game_should_continue = True
#
#     account_a = get_random_account()
#     account_b = get_random_account()
#
#     while game_should_continue:
#
#         # Prevent same account comparison
#         while account_a == account_b:
#             account_b = get_random_account()
#
#         print(f"Compare A: {format_account(account_a)}")
#         print(vs)
#         print(f"Against B: {format_account(account_b)}")
#
#         user_answer = input(
#             "Who has more followers? Type 'A' or 'B': "
#         ).upper()
#
#         followers_a = account_a['follower_count']
#         followers_b = account_b['follower_count']
#
#         is_correct = check_answer(
#             user_answer,
#             followers_a,
#             followers_b
#         )
#
#         if is_correct:
#             score += 1
#             print(f"You're right! Current score: {score}")
#
#             # Winner stays
#             account_a = account_b
#             account_b = get_random_account()
#
#         else:
#             game_should_continue = False
#             print(f"Sorry, that's wrong. Final score: {score}")
#
#
# compare_insta_followers()