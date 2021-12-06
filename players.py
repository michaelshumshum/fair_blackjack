import random


class Player:
    def __init__(self):
        self.hand = []
        self.points = 0
        self.bust = False

    def draw_cards(self, cards: tuple):
        self.hand = list(cards)
        self.get_points()

    def hit(self, card):
        self.hand.append(card)
        self.get_points()

    def should_hit(self, dealer_card):
        if dealer_card in ['J', 'Q', 'K']:
            dealer_card = 10
        elif dealer_card == 'A':
            dealer_card = 1
        else:
            dealer_card = int(dealer_card)
        soft_totals = [  # hands where player has an ace
            lambda hand: sorted(hand) == ['8', 'A'] and (dealer_card == 6),
            lambda hand: sorted(hand) == ['7', 'A'] and (dealer_card <= 9),
            lambda hand: sorted(hand) in [['6', 'A'], ['5', 'A'], ['4', 'A'], ['3', 'A'], ['2', 'A'], ] and dealer_card <= 6,
        ]

        hard_totals = [  # hands with no aces or aces that can only be counted as 1
            lambda points: points <= 11,
            lambda points: (13 <= points <= 16) and (2 <= int(dealer_card) <= 6),
            lambda points: points == 12 and (4 <= int(dealer_card) <= 6),
        ]

        if self.points <= 11:
            return True
        # for condition in soft_totals:
        #     print(condition, condition(self.hand))
        # for condition in hard_totals:
        #     print(condition, condition(self.points))
        if any(condition(self.hand) for condition in soft_totals):
            return True
        if any(condition(self.points) for condition in hard_totals):
            return True
        return False

    def get_points(self):
        self.points = 0
        aces = 0
        for card in self.hand:
            if card in ['J', 'Q', 'K']:
                self.points += 10
            elif card == 'A':
                aces += 1
            else:
                self.points += int(card)

        for ace in range(aces):
            if self.points + 11 <= 21:
                self.points += 11
            else:
                self.points += 1

        if self.points < 21:
            self.bust = True
        else:
            self.bust = False


class Dealer(Player):
    def should_hit(self):
        return True if self.points < 17 else False
