""" Advent of code 2024 """

import enum
import logging
import argparse
import re


class FileType(enum.Enum):
    TEST = "test_data.txt"
    REAL = "data.txt"


def setup_logger(log_level: int = logging.INFO) -> None:
    """Setup for logging"""
    logger = logging.getLogger()
    logger.setLevel(log_level)

    ch = logging.StreamHandler()
    ch.setLevel(log_level)

    f = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    ch.setFormatter(f)

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

def get_lists(data: list) -> tuple:
    re_get_digits: str = re.compile(r'(\d+)\s+(\d+)')
    left_list: list = []
    right_list: list = []

    for line in data:
        matches = re_get_digits.match(line)
        if matches:
            left_list.append(int(matches.group(1)))
            right_list.append(int(matches.group(2)))
            logging.debug("left: %s, right: %s", matches.group(1), matches.group(2))

    return left_list, right_list

def part_one(data: list) -> None:
    logging.info("%s()", part_one.__name__)
    total: int = 0
    left_list, right_list = get_lists(data)

    left_list = sorted(left_list)
    right_list = sorted(right_list)

    for i, _ in enumerate(left_list):
        difference = left_list[i] - right_list[i]
        total += abs(difference)
        logging.debug("%d - %d: %d, total: %d", left_list[i], right_list[i], abs(difference), total)

    logging.info("Total: %d", total)
    logging.debug("end %s\n", part_one.__name__)


def part_two(data: list) -> None:
    logging.info("%s()", part_two.__name__)
    total: int = 0
    left_list, right_list = get_lists(data)

    for i, _ in enumerate(left_list):
        total += left_list[i] * right_list.count(left_list[i])

    logging.info("Total: %d", total)
    logging.debug("end %s\n", part_two.__name__)


def main() -> None:
    parser = argparse.ArgumentParser(description='Advent of code 2024')
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
    part_two(data)
    logging.debug("end %s()", main.__name__)


if __name__ == "__main__":
    main()
