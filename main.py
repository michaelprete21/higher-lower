from art import logo, vs
from game_data import gdata
from replit import clear
import random


def pop_item(a_lst):
    """removes items from the list and returns them as"""
    option = a_lst.pop(random.randint(0, (len(a_lst) - 1)))
    return (option)


def compare_item(option_a, option_b):
    """Compare two items and returns the one with greater follower count"""
    if option_a['follower_count'] > option_b['follower_count']:
        return "a"
    else:
        return "b"


def output_format(option):
    return (f"{option['name']}, a "
            f"{option['description']}, from"
            f" {option['country']}. ")


def output_resut(option_a, option_b):
    return (f"\n\n{option_a['name']} has {option_a['follower_count']} "
            f"followers and "
            f"{option_b['name']} has {option_b['follower_count']} followers.")


current_score = 0
print(logo)
option_a = pop_item(gdata)
option_b = pop_item(gdata)
while True:
    clear()
    correct_answer = compare_item(option_a, option_b)
    # Prints out options for user to select
    print(f"Option A: {output_format(option_a)}")
    print(f"{vs}")
    print(f"Option B: {output_format(option_b)}")
    print("Who has more followers? \n")
    user_choice = input(f"Type A or B:\n").lower()
    # Determines the whether you win or lose and compiles or prints points.
    if user_choice == correct_answer:
        clear()
        current_score += 1
        print(logo)
        print(output_resut(option_a, option_b))
        print(f"You are correct! Current score: {current_score}")
        if correct_answer == 'a':
            option_b = pop_item(gdata)
        else:
            option_a = option_b
            option_b = pop_item(gdata)

    else:
        clear()
        print(logo)
        print("You are incorrect.")
        print(output_resut(option_a, option_b))
        print(f"Your final score is: {current_score}")
        break
