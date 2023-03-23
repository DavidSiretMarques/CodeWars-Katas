from count_the_smiley_faces import count_smileys


def test_empty_array():
    assert count_smileys([]) == 0


def test_all_correct_smileys():
    assert count_smileys([':D', ':-)', ';~D', ':)']) == 4


def test_some_wrong_smileys():
    assert count_smileys([':)', ':(', ':D', ':O', ':;', ':·)', '=)']) == 2


def test_all_wrong_smileys():
    assert count_smileys([':(', ':O', ':;', ':·)', '=)', '::::', ':']) == 0
