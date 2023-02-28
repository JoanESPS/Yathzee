import main


def test_five_dices_values():
    for dice in main.hand.dices:
        assert dice.value in range(1, 7)
