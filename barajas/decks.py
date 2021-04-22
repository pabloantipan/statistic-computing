import random
import collections

DECKS = ["club", "spades", "hearth", "diamond"]
VALUES = ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "jack", "queen", "king"]


def make_deck() -> list:
    decks = []
    for deck in DECKS:
        for value in VALUES:
            decks.append((deck, value))

    return decks


def get_hand(deck: list, hand_size: int) -> list:
    hand = random.sample(deck, hand_size)
    return hand


def build_royal_flush():
    target_values = ["ace", "king", "queen", "jack", "10"]
    target_deck = ["club", "spades", "hearth", "diamond"]

    result = []
    for deck in target_deck:
        for value in target_values:
            result.append((deck, value))

    return result


def proba_royal_flush(targethand: list, tries: int)->float:

    deck = make_deck()
    hands = []
    for _ in range(tries):
        hand = get_hand(deck, hand_size)
        hands.append(hand)

    appearances = 0
    for hand in hands:
        for card in hand:
            if card in 

    prob = pairs / tries

    return prob




def main(hand_size: int, tries: int):
    deck = make_deck()

    hands = []
    for _ in range(tries):
        hand = get_hand(deck, hand_size)
        hands.append(hand)

    pairs = 0
    for hand in hands:
        values = []
        for card in hand:
            values.append(card[1])
        # print(hand )
        # print(values)
        counter = dict(collections.Counter(values))
        for val in counter.values():
            if val == 3:
                pairs += 1
                break

    prob = pairs / tries

    return prob


if __name__ == "__main__":
    hand_size = 5
    tries = 100

    print(build_royal_flush())

    # pairs = main(hand_size, tries)
    # print(pairs)

    # deck = make_deck()
    # hand = get_hand(deck, 5)

    # # for card in deck:
    # #     print(card)
    # print("hand:", hand)
