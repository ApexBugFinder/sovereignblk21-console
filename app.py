import pyfiglet
import json, random
from enum import Enum
from menus import show_menus
from models import deck, card, hand, player
from models import blackjack




with open('data.json') as cards_file:
      cards = json.load(cards_file)

      new_deck = deck.Deck(cards['deck']);
      # for card in cards['deck']:
      #       print (card["name"])




#  NEW DECK


# print(new_deck.card_count())


# SHOW MAIN MENU AND GET USER INPUT

show_menus.main_header()


# MENU CHOICE
show_menus.welcome_message()
show_menus.clear_screen()
show_menus.main_header()
show_menus.main_menu()

print("\n")
main_menu_choice = input ("Select 1 or 2:  ")



if (main_menu_choice == "1"):
      user_name = input('Enter your name:  ')
      new_player = player.Player(user_name)
      dealer = player.Player('dealer')
      dealer.change_limit(17)

      players={"player":new_player, "dealer":dealer}
      ng = blackjack.Game(players, new_deck)

      ng.play_game()
elif (main_menu_choice == "2"):
      exit()
#  CREATE  PLAYERs










