from art import logo, vs
from game_data import gdata
import random

def pop_item(a_lst):
    """removes items from the list and returns them as"""
    option = a_lst.pop(random.randint(0, (len(a_lst)-1)))
    return(option)

def compare_item(option_a, option_b):
    """Compare two items and returns the one with greater follower count"""
    if option_a['follower_count'] > option_b['follower_count']:
        return "a"
    else:
        return "b"

current_score = 0
print(logo)
option_a = pop_item(gdata)
option_b = pop_item(gdata)
while True:
    correct_answer = compare_item(option_a, option_b)
    # Prints out options for user to select
    print(f"Option A: {option_a['name']}, a "
          f"{option_a['description']}, from"
          f" {option_a['country']}. ")
    print(f"{vs}")
    print(f"Option B: {option_b['name']}, a "
          f"{option_b['description']}, from"
          f" {option_b['country']}")
    print("Who has more followers? \n")
    user_choice = input(f"Type A or B:\n").lower()

    print(f"\n\n{option_a['name']} has {option_a['follower_count']} followers and "
          f"{option_b['name']} has {option_b['follower_count']} followers.\n")

    #Determines the whether you win or lose and compiles or prints points.
    if user_choice == correct_answer:
        current_score += 1
        print(logo)
        print(f"You are correct! Current score: {current_score}")
        if correct_answer == 'a':
            option_b = pop_item(gdata)
        else:
            option_a = option_b
            option_b = pop_item(gdata)

    else:
        print(logo)
        print("That is incorrect.")
        print(f"Your final score is: {current_score}")
        break




