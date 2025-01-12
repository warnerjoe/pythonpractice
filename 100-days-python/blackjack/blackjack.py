import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_hand = []
computer_hand = []

def reset_game_state(p_hand, c_hand):
    """Resets the values of the hands"""
    p_hand.clear()
    c_hand.clear()

def start_game():
    """
    Asks the user if they wish to play blackjack,

    if yes it plays blackjack
    no ends the program
    any other input restarts the input
    """
    reset_game_state(player_hand, computer_hand)

    desire_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n' ").lower()

    if desire_to_play == 'y':
        print(art.logo)
        play_blackjack()
    elif desire_to_play == 'n':
        print("Ending game.")
    else:
        print("Incorrect input.")
        start_game()

def play_blackjack():
    """
    Prints blackjack logo, draws starting hands, displays game state, asks for an additional card
    """
    draw_starting_hands()
    display_game_state()
    player_score = sum(player_hand)
    if player_score == 21:
        print("Blackjack! You win!")
        start_game()
    else:
        ask_for_hit()

def draw_starting_hands():
    """Draws 2 cards for the player, 1 card for the computer"""
    draw_card(player_hand, 2)
    draw_card(computer_hand, 1)

def ask_for_hit():
    """
    Asks the user if they would like another card,
    Yes: Draws a card, shows the game state, asks again
    No: Calculates game score
    Other: Prints invalid input, asks again
    """
    hit_me = input(f"Type 'y' to get another card, type 'n' to pass: ").lower()

    if hit_me == 'y':
        draw_card(player_hand, 1)
        player_score = sum(player_hand)
        display_game_state()
        if player_score > 21:
            final_game_state()
            print("Bust!  You lose!")
            start_game()
        elif player_score == 21:
            final_game_state()
            print("Blackjack!  You win!")
            start_game()
        else:
            ask_for_hit()
    elif hit_me == 'n':
        end_game()
    else:
        print("Invalid input.")
        display_game_state()
        ask_for_hit()

def end_game():
    """
    Runs the computer decision logic, calculates score,
    determines who won, and then asks if you'd like another round
    """
    computer_draw_logic()

    player_score = sum(player_hand)
    computer_score = sum(computer_hand)

    final_game_state()
    if computer_score == 21:
        print(f"Your opponent got a blackjack!  You lose.")
    elif computer_score > 21:
        print(f"The computer busted! You win!")
    elif player_score == computer_score:
        print("Draw!")
    elif player_score > computer_score:
        print("Your hand was higher! You win!")
    else:
        print("You had less points, you lose!")

    start_game()

def computer_draw_logic():
    """
    If the computer determines it's worth drawing another card it will.
    """
    computer_score = sum(computer_hand)
    if (21 - computer_score) > 5:
        draw_card(computer_hand, 1)
        computer_draw_logic()

def draw_card(participant_hand, times):
    """Chooses a random card from the cards array and adds it into the provided hand """
    for number in range(times):
        drawn_card = random.choice(cards)
        participant_score = sum(participant_hand)
        if drawn_card == 11:
            if (21 - participant_score) >= 11:
                participant_hand.append(11)
            else:
                participant_hand.append(1)
        else:
            participant_hand.append(drawn_card)

def display_game_state():
    """Displays the current game state (hands and scores)"""
    player_current_score = sum(player_hand)
    print(f"\tYour cards: {player_hand}, current score: {player_current_score}")
    print(f"\tComputer's first card: {computer_hand[0]}")

def final_game_state():
    player_score = sum(player_hand)
    computer_score = sum(computer_hand)
    print(f"\tYour final hand: {player_hand}, final score: {player_score}")
    print(f"\tComputer's final hand: {computer_hand}, final score: {computer_score}")

start_game()