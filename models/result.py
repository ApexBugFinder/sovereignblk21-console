class Results:
      def __init__(self, players):
          self.dealer = 0
          self.player = 0
          self.pot = 0
          self.winner = ''
          self.players = players

      def dealer_won(self):

            self.dealer  = self.dealer + self.pot + 1
            self.pot = 0

            self.winner = self.players["dealer"].name
            print(f'WINNER: {self.winner}')
            return

      def player_won(self):

            self.player = self.player + self.pot + 1
            self.pot = 0

            self.winner = self.players["player"].name
            print(f'WINNER: {self.winner}')
            return

      def draw(self):
            self.pot += 1
            self.winner = "draw"
            print(f'WINNER: {self.winner.title()}')
            return