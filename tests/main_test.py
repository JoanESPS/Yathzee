import main
import mock
from Dice import Dice
from ScoreCard import init_score_card


def test_five_dices_values():
    for dice in main.hand.dices:
        assert dice.value in range(1, 7)


def test_sum_of_3_ones():
    # Arrange
    main.hand = [Dice(1), Dice(1), Dice(1), Dice(3), Dice(5)]
    # Act
    score_card = main.score_card_completion(main.hand)
    test_sum_of_three_ones = score_card['ones']
    # Assert
    assert test_sum_of_three_ones == 3


def test_sum_of_2_twos():
    # Arrange
    main.hand = [Dice(2), Dice(2), Dice(1), Dice(3), Dice(5)]
    # Act
    score_card = main.score_card_completion(main.hand)
    test_sum_of_two_twos = score_card['twos']
    # Assert
    assert test_sum_of_two_twos == 4


def test_chance():
    # Arrange
    main.hand = [Dice(1), Dice(2), Dice(1), Dice(4), Dice(5)]
    # Act
    score_card = main.score_card_completion(main.hand)
    test_of_chance_value = score_card['chance']
    # Assert
    assert test_of_chance_value == 13


def test_three_of_a_kind():
    # Arrange
    main.hand = [Dice(1), Dice(1), Dice(1), Dice(4), Dice(5)]
    # Act
    score_card = main.score_card_completion(main.hand)
    three_of_a_kind_value = score_card['three_of_a_kind']
    # Assert
    assert three_of_a_kind_value == 12


def test_four_of_a_kind():
    # Arrange
    main.hand = [Dice(1), Dice(1), Dice(1), Dice(1), Dice(5)]
    # Act
    score_card = main.score_card_completion(main.hand)
    four_of_a_kind_value = score_card['four_of_a_kind']
    # Assert
    assert four_of_a_kind_value == 9


def test_yahtzee():
    # Arrange
    main.hand = [Dice(1), Dice(1), Dice(1), Dice(1), Dice(1)]
    # Act
    score_card = main.score_card_completion(main.hand)
    yahtzee_value = score_card['yahtzee']
    # Assert
    assert yahtzee_value == 50


def test_full_house():
    # Arrange
    main.hand = [Dice(1), Dice(1), Dice(1), Dice(3), Dice(3)]
    # Act
    score_card = main.score_card_completion(main.hand)
    full_house_value = score_card['full_house']
    # Assert
    assert full_house_value == 25
