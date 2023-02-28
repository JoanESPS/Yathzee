import main
import mock
from Dice import Dice


def test_five_dices_values():
    for dice in main.hand.dices:
        assert dice.value in range(1, 7)


def test_sum_of_3_ones():
    # Arrange
    main.hand = [Dice(1), Dice(1), Dice(1), Dice(3), Dice(5)]
    # Act
    test_sum_of_three_ones = main.sum_of_ones(main.hand)
    # Assert
    assert test_sum_of_three_ones == 3

def test_sum_of_2_twos():
    # Arrange
    main.hand = [Dice(2), Dice(2), Dice(1), Dice(3), Dice(5)]
    # Act
    test_sum_of_two_twos = main.sum_of_twos(main.hand)
    # Assert
    assert test_sum_of_three_ones == 4
