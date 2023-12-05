import regex as re
"""
We are not using the standard re module here as it does not support searches for overlapping patterns.
This, however, is 
"""

extended_digit = re.compile(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))')
word_to_digit = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}


def calibrate_trebuchet(calibration_document: str):
    sum_ = 0
    with open(calibration_document) as file:
        for line in file.readlines():
            matches = re.findall(extended_digit, line, overlapped=True)
            if not matches:
                raise ValueError(f'Could not find a digit in line "{line}".')
            # If at least one digit was found, concatenate and add to sum_
            first_match = matches[0]
            first_digit = first_match if first_match.isdigit() else word_to_digit[first_match]
            if len(matches) == 1:
                second_digit = first_digit
            else:
                last_match = first_match if len(matches) == 1 else matches[-1]
                second_digit = last_match if last_match.isdigit() else word_to_digit[last_match]

            sum_ += int(first_digit + second_digit)
    return sum_


if __name__ == '__main__':
    print(calibrate_trebuchet('input.txt'))
