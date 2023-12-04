import re


def calibrate_trebuchet(calibration_document: str):
    sum_ = 0
    with open(calibration_document) as file:
        for line in file.readlines():
            # Find the first digit
            first_digit = None
            for char in line:
                if char.isdigit():
                    first_digit = char
                    break
            if first_digit is None:
                raise ValueError

            # Find the second digit
            second_digit = None
            for char in line[::-1]:
                if char.isdigit():
                    second_digit = char
                    break

            # If at least one digit was found, concatenate and add to sum_
            sum_ += int(first_digit + second_digit)

    return sum_


if __name__ == '__main__':
    print(calibrate_trebuchet('input.txt'))
