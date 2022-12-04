""" Advent of code 2022 """


def get_data(is_test: bool) -> list:
    """Get data from file."""
    file_name = 'data.txt' if is_test is True else 'test_data.txt'
    with open(file_name, 'r', encoding='utf-8') as the_file:
        return the_file.read().splitlines()


def part_one(data) -> None:
    print(f"\n{part_one.__name__}()\n---------")
    for line in data:
        print(line)


def part_two(data) -> None:
    print(f"\n{part_two.__name__}()\n---------")
    for line in data:
        print(line)


def main() -> None:
    data = get_data(False)
    part_one(data)
    part_two(data)
    print("\n------\nexit()")


if __name__ == "__main__":
    main()
