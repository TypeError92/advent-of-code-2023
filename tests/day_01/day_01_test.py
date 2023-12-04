from day_01.day_01 import calibrate_trebuchet


def test_day_01():
    assert calibrate_trebuchet("example1.txt") == 142
    assert calibrate_trebuchet("example2.txt") == 281
