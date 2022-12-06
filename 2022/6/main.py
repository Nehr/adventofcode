def get_data(is_test: bool) -> list:
    """Get data from file."""
    file_name = 'data.txt' if is_test is True else 'test_data.txt'
    with open(file_name, 'r', encoding='utf-8') as the_file:
        return the_file.read().splitlines()


def is_only_uniques(string: str) -> bool:
    return len(set(string)) == len(string)


def get_no_duplicates(data: str, num_chars: int) -> int:
    used = []
    current = data[0:num_chars]
    data = data[num_chars:]
    no_duplicates = False
    for char in data:
        used.append(current[0])
        current = current[1:] + char
        no_duplicates = is_only_uniques(current)
        if no_duplicates is True:
            return len(used) + len(current)
    return 0


def part_one(data: list, is_not_test: bool) -> None:
    print(f"\n{part_one.__name__}()\n---------")
    if is_not_test is True:
        result = get_no_duplicates(data[0], 4)
        print(f'{result=}')
    else:
        count = 0
        answers = [7, 5, 6, 10, 11]
        for line in data:
            result = get_no_duplicates(line, 4)
            print(f'{result=} -> expected={answers[count]}')
            count += 1


def part_two(data: list, is_not_test: bool) -> None:
    print(f"\n{part_two.__name__}()\n---------")
    if is_not_test is True:
        result = get_no_duplicates(data[0], 14)
        print(f'{result=}')
    else:
        count = 0
        answers = [19, 23, 23, 29, 26]
        for line in data:
            result = get_no_duplicates(line, 14)
            print(f'{result=} -> expected={answers[count]}')
            count += 1


def main() -> None:
    is_not_test = True
    data = get_data(is_not_test)
    part_one(data, is_not_test)
    part_two(data, is_not_test)
    print("\n------\nexit()")


if __name__ == "__main__":
    main()
