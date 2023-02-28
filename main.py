import random
from Hand import Hand
from ScoreCard import score_card


hand = Hand()
hand.roll_dices()


def sum_of_dices_by_value(player_hand):
    combination_names = list(score_card.keys())
    for dice in player_hand:
        score_card[combination_names[dice.value - 1]] += dice.value
    return True

