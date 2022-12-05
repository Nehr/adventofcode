import re


def get_data(is_test: bool) -> list:
    """Get data from file."""
    file_name = 'data.txt' if is_test is True else 'test_data.txt'
    with open(file_name, 'r', encoding='utf-8') as the_file:
        return the_file.read().splitlines()


def create_stacks(data: list) -> dict:
    stacks = {}
    for line in data:
        char_num = 0
        for char in line:
            if char.isalpha() and line.index(char) % 4 == 1:
                stack_num = int((char_num - 1) / 4 + 1)
                if stack_num not in stacks:
                    stacks[stack_num] = []
                stacks[stack_num].append(char)
            char_num += 1
    return stacks


def move_to_stack(stack: dict, num: int, from_stack: int, to_stack: int):
    for _ in range(num):
        from_s = stack[from_stack]
        to_s = stack[to_stack]
        to_s.insert(0, from_s.pop(0))


def move_multiple_to_stack(stack: dict, num: int, from_stack: int, to_stack: int):
    old_stack = stack[from_stack]
    updated_new_stack = old_stack[0:num] + stack[to_stack]
    updated_old_stack = old_stack[num:]
    stack[from_stack] = updated_old_stack
    stack[to_stack] = updated_new_stack


def get_separated_data(data: list) -> dict:
    stacks = {}
    actions = []
    add_to_stacks = True
    line_stacks = []
    count = 0
    for line in data:
        if add_to_stacks is False:
            actions = data[count:]
            break
        if add_to_stacks is True:
            line_stacks.append(line)
        if line.strip() == "":
            stacks = create_stacks(line_stacks)
            add_to_stacks = False
        count += 1
    return {
        "stacks": dict(sorted(stacks.items())),
        "actions": actions
    }


def print_result(data: dict) -> None:
    result = ''
    for top_val in data.values():
        if len(top_val) > 0:
            result += top_val[0]
    print(f'{result=}')


def part_one(data: list) -> None:
    print(f"\n{part_one.__name__}()\n---------")
    directions = re.compile(r'move (\d+) from (\d+) to (\d+)')
    new_data = get_separated_data(data)
    for line in new_data["actions"]:
        action = directions.search(line).groups()
        move_to_stack(new_data["stacks"], int(action[0]), int(action[1]), int(action[2]))
    print_result(new_data["stacks"])


def part_two(data: list) -> None:
    print(f"\n{part_two.__name__}()\n---------")
    new_data = get_separated_data(data)
    directions = re.compile(r'move (\d+) from (\d+) to (\d+)')
    for line in new_data["actions"]:
        action = directions.search(line).groups()
        move_multiple_to_stack(new_data["stacks"], int(action[0]), int(action[1]), int(action[2]))
    print_result(new_data["stacks"])


def print_data(data: list, test: bool) -> None:
    print("\nDATA\n------\n")
    for line in range(9) if test is True else range(4):
        print(data[line])


def main() -> None:
    real_data = True
    data = get_data(real_data)
    print_data(data, real_data)
    part_one(data)
    part_two(data)
    print("\n------\nexit()")


if __name__ == "__main__":
    main()
