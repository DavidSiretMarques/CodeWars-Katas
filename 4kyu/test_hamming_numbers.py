import hamming_numbers as hn


def test_hamming_10_first():
    assert [hn.hamming(i+1) for i in range(10)] == [1, 2, 3, 4, 5, 6, 8, 9, 10, 12]


