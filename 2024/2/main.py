""" Advent of code 2024 """

import enum
import logging
import argparse
import re
import time

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

def check_safe(first: int, second: int, is_lower: bool) -> bool:
    absolute = abs(first - second)
    if 0 < absolute <= 3:
        logging.debug("Within 3 and more than 0: %d, %d", first, second)
    else:
        logging.debug("Not within 3 or more than 0")
        return False

    if is_lower:
        logging.debug("Should be higher: %d > %d", first, second)
        if first > second:
            return True
    if not is_lower:
        logging.debug("Should be lower: %d < %d", first, second)
        if first < second:
            return True

    return False

def part_one(data: list) -> None:
    logging.info("%s()", part_one.__name__)
    total_safe: int = 0
    re_get_digits = re.compile(r'(\d+)\s*')
    for line in data:
        matches = re_get_digits.findall(line)
        logging.debug("Matches: %s", matches)
        is_lower = False
        if int(matches[0]) > int(matches[1]):
            is_lower = True
            logging.debug("Decreasing")
        else:
            logging.debug("Increasing")

        for i, _ in enumerate(matches):
            logging.debug("%d (%d/%d)", int(matches[i]), i, len(matches))
            if i < len(matches) - 1:
                first_num: int = int(matches[i])
                second_num: int = int(matches[i+1])
                if check_safe(first_num, second_num, is_lower):
                    pass
                else:
                    logging.debug("Unsafe row\n")
                    break
            if i == len(matches) - 1:
                logging.debug("Safe row\n")
                total_safe += 1

    logging.info("Total safe: %d", total_safe)

    logging.debug("end %s\n", part_one.__name__)

def part_two(data: list) -> None:
    logging.info("%s()", part_two.__name__)
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
    start_time = time.time()
    part_one(data)
    end_time = time.time()
    logging.info("Part one took %.2f seconds", end_time - start_time)
    # part_two(data)
    # end_time_part_two = time.time()
    # logging.info("Part two took %.2f seconds", end_time_part_two - end_time)
    logging.debug("end %s()", main.__name__)


if __name__ == "__main__":
    main()
