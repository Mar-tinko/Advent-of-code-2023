def game_number_and_content(aline):
    aline = aline.split(":")
    game_num = filter(str.isdecimal, aline[0])
    game_num = "".join(game_num)
    game_cont = aline[1]
    return game_num, game_cont


def get_colour_and_number(a_set):
    a_set = a_set.split(" ")
    a_set = list(filter(None, a_set))
    return a_set


def insert_missing_colours(this_set):
    colours = ("red", "green", "blue")
    for colour in colours:
        if not (any(text.endswith(colour) for text in this_set)):
            this_set.append("0 " + colour)
    return this_set


def highest_number_list(colour_number_list):
    highest_number_list = []
    colour_number_list.sort(reverse=True)
    highest_number_list.append(colour_number_list[0])
    return highest_number_list


def multiply_mylist(mylist):
    resultt = 1
    for numberrs in mylist:
        resultt = resultt * numberrs
    return resultt


def summarize_thelist(thelist):
    resulttt = 0
    for numberrrs in thelist:
        resulttt = resulttt + numberrrs
    return resulttt


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

color_number = []
colors = ["red", "green", "blue"]
factor_result = []
for game_id in dice_game_dictionary:
    highest_number = []

    for color in colors:
        for set_id in dice_game_dictionary[game_id]:
            color_number.append(dice_game_dictionary[game_id][set_id][color])
        highest_number.append(highest_number_list(color_number)[0])
        color_number.clear()
    factor_result.append(multiply_mylist(highest_number))
print(summarize_thelist(factor_result))

