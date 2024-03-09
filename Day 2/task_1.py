def game_number_and_content(aline):
    aline = aline.split(":")
    game_num = filter(str.isdecimal, aline[0])
    game_num = "".join(game_num)
    game_cont = aline[1]
    return game_num, game_cont


def get_colour_and_number(a_colour):
    a_colour = a_colour.split(" ")
    a_colour = list(filter(None, a_colour))
    return a_colour


def insert_missing_colours(this_set):
    colours = ("red", "green", "blue")
    for colour in colours:
        if not (any(text.endswith(colour) for text in this_set)):
            this_set.append("0 " + colour)
    return this_set


with open('puzzle_input') as f:
    document = f.read().splitlines()

dice_game_dictionary = {}

for line in document:
    split_line = game_number_and_content(line)
    game_numb = split_line[0]
    game_content = split_line[1]
    game_content = game_content.split(";")
    number_of_sets = len(game_content)
    sets = {}

    for set_number in range(number_of_sets):
        one_set = game_content[set_number]
        one_set = one_set.split(",")
        insert_missing_colours(one_set)
        a_set = {}

        for numb in range(len(one_set)):
            one_colour = one_set[numb]
            colour_number = {get_colour_and_number(one_colour)[1]: int(get_colour_and_number(one_colour)[0])}
            a_set.update(colour_number)

        a_set = {set_number + 1: a_set}
        sets.update(a_set)

    sets = {int(game_numb): sets}
    dice_game_dictionary.update(sets)

result = 0

for game_id in dice_game_dictionary:
    this_id = 0

    for set_id in dice_game_dictionary[game_id]:

        if dice_game_dictionary[game_id][set_id]["red"] <= 12 \
                and dice_game_dictionary[game_id][set_id]["green"] <= 13 \
                and dice_game_dictionary[game_id][set_id]["blue"] <= 14:
            this_id += 1

        if this_id == len(dice_game_dictionary[game_id]):
            result += game_id

print(result)

