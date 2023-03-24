"""
Note that pytest does not worry about covering every possibility of the regex
"""
import pytest
from strip_comments import strip_comments


def test_no_markers():
    assert strip_comments('apples, pears # and bananas\ngrapes\nbananas !apples', []) == \
           'apples, pears # and bananas\ngrapes\nbananas !apples'


@pytest.mark.parametrize('marker', [mark for mark in "!@#$§*^=?-.,';"])
def test_1_marker(marker):
    assert strip_comments('apples pears ' + marker + ' and bananas\ngrapes\nbananas ' +
                          marker + 'apples', [marker]) == 'apples pears\ngrapes\nbananas'


@pytest.mark.parametrize('marker1, marker2', [(marker1, marker2)
                                              for marker1 in "!@#$§*^=?-.,';"
                                              for marker2 in "!@#$§*^=?-.,';"])
def test_2_marker(marker1, marker2):
    assert strip_comments('apples pears ' + marker1 + ' and bananas\ngrapes\nbananas ' +
                          marker2 + 'apples', [marker1, marker2]) == 'apples pears\ngrapes\nbananas'


@pytest.mark.parametrize('marker1, marker2, marker3', [(marker1, marker2, marker3)
                                                       for marker1 in "!@#$§*^=?-.,';"
                                                       for marker2 in "!@#$§*^=?-.,';"
                                                       for marker3 in "!@#$§*^=?-.,';"])
def test_3_marker(marker1, marker2, marker3):
    assert strip_comments('apples pears ' + marker1 + ' and bananas\ngrapes' + marker2 + 'asdf\nbananas ' +
                          marker3 + 'apples', [marker1, marker2, marker3]) == 'apples pears\ngrapes\nbananas'
