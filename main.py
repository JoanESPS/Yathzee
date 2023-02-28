import random
from Hand import Hand
from ScoreCard import init_score_card


hand = Hand()
hand.roll_dices()


def score_card_completion(player_hand):
    score_card = init_score_card()
    sum_of_dices_values = 0

    counter_by_value = [0, 0, 0, 0, 0, 0]
    for dice in player_hand:
        counter_by_value[dice.value - 1] += 1
        sum_of_dices_values += dice.value

    combination_names = list(score_card.keys())
    for i in range(6):
        score_card[combination_names[i]] += counter_by_value[i] * (i+1)

    score_card['chance'] = sum_of_dices_values

    if 3 in counter_by_value:
        score_card['three_of_a_kind'] = sum_of_dices_values

    if 4 in counter_by_value:
        score_card['four_of_a_kind'] = sum_of_dices_values

    return score_card
