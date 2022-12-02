import re


def get_data() -> list:
    print(f"{get_data.__name__}()")
    temp_data = []
    with open('data.txt', 'r', encoding='utf-8') as the_file:
        data = the_file.read().splitlines()
        for line in data:
            temp_data.append(line)
    return temp_data


def get_item_points(item) -> int:
    match item:
        case "rock":
            return 1
        case "paper":
            return 2
        case "scissors":
            return 3
        case _:
            return 0


def get_round_points(outcome) -> int:
    match outcome:
        case 1:
            return 6
        case 0:
            return 3
        case _:
            return 0


def calc_win(you, opp) -> int:
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


def get_loss_item(opp) -> str:
    match opp:
        case "rock":
            return "scissors"
        case "scissors":
            return "paper"
        case _:
            return "rock"


def get_win_item(opp) -> str:
    match opp:
        case "rock":
            return "paper"
        case "scissors":
            return "rock"
        case _:
            return "scissors"


def item_converter(letter) -> str:
    if letter in ('X', 'A'):
        return 'rock'
    if letter in ('Y', 'B'):
        return 'paper'
    if letter in ('Z', 'C'):
        return 'scissors'
    return ''


def part_two_conclusion(conclusion, opp) -> int:
    if conclusion == 'X':
        # loss
        your_item = get_loss_item(opp)
        return get_round_points(-1) + get_item_points(your_item)
    if conclusion == 'Z':
        # win
        your_item = get_win_item(opp)
        return get_round_points(1) + get_item_points(your_item)
    # draw
    your_item = opp
    return get_round_points(0) + get_item_points(your_item)


def part_one(data) -> None:
    print(f"\n{part_one.__name__}()\n---------")
    reg_data = re.compile(r'(\w) (\w)')
    total = 0
    for line in data:
        reg_result = reg_data.search(line)
        opp_regex = reg_result.group(1)
        you_regex = reg_result.group(2)
        you_item = item_converter(you_regex)
        opp_item = item_converter(opp_regex)
        is_win = calc_win(you_item, opp_item)
        round_points = get_round_points(is_win)
        item_points = get_item_points(you_item)
        round_total = round_points + item_points
        total += round_total
    print(f'{total=}')


def part_two(data) -> None:
    print(f"\n{part_two.__name__}()\n---------")
    reg_data = re.compile(r'(\w) (\w)')
    total = 0
    for line in data:
        reg_result = reg_data.search(line)
        opp_regex = reg_result.group(1)
        opp_item = item_converter(opp_regex)
        round_result = reg_result.group(2)
        total += part_two_conclusion(round_result, opp_item)
    print(f'{total=}')


def main() -> None:
    data = get_data()
    part_one(data)
    part_two(data)
    print("\n------\nexit()")


if __name__ == "__main__":
    main()
