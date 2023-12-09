""" Advent of code 2023 """

import enum
import logging
import argparse


class FileType(enum.Enum):
    TEST = "test_data.txt"
    REAL = "data.txt"


def setup_logger(log_level: int = logging.INFO) -> None:
    """Setup for logging"""
    logger = logging.getLogger()
    logger.setLevel(log_level)

    ch = logging.StreamHandler()
    ch.setLevel(log_level)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', 
                                  datefmt='%Y-%m-%d %H:%M:%S')
    ch.setFormatter(formatter)

    logger.addHandler(ch)


def get_data(file_type: FileType) -> list:
    """Get data from file."""
    file_name = file_type.value
    try:
        with open(file_name, 'r', encoding='utf-8') as the_file:
            return the_file.read().splitlines()
    except FileNotFoundError:
        logging.error("File not found: %s", file_name)
        return []


def get_differences(val_arr: list) -> list:
    current_differences = []
    for i, val in enumerate(val_arr):
        #logging.debug("current value, index: %s, %s", val, i)
        if i == len(val_arr) - 1:
            #logging.debug("last value, index: %s, %s", val, i)
            break
        #logging.debug("current value: %s, next value: %s, index: %s", val, val_arr[i+1], i+1)
        current_differences.append(int(val_arr[i+1]) - int(val))
    return current_differences


class DifferenceObject:
    def __init__(self, index: int, original_values: list, difference: list, answer: int):
        self.difference = difference
        self.index = index
        self.answer = answer
        self.original_values = original_values
    def __str__(self) -> str:
        return str(self.answer)


def part_one(data: list) -> None:
    logging.info("%s()", part_one.__name__)
    values = []
    answers = {}
    total = 0
    for line in data:
        #logging.debug(line)
        values.extend([line.split()])
    #logging.debug("values: %s", values)
    for index, val_arr in enumerate(values):
        #logging.debug("val_arr: %s", val_arr)
        diff_list = []
        last_diffs = get_differences(val_arr)
        diff_list.append(last_diffs)
        running = True
        while running is True:
            diffs = get_differences(last_diffs)
            #logging.debug("diffs: %s", diffs)
            diff_list.append(diffs)
            last_diffs = diffs
            if all(diff == 0 for diff in last_diffs):
                #logging.debug("All differences are zero.")
                running = False
                continue
        
        answers[index] = DifferenceObject(index, val_arr, list(reversed(diff_list)), 0)
    for _key, ans in answers.items():
        logging.debug("original values: %s", ans.original_values)
        logging.debug("index: %s, difference: %s (%s), answer: %s", ans.index, len(ans.difference), ans.difference, ans.answer)
        for ind, diff in enumerate(ans.difference):
            logging.debug("Difference: %s, index: %s", diff, ind)
            if len(ans.difference) >= ind + 1:
                if ind > 0:
                    last_num = ans.difference[ind - 1][-1]
                else:
                    last_num = 0
                logging.debug("last_num: %s", last_num)
                new_num = diff[-1] + last_num
                ans.difference[ind].append(new_num)
                logging.debug("ans.difference[ind + 1]: %s, new_num: %s", ans.difference[ind], new_num)
        new_og = ans.difference[-1][-1] + int(ans.original_values[-1])
        logging.debug("last number to add to og: %s", new_og)
        ans.original_values.append(new_og)
        logging.debug("new original values: %s", ans.original_values)
        total += new_og
        logging.debug("")
    logging.info("Total: %s", total)

def part_two(data: list) -> None:
    logging.info("%s()", part_two.__name__)
    for line in data:
        logging.debug("%s", line)


def main() -> None:
    parser = argparse.ArgumentParser(description='Advent of code 2023')
    parser.add_argument('--real', action='store_true', default=False)
    args = parser.parse_args()

    if args.real:
        setup_logger(logging.INFO)
        file_type = FileType.REAL
    else:
        setup_logger(logging.DEBUG)
        file_type = FileType.TEST
    data = get_data(file_type)
    part_one(data)
    logging.debug("end %s\n", part_one.__name__)
    #part_two(data)
    logging.debug("end %s\n", part_two.__name__)
    logging.debug("end %s()", main.__name__)


if __name__ == "__main__":
    main()
