import main


def test_dice_value():
    assert main.dice_value() in range(1, 7)


def test_five_dices_values():
    dices_values = main.five_dices_values()
    for dice_value in dices_values:
        assert dice_value in range(1, 7)
