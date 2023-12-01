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
        num_raw = re.sub('\D', '', line)
        num = int(num_raw[0] + num_raw[-1])
        #print(num_raw, num)
        total += num
    
    print("total: ", total)


def part_two(data: list) -> None:
    print(f"\n{part_two.__name__}()\n---------")
    for line in data:
        #print(line)
        new_line = replace_number(line)
        #print(new_line + "\n")


#def get_num_data(line: string):
#    num_raw = re.sub('\D', '', line)
#    num = int(num_raw[0] + num_raw[-1])


def replace_number(text: str) -> str:
    num_dict = {
      "one": "1",
      "two": "2",
      "three": "3",
      "four": "4",
      "five": "5",
      "six": "6",
      "seven": "7",
      "eight": "8",
      "nine": "9",
      "zero": "0"
    }
    
    for i, j in num_dict.items():
        text = text.replace(i, j)
    return text

def main() -> None:
    data = get_data(False)
    #part_one(data)
    part_two(data)
    print("\n------\nexit()")


if __name__ == "__main__":
    main()
