""" Advent of code 2022 """


def get_data() -> list:
    """Get data from file."""
    with open('test_data.txt', 'r', encoding='utf-8') as the_file:
        data = the_file.read().splitlines()
        for line in data:
            print(line)
    return data


def part_one(_data) -> None:
    print(f"{part_one.__name__}:")


def part_two(_data) -> None:
    print(f"{part_two.__name__}:")


def main() -> None:
    data = get_data()
    part_one(data)
    part_two(data)


if __name__ == "__main__":
    main()
