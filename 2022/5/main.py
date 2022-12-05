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
    for _amount in range(num):
        from_s = stack[from_stack]
        to_s = stack[to_stack]
        to_s.insert(0, from_s.pop(0))


def part_one(data) -> None:
    print(f"\n{part_one.__name__}()\n---------")
    stacks = {}
    add_to_stacks = True
    line_stacks = []
    directions = re.compile(r'move (\d+) from (\d+) to (\d+)')
    for line in data:
        if add_to_stacks is False:
            action = directions.search(line).groups()
            move_to_stack(stacks, int(action[0]), int(action[1]), int(action[2]))
            stacks = dict(sorted(stacks.items()))
        if add_to_stacks is True:
            line_stacks.append(line)
        if line.strip() == "":
            stacks = create_stacks(line_stacks)
            add_to_stacks = False
    result = ''
    for top_val in stacks.values():
        if len(top_val) > 0:
            result += top_val[0]
    print(f'{result=}')


def part_two(_data) -> None:
    print(f"\n{part_two.__name__}()\n---------")
    # for line in data:
    #    print(line)


def main() -> None:
    data = get_data(True)
    part_one(data)
    part_two(data)
    print("\n------\nexit()")


if __name__ == "__main__":
    main()
