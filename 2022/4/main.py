""" Advent of code 2022 """
import re


def get_data() -> list:
    """Get data from file."""
    with open('data.txt', 'r', encoding='utf-8') as the_file:
        return the_file.read().splitlines()


def num_within(data: list) -> int:
    first_list = data[0]
    first_min = int(first_list[0])
    first_max = (int(first_list[1]) + 1)
    second_list = data[1]
    second_min = int(second_list[0])
    second_max = (int(second_list[1]) + 1)
    if first_min in range(second_min, second_max) and first_max in range(second_min, second_max):
        #print("\nfirst is within second")
        return 1
    if second_min in range(first_min, first_max) and second_max in range(first_min, first_max):
        #print("\nsecond is within first")
        return 1
    return 0


def build_full_list(num_a: int, num_b: int) -> list:
    data = []
    for num in range(num_a, num_b + 1):
        data.append(num)
    return data


def get_any_overlap(data: list) -> int:
    first = list(map(int, data[0]))
    second = list(map(int, data[1]))
    one = build_full_list(first[0], first[1])
    two = build_full_list(second[0], second[1])
    return 1 if any(num in one for num in two) else 0


def part_one(data) -> None:
    print(f"\n{part_one.__name__}()\n---------")
    reg_data = re.compile(r'(\d+)-(\d+)')
    total = 0
    for line in data:
        reg_result = reg_data.findall(line)
        num = num_within(reg_result)
        total += num
    print(f"{total=}")


def part_two(data) -> None:
    print(f"\n{part_two.__name__}()\n---------")
    reg_data = re.compile(r'(\d+)-(\d+)')
    total = 0
    for line in data:
        reg_result = reg_data.findall(line)
        overlap = get_any_overlap(reg_result)
        #print(reg_result, overlap)
        total += overlap
    print(f"{total=}")


def main() -> None:
    data = get_data()
    part_one(data)
    part_two(data)
    print("\n------\nexit()")


if __name__ == "__main__":
    main()
