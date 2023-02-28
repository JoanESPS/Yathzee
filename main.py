import random
from Hand import Hand
from ScoreCard import init_score_card


hand = Hand()
hand.roll_dices()


def sum_of_dices_by_value(player_hand):
    score_card = init_score_card()
    combination_names = list(score_card.keys())
    for dice in player_hand:
        score_card[combination_names[dice.value - 1]] += dice.value
        score_card['chance'] += dice.value
    return score_card


def three_ok_a_kind(player_hand):
    score_card = init_score_card()
    counter_by_value = [0, 0, 0, 0, 0, 0]
    for dice in player_hand:
        counter_by_value[dice.value - 1] += 1
    if 3 in counter_by_value:
        score = 0
        for i in range(1, 7):
            score += (i * counter_by_value[i-1])
        score_card["three_of_a_kind"] = score
    return score_card
