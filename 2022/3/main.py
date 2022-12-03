import string


def get_data() -> list:
    """Get data from file."""
    with open('data.txt', 'r', encoding='utf-8') as the_file:
        return the_file.read().splitlines()


def get_char_value(char: str) -> int:
    if char.islower():
        return string.ascii_lowercase.index(char) + 1
    return string.ascii_uppercase.index(char) + 27


def get_match(data: list) -> str | None:
    if len(data) == 2:
        return ''.join(set(data[0]).intersection(data[1]))
    if len(data) == 3:
        return ''.join(set(data[0]) & set(data[1]) & set(data[2]))
    return None


def part_one(data: list) -> None:
    print(f"\n{part_one.__name__}()\n---------")
    total = 0
    for rucksack in data:
        split_at = int(len(rucksack) / 2)
        comps = [rucksack[0:split_at], rucksack[split_at:None]]
        matching_char = get_match(comps)
        char_val = get_char_value(matching_char)
        total += char_val
    print(f"{total=}")


def part_two(data: list) -> None:
    print(f"\n{part_two.__name__}()\n---------")
    index = 0
    total = 0
    for _rucksack in data[::3]:
        #print(f"{index=}")
        comps = [data[index], data[index + 1], data[index + 2]]
        matching_char = get_match(comps)
        #print(f"{matching_char=}")
        if matching_char is not None:
            total += get_char_value(matching_char)
        else:
            print(f"{comps=}")
            raise Exception("No matching character")
        index += 3
    print(f"{total=}")


def main() -> None:
    data = get_data()
    part_one(data)
    part_two(data)
    print("\n------\nexit()")


if __name__ == "__main__":
    main()
