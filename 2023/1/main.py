""" Advent of code 2023 """
import re


def get_data(real_data: bool) -> list:
    """Get data from file."""
    file_name = "data.txt" if real_data is True else "test_data_2.txt"
    with open(file_name, "r", encoding="utf-8") as the_file:
        return the_file.read().splitlines()


def part_one(data: list) -> None:
    print(f"\n{part_one.__name__}()\n---------")
    total = 0
    for line in data:
        num = get_num_data(line)
        #print(num_raw, num)
        total += num
    
    print("total: ", total)


def part_two(data: list) -> None:
    print(f"\n{part_two.__name__}()\n---------")
    total = 0
    for line in data:
        #print(line)
        new_line = replace_number_text(line)
        #print(new_line)
        num = get_num_data(new_line)
        #print(str(num) + "\n")
        total += num

    print("total: ", total)



def get_num_data(line: str):
    num_raw = re.sub('\D', '', line)
    num = int(num_raw[0] + num_raw[-1])
    return num


def replace_number_text(text: str) -> str:
    num_dict = {
      "one": "o1e",
      "two": "t2o",
      "three": "t3e",
      "four": "f4r",
      "five": "f5e",
      "six": "s6x",
      "seven": "s7n",
      "eight": "e8h",
      "nine": "n9e",
      "zero": "z0o"
    }

    for i, j in num_dict.items():
        text = text.replace(i, j)

    return text

def main() -> None:
    data = get_data(True)
    part_one(data)
    part_two(data)
    print("\n------\nexit()")


if __name__ == "__main__":
    main()
