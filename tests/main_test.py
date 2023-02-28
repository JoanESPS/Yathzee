import main

def test_dice_value():
    assert main.dice_value() in range(1, 7)
