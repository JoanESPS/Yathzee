import random
from Hand import Hand
from Dice import Dice
from ScoreCard import init_score_card

hand = Hand()
hand.roll_dices()


def score_card_completion(player_hand):
    score_card = init_score_card()
    sum_of_dices_values = 0

    counter_by_value = [0, 0, 0, 0, 0, 0]
    for dice in player_hand.dices:
        counter_by_value[dice.value - 1] += 1
        sum_of_dices_values += dice.value

    combination_names = list(score_card.keys())
    for i in range(6):
        score_card[combination_names[i]] += counter_by_value[i] * (i + 1)

    score_card['chance'] = sum_of_dices_values

    if 3 in counter_by_value:
        score_card['three_of_a_kind'] = sum_of_dices_values
        if 2 in counter_by_value:
            score_card['full_house'] = 25

    if 4 in counter_by_value:
        score_card['four_of_a_kind'] = sum_of_dices_values

    if 5 in counter_by_value:
        score_card['yahtzee'] = 50

    if (counter_by_value[2] != 0 and counter_by_value[3] != 0
            and counter_by_value[0] != 0 and counter_by_value[1] != 0
                                        or counter_by_value[1] != 0 and counter_by_value[4] != 0
                                        or counter_by_value[4] != 0 and counter_by_value[5] != 0):
        score_card['small_straight'] = 30

    if (counter_by_value[1] != 0 and counter_by_value[2] != 0 and counter_by_value[3] != 0 and counter_by_value[4] != 0
            and (counter_by_value[0] != 0 or counter_by_value[5] != 0)):
        score_card['large_straight'] = 40

    return score_card


print(f'Ma main est : {hand.dices}')
score_card = score_card_completion(hand)
print(score_card)

