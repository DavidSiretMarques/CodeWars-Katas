from ball_upwards import max_ball


def test_zero_v():
    assert max_ball(0) == 0


def test_negative_v():
    assert max_ball(-3) == 0


def test_positive_v():
    assert max_ball(37) == 10


def test_very_big_v():
    assert max_ball(300_000_000_000) == 1000

