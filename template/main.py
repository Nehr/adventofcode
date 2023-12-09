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


def part_one(data: list) -> None:
    logging.info("%s()", part_one.__name__)
    for line in data:
        logging.debug(line)
    logging.debug("end %s\n", part_one.__name__)


def part_two(data: list) -> None:
    logging.info("%s()", part_two.__name__)
    for line in data:
        logging.debug("%s", line)
    logging.debug("end %s\n", part_two.__name__)


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
    #part_two(data)
    logging.debug("end %s()", main.__name__)


if __name__ == "__main__":
    main()
