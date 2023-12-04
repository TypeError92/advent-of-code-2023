from day_02.day_02 import parse, is_compatible


def test_parser():
    assert (parse('Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green') ==
            (1,
             [
                 {'red': 4, 'green': 0, 'blue': 3},
                 {'red': 1, 'green': 2, 'blue': 6},
                 {'red': 0, 'green': 2, 'blue': 0}
             ]
             )
            )


def test_is_compatible():
    sum_of_ids = 0
    with open('example.txt') as file:
        for line in file.readlines():
            game_id, game = parse(line)
            if is_compatible(game, {'red': 12, 'green': 13, 'blue': 14}):
                sum_of_ids += game_id
    assert sum_of_ids == 8
