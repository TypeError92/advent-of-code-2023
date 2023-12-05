def parse(line):
    line = line.rstrip('\n ')
    game_id, subsets = line[5:].split(': ')
    parsed_subsets = []
    for subset in subsets.split('; '):
        rgb = {'red': 0, 'green': 0, 'blue': 0}
        for group in subset.split(', '):
            count, colour = group.split(' ')
            rgb[colour] += int(count)
        parsed_subsets.append(rgb)
    return int(game_id), parsed_subsets


def is_compatible(game, bag):
    total = sum(bag.values())
    for subset in game:
        for colour in ('red', 'green', 'blue'):
            if subset[colour] > bag[colour]:
                return False
    return True


def power(set_of_cubes):
    return set_of_cubes['red'] * set_of_cubes['green'] * set_of_cubes['blue']


def minimum_counts(game):
    min_counts = {'red': 0, 'green': 0, 'blue': 0}
    for subset in game:
        for colour in ('red', 'green', 'blue'):
            if (count := subset[colour]) > min_counts[colour]:
                min_counts[colour] = count
    return min_counts


if __name__ == '__main__':
    sum_of_ids = 0
    sum_of_powers_of_min_counts = 0
    with open('input.txt') as file:
        for line in file.readlines():
            game_id, game = parse(line)
            if is_compatible(game, {'red': 12, 'green': 13, 'blue': 14}):
                sum_of_ids += game_id
            sum_of_powers_of_min_counts += power(minimum_counts(game))
    print("Solution for Part 1:", sum_of_ids)
    print("Solution for Part 2:", sum_of_powers_of_min_counts)

