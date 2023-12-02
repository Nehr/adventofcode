""" Advent of code 2023 """

import enum
import logging
import re


MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14


class FileType(enum.Enum):
    TEST = "test_data.txt"
    REAL = "data.txt"


def setup_logger(log_level: int = logging.INFO) -> None:
    """Setup for logging"""
    logger = logging.getLogger()
    logger.setLevel(log_level)

    ch = logging.StreamHandler()
    ch.setLevel(log_level)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
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


def get_game_num(line: str) -> int:
    match = re.search(r'Game (\d+):', line)
    if match:
        return int(match.group(1))
    else:
        return 0


def check_rgb(line: str) -> bool:
    blue_match = re.findall(r'(\d+) blue', line)
    if blue_match:
        for match in blue_match:
            logging.debug("blue match: %s", match)
            if int(match) > MAX_BLUE:
                return False
    red_match = re.findall(r'(\d+) red', line)
    if red_match:
        for match in red_match:
            logging.debug("red match: %s", match)
            if int(match) > MAX_RED:
                return False
    green_match = re.findall(r'(\d+) green', line)
    if green_match:
        for match in green_match:
            logging.debug("green match: %s", match)
            if int(match) > MAX_GREEN:
                return False
    
    return True


def part_one(data: list) -> None:
    logging.debug("%s()", part_one.__name__)
    total = 0

    for line in data:
        logging.debug(line)
        rgb_check = check_rgb(line)
        logging.debug(rgb_check)
        if rgb_check is True:
            game_num = get_game_num(line)
            logging.info("game: %s", game_num)
            total += int(game_num)

    logging.info("total: %s", total)
    logging.debug("end %s\n", part_one.__name__)


def part_two(data: list) -> None:
    logging.debug("%s()", part_two.__name__)
    total = 0
    for line in data:
        logging.debug("%s 2", line)
        num = get_highest_multiplied(line)
        logging.debug("num: %s", num)
        total += num
    logging.info("total: %s", total)
    logging.debug("end %s\n", part_two.__name__)


def get_highest_multiplied(line: str) -> int:
    blue = 0
    red = 0
    green = 0
    blue_match = re.findall(r'(\d+) blue', line)
    if blue_match:
        logging.debug("blue match: %s", blue_match)
        blue = max(map(int, blue_match))
        logging.debug("max blue: %s", blue)
    red_match = re.findall(r'(\d+) red', line)
    if red_match:
        logging.debug("red match: %s", red_match)
        red = max(map(int, red_match))
        logging.debug("max red: %s", red)
    green_match = re.findall(r'(\d+) green', line)
    if green_match:
        logging.debug("green match: %s", green_match)
        green = max(map(int, green_match))
        logging.debug("max green: %s", green)
    return red*blue*green


def main() -> None:
    setup_logger(logging.INFO)
    file_type = FileType.REAL
    data = get_data(file_type)
    #part_one(data)
    part_two(data)
    logging.debug("exit()")


if __name__ == "__main__":
    main()
