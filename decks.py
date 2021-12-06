import random


class Deck:
    def __init__(self):
        self.card_count = {
            'A': 4,
            '2': 4,
            '3': 4,
            '4': 4,
            '5': 4,
            '6': 4,
            '7': 4,
            '8': 4,
            '9': 4,
            '10': 4,
            'J': 4,
            'Q': 4,
            'K': 4,
        }
        self.make_deck()

    def make_deck(self):
        self.cards = []
        for card, count in self.card_count.items():
            self.cards.extend([card for i in range(count)])

    def shuffle(self):
        self.make_deck()
        random.shuffle(self.cards)

    def get_card(self):
        return self.cards.pop(0)


class CustomDeck(Deck):
    def __init__(self, **kwargs):
        card_kwargs = {
            'A': 'A',
            'two': '2',
            'three': '3',
            'four': '4',
            'five': '5',
            'six': '6',
            'seven': '7',
            'eight': '8',
            'nine': '9',
            'ten': '10',
            'J': 'J',
            'Q': 'Q',
            'K': 'K'

        }
        self.card_count = {
            'A': 4,
            '2': 4,
            '3': 4,
            '4': 4,
            '5': 4,
            '6': 4,
            '7': 4,
            '8': 4,
            '9': 4,
            '10': 4,
            'J': 4,
            'Q': 4,
            'K': 4,
        }
        for card, count in kwargs.items():
            self.card_count[card_kwargs[card]] = count
        self.make_deck()
