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
        if sum(subset.values()) > total:
            return False
        for colour in ('red', 'green', 'blue'):
            if subset[colour] > bag[colour]:
                return False
    return True


if __name__ == '__main__':
    sum_of_ids = 0
    with open('input.txt') as file:
        for line in file.readlines():
            game_id, game = parse(line)
            if is_compatible(game, {'red': 12, 'green': 13, 'blue': 14}):
                sum_of_ids += game_id
    print(sum_of_ids)

