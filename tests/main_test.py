import main
import mock


def test_five_dices_values():
    for dice in main.hand.dices:
        assert dice.value in range(1, 7)


@mock.patch('main.sum_of_ones')
def test_sum_of_3_ones():
    # Arrange
    main.hand = [1, 1, 1, 3, 5]
    # Act
    test_sum_of_three_ones = main.sum_of_ones(main.hand)
    # Assert
    assert test_sum_of_three_ones == 3
