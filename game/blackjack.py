
from models.hand import Hand, HandStatus
from models.player import Player
from models.deck import Deck
from models.card import Card
from models.result import Results
from enum import Enum
import time
from menus.show_menus import display_hand, print_cards, display_hand_noclear
from menus.show_menus import clear_screen, main_header, print_score

class GameStatus(Enum):
            ACTIVE = 1
            COMPLETE = 2
class Game:
      def __init__(self, players, deck):
            self.player = players["player"]
            self.dealer = players["dealer"]
            self.status = GameStatus.COMPLETE
            self.results = Results(players)
            self.deck = deck
            self.play = False

            self.used_pile = []

      def sortDeck(self, deck):
            self.deck.shuffle_deck()



      def deal_to_player(self):
            if len(self.player.hand.cards) == 0:
                  # if player has no cards deal two cards from deck

                  pass
            else:
                  #else deal one
                  pass


      def play_game(self):
            self.status= GameStatus.ACTIVE
            self.play = True

            # print(f"Deck Count: {self.deck.deck_count()}")
            while self.play and self.deck.deck_count() > 0:


                  players_turn = True
                  dealers_turn = True
                  while players_turn:
                        clear_screen()
                        main_header()
                        if self.player.hand.status == HandStatus.ACTIVE.name:
                              # deal to player 2 cards
                              cards_for_player = self.deck.deal_from_deck(2)

                              print_cards(cards_for_player)
                              time.sleep(2)
                              self.player.add_to_hand(cards_for_player)

                              display_hand(self.player)
                              player_complete = self.hit_or_hold()


                              if player_complete:
                                    players_turn = not player_complete
                                    # print(f"players turn: {players_turn}")
                                    break
                              else:
                                    pass

                        else:
                              players_turn = False

                  input("Enter to continue...")
                  clear_screen()
                  main_header()
                  print("Dealer's Turn:")
                  print("-----------------------------------------\n")
                  while self.dealer.hand.status == HandStatus.ACTIVE.name:


                              cards_for_dealer = self.deck.deal_from_deck(1)
                              print_cards(cards_for_dealer)
                              time.sleep(2)
                              self.dealer.hand.add_to_hand(cards_for_dealer)

                              display_hand(self.dealer)
                              input("Enter to continue")


                  #  SET SCORE
                  self.set_score()
                  # clear_screen()
                  self.completeHand()

                  # ASK TO CONTINUE
                  cont_choice = input("\nPress Enter to  continue or enter N for no?")
                  if cont_choice.lower() == "n":
                        self.play = False
                        clear_screen()
                        main_header()
                        print_score(self.results)
                        print("\nThank you for playing Sovereign BlackJack 21")
                  else:

                  #  CLEAR HAND / NEW HAND
                        self.refreshHand()
                        




            # def have_turn(user):
            #       pass

            # def manage_hand_status(self):
            #       if self.player.limit == 0 and self.player.hand.status == HandStatus.ACTIVE:
            #             hand_status = True
            #             while hand_status:
            #                   players_choice = self.hit_or_hold()



            #       elif self.player.limit !=0 and self.player.hand.status == HandStatus.ACTIVE:
            #             hand_status = True

      def completeHand(self):
                  self.set_score()
                  clear_screen()
                  main_header()
                  display_hand_noclear(self.player)
                  display_hand_noclear(self.dealer)
                  print_score(self.results)

      def refreshHand(self):
            for i in self.player.hand.cards:
                        self.used_pile.append(i)
            for i in self.dealer.hand.cards:
                  self.used_pile.append(i)
            del self.player.hand
            self.player.hand = Hand(self.player.limit)
            print(f"Player hand status: {self.player.hand.status}")
            del self.dealer.hand
            self.dealer.hand = Hand(self.dealer.limit)

      def hit_or_hold(self):
            round_complete = False
            while self.player.hand.status == HandStatus.ACTIVE.name:
                  print()
                  print("1.  Hit Me!\n2.  Hold")
                  players_choice = input("Please choose 1 or 2:  ")
                  if players_choice == "2":
                              self.player.hand.hand_status_hold()

                              break
                  elif players_choice == "1":

                              self.player.hand.hand_status_active()
                              clear_screen()
                              main_header()
                              # Deal from deck
                              cards_for_player = self.deck.deal_from_deck(1)
                              # print("Display cards dealt")
                              print_cards(cards_for_player)
                              time.sleep(2)
                              # print("Adding cards to player hand")
                              self.player.add_to_hand(cards_for_player)
                              display_hand(self.player)



                  else:
                              print("Incorrect entry.. Try Again\n\n")

            if self.player.hand.status != HandStatus.ACTIVE.name:
                  round_complete = True
                  print('Round complete')
            return round_complete

      def set_score(self):
            if self.dealer.hand.status == HandStatus.BLACKJACK.name and self.player.hand.status == HandStatus.BLACKJACK.name:
                  self.results.draw()
            elif self.dealer.hand.status == HandStatus.BLACKJACK.name:
                  self.results.dealer_won()
            elif self.player.hand.status == HandStatus.BLACKJACK.name:
                  self.results.player_won()
            elif self.player.hand.status == HandStatus.HOLD.name and self.dealer.hand.status == HandStatus.HOLD.name:
                  p_low =99
                  p_high=99
                  player_low=0
                  d_low = 99
                  d_high = 99
                  dealer_low=0

                  if self.player.hand.value["high"] < 21:
                        p_high = 21 -self.player.hand.value["high"]


                  if self.player.hand.value["low"] < 21:
                        p_low = 21 - self.player.hand.value["high"]

                  if self.dealer.hand.value["high"] < 21:
                        d_high = 21 - self.dealer.hand.value["high"]

                  if self.dealer.hand.value["low"] < 21:
                        d_low = 21 -self.dealer.hand.value["low"]

                  player_low = min(p_high, p_low)
                  dealer_low = min(d_low, d_high)

                  if player_low == dealer_low:
                        self.results.draw()
                  elif player_low < dealer_low:
                        self.results.player_won()
                  else:
                        self.results.dealer_won()
            elif self.player.hand.status == HandStatus.BUST.name and self.dealer.hand.status == HandStatus.BUST.name:
                  self.results.draw()
            elif self.player.hand.status == HandStatus.BUST.name:
                  self.results.dealer_won()
            elif self.dealer.hand.status == HandStatus.BUST.name:
                  self.results.player_won()


