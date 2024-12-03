""" Advent of code 2023 """

import enum
import logging
import argparse
import time
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


def get_data(file_type: FileType) -> str:
    """Get data from file."""
    file_name = file_type.value
    try:
        with open(file_name, 'r', encoding='utf-8') as the_file:
            return the_file.read()
    except FileNotFoundError:
        logging.error("File not found: %s", file_name)
        return []


def part_one(data: str) -> None:
    start_time = time.time()
    logging.info("%s()", part_one.__name__)
    total: int = 0
    get_multipliers = re.compile(r'mul\((\d+),(\d+)\)')
    matches = get_multipliers.findall(data)
    if matches:
        logging.debug("matches: %s", matches)
        for match in matches:
            total += int(match[0]) * int(match[1])
    logging.info("total: %s", total)
    end_time = time.time()
    logging.info("end %s in %.2f seconds\n", part_one.__name__, end_time - start_time)


def part_two(data: str) -> None:
    start_time = time.time()
    logging.info("%s()", part_two.__name__)
    total: int = 0

    get_between_dont_do = re.compile(r'don\'t\(\).*?do\(\)', re.DOTALL)
    get_multipliers = re.compile(r'mul\((\d+),(\d+)\)')

    data = get_between_dont_do.sub('', data)

    matches = get_multipliers.findall(data)
    if matches:
        logging.debug("matches: %s", matches)
        for match in matches:
            total += int(match[0]) * int(match[1])

    logging.info("total: %s", total)
    end_time = time.time()
    logging.info("end %s in %.2f seconds\n", part_two.__name__, end_time - start_time)

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
