import pyfiglet
import os
import time


def main_header():
        title = pyfiglet.figlet_format("Sovereign Black 21")
        print("==================================================================================")
        print(title)
        print("==================================================================================")

def main_menu():
        print("| 1. Start New Game")
        print("| 2. Quit ")


def black_jack_menu():
        print("| 1. Hit \t\t\t\t\t|")
        print("| 2. Stay \t\t\t\t\t|")


def welcome_message():
        clear_screen()
        main_header()
        print("\nWelcome to Sovereign Black 21")
        print("Let us have some fun... Do you feel lucky??")
        input("Press Enter if you do")

def display_hand(player):
        clear_screen()
        main_header()
        handstring = ""
        hand_high_value = player.hand.value["high"]
        hand_low_value = player.hand.value["low"]
        remaining = 5 - len(player.hand.cards)
        handstring=''
        for card in player.hand.cards:
                handstring += f"{card.face }\t"
        print(f"\nPlayer:\t{player.name.title()}\t\t\tHand Status: {player.hand.status}")
        print("-----------------------------------------------------")
        print("CARD 1\tCARD 2\tCARD 3\tCARD 4\tCARD 5\t")
        print(handstring)
        print(f"\nHigh: {hand_high_value}\tLow:{hand_low_value}\tRemaining Cards:{remaining}")
        print("\n")


def display_hand_noclear(player):
        handstring = ""
        hand_high_value = player.hand.value["high"]
        hand_low_value = player.hand.value["low"]
        remaining = 5 - len(player.hand.cards)
        handstring = ''
        for card in player.hand.cards:
                handstring += f"{card.face }\t"
        print(f"\nPlayer:\t{player.name.title()}\t\t\tHand Status: {player.hand.status}")
        print("-----------------------------------------------------")
        print("CARD 1\tCARD 2\tCARD 3\tCARD 4\tCARD 5\t")
        print(handstring)
        print(f"\nHigh: {hand_high_value}\tLow:{hand_low_value}\tRemaining Cards:{remaining}")
        print("\n")

def print_cards(cards):
        clear_screen()
        main_header()
        header = pyfiglet.figlet_format("Card(s) Dealt")
        # print(header)
        print("Card(s) Dealt")
        print("==========================================================")
        for card in cards:
                print(f"card face: {card.face}\tcard_value: {max(card.possible_values)}, {min(card.possible_values)}")
        print()



def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_score(results):
        resultsbanner = pyfiglet.figlet_format("R E S U L T S")
        print("=========================================================")
        print(resultsbanner)
        print(f"| Hand Winner:\t\t {results.winner.title()}")
        print("--------------------------------------------------------")
        print("Score")
        print("--------------------------------------------------------")
        print(f"| Player: {results.players['player'].name.title()}\t\t{results.player}")
        print(f"| Player: {results.players['dealer'].name.title()}\t\t{results.dealer}")
        print(f"| Game Pot: \t\t\t{results.pot}")


def congratulations_blackjack():
        blackjack = pyfiglet.figlet_format("BlackJack")
        clear_screen()
        main_header()

        for i in range(0, 20):
                time.sleep(0.3)
                print(blackjack)


def busted():
    blackjack = pyfiglet.figlet_format("Busted")
    clear_screen()
    main_header()

    for i in range(0, 20):
        time.sleep(.3)
        print(blackjack)



