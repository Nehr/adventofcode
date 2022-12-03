""" Advent of code 2022 """


def get_data() -> list:
    """Get data from file."""
    with open('test_data.txt', 'r', encoding='utf-8') as the_file:
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
    data = get_data()
    part_one(data)
    part_two(data)
    print("\n------\nexit()")


if __name__ == "__main__":
    main()
