import random


class Game:
    def __init__(self, decks, players, dealer, rounds):
        self.decks = decks
        self.players = players
        self.dealer = dealer
        self.deck_order = []
        self.rounds = rounds
        self.current_round = 0
        self.card_count = 0

        self.scores = {}
        for player in self.players:
            self.scores[player] = {'wins': 0, 'ties': 0, 'losses': 0}

    def shuffle(self):
        self.deck_order = []
        for index, deck in enumerate(self.decks):
            deck.shuffle()
            self.deck_order.extend([index for i in range(len(deck.cards) - 1)])
        random.shuffle(self.deck_order)
        self.card_count = len(self.deck_order)

    def card(self):
        return self.decks[self.deck_order.pop(0)].get_card()

    def simulate(self):
        self.shuffle()
        while self.current_round < self.rounds:
            # draw cards to players and dealer
            for player in self.players:
                player.draw_cards((self.card(), self.card()))
            self.dealer.draw_cards((self.card(), self.card()))

            for player in self.players:
                while player.should_hit(self.dealer.hand[0]):
                    player.hit(self.card())
            while self.dealer.should_hit():
                self.dealer.hit(self.card())

            for player in self.players:
                if player.points > 21:
                    # print(player.points, self.dealer.points, 'lose')
                    self.scores[player]['losses'] += 1
                elif (player.points < self.dealer.points) and (self.dealer.points <= 21):
                    # print(player.points, self.dealer.points, 'lose')
                    self.scores[player]['losses'] += 1
                elif player.points == self.dealer.points:
                    # print(player.points, self.dealer.points, 'tie')
                    self.scores[player]['ties'] += 1
                else:
                    # print(player.points, self.dealer.points, 'win')
                    self.scores[player]['wins'] += 1
            self.current_round += 1
            if len(self.deck_order) < self.card_count / 2:
                self.shuffle()
