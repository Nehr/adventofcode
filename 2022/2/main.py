import re

def get_data() -> list:
    print(f"{get_data.__name__}()")
    temp_data = []
    with open('test_data.txt', 'r', encoding='utf-8') as the_file:
        data = the_file.read().splitlines()
        for line in data:
            temp_data.append(line)
    return temp_data


def part_two(_data) -> None:
    print(f"{part_two.__name__}():")


def get_item_points(item):
    match item:
        case "rock":
            return 1
        case "paper":
            return 2
        case "scissors":
            return 3
        case _:
            return 0

def get_round_points(outcome):
    match outcome:
        case "win":
            return 6
        case "draw":
            return 3
        case _:
            return 0


def calc_win(you, opp):
    match you:
        case "rock":
            if opp == "paper":
                return -1
            if opp == "scissors":
                return 1
        case "paper":
            if opp == "scissors":
                return -1
            if opp == "rock":
                return 1
        case "scissors":
            if opp == "rock":
                return -1
            if opp == "paper":
                return 1
    return 0


# X for Rock, Y for Paper, and Z for Scissors
# A for Rock, B for Paper, and C for Scissors
def type_converter(letter):
    print(f"{letter=}")
    match letter:
        case ['X', 'A']:
            return 'rock'
        case ['Y', 'B']:
            return 'paper'
        case ['Z', 'C']:
            return 'scissors'


def part_one(data) -> None:
    print(f"{part_one.__name__}():")
    you_regex = re.compile(r'A|B|C')
    opp_regex = re.compile(r'X|Y|Z')
    for line in data:
        print(line)
        you_val = you_regex.search(line).group()
        print(f"{you_val=}")
        print(you_val == 'A')
        you_item = type_converter(you_val)
        print(f"{you_item=}")
        #print(you_val.group())
        opp_val = opp_regex.search(line).group()
        opp_item = type_converter(opp_val)
        print(f"{opp_item=}")
        #print(opp_val.group())
        is_win = calc_win(you_item, opp_item)
        print(f"{is_win=}")


def main() -> None:
    data = get_data()
    #print(data)
    part_one(data)
    part_two(data)


if __name__ == "__main__":
    main()
