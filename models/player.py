from models.hand import Hand, HandStatus
from enum import Enum


class Player:

      def __init__(self, name):
            self.name = name
            self.limit = 0
            self.hand = Hand(self.limit)


      def change_limit(self, new_limit):
            # print(f"{self.name} your limit {self.limit} is being changed to {new_limit}")
            self.limit = new_limit
            self.hand.player_limit = new_limit
            # print(f"{self.name} your new limit is {self.limit}")
            return self.limit

      def add_to_hand(self, cards ):
            if self.hand.status == HandStatus.ACTIVE.name:


                  self.hand.add_to_hand(cards)




