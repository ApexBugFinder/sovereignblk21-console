from models import card
from menus.show_menus import print_cards
import random

class Deck:
      def __init__(self, deckdata):
            self.deck = []

            for i in deckdata:
                  h_value = max(i["value"])
                  l_value = min(i["value"])
                  new_card = card.Card(i["name"], h_value, l_value)
                  self.add_to_deck(new_card)
            self.shuffle_deck()




      def card_count(self):
            return len(self.deck)


      def add_to_deck(self, card):
            self.deck.append(card)
            # print('added card to deck: ', card.face)

      def deal_from_deck(self, amnt_of_cards):
            count =0
            cards_dealt = set()
            while count < amnt_of_cards:
                  cards_dealt.add(self.deck.pop(random.randrange(0, len(self.deck))))
                  count += 1

            return cards_dealt

      def print_deck(self):
            for i in self.deck:
                  print(i.face, i.value)

      def shuffle_deck(self):
            # print("PRE SHUFFLE")
            # for i in self.deck:
            #       print(i.face)

            random.shuffle(self.deck)
            # print("POST SHUFFLE")
            # for i in self.deck:
            #       print(i.face)

      def deck_count(self):
            return len(self.deck)

