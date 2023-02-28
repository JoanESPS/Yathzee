import main


def test_dice_value():
    assert main.dice_value() in range(1, 7)


def test_five_dice_values():
    assert main.five_dice_values() in [range(1, 7), range(1, 7), range(1, 7), range(1, 7), range(1, 7)]
