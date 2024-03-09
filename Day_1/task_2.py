def replace_word_with_number(text):
    replacers = {
        "one": "o1e",
        "two": "t2o",
        "three": "t3e",
        "four": "f4r",
        "five": "f5e",
        "six": "s6x",
        "seven": "s7n",
        "eight": "e8t",
        "nine": "n9e"
    }
    for word, number in replacers.items():
        text = text.replace(word, number)
    return text


def get_digits(aline):
    digits = []
    for character in aline:
        if character.isdigit():
            digits.append(character)
    return digits


def combine_numbers(zwei_numbers):
    first_num = zwei_numbers[0]
    last_num = zwei_numbers[-1]
    combined_num = "%s%s" % (first_num, last_num)
    return int(combined_num)


with open('puzzle_input') as f:
    document = f.read().splitlines()

final_numbers = []
for line in document:
    replaced_line = replace_word_with_number(line)
    numbers = get_digits(replaced_line)
    combined_numbers = combine_numbers(numbers)
    final_numbers.append(combined_numbers)

result = sum(final_numbers)
print(result)
