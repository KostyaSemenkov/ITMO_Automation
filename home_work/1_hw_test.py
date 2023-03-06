def test_equality_home_work():
    assert ('home', 'work') == ('home', 'work')


def test_equality_engeniers():
    assert 'QA' == 'QA'


def test_equality_numbers():
    assert not (1, 1, 2, 3, 5) == (2, 3, 5)