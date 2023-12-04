""" Advent of code 2023 """

import enum
import logging
import re


class FileType(enum.Enum):
    TEST = "test_data2.txt"
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


def get_card_data(line: str) -> dict or None:
    logging.debug("%s()", get_card_data.__name__)
    match = re.search(r'Card\s*(\d+):\s*((\d+\s*)*)\|', line)
    if match:
        logging.debug("card: %s", match.group(1))
        numbers = re.findall(r'\d+', match.group(2))
        winning_numbers = [int(num) for num in numbers]
        logging.debug("winning numbers: %s", winning_numbers)
        return {
            'card': int(match.group(1)),
            'winning_numbers': winning_numbers
        }
    return None


def get_user_data(line: str) -> list or None:
    logging.debug("%s()", get_user_data.__name__)
    match = re.search(r'\|\s*((\d+)\s*)*', line)
    if match:
        numbers = re.findall(r'\d+', match.group(0))
        user_data = [int(num) for num in numbers]
        logging.debug("user data: %s", user_data)
        return user_data
    return None


def count_common_numbers(card_array: list, user_data: list) -> int:
    return len(set(card_array) & set(user_data))


def count_winnings(wins: int) -> int:
    if wins > 0:
        return 2 ** (wins - 1)
    return 0


def part_one(data: list) -> None:
    logging.info("%s()", part_one.__name__)
    total = 0
    for line in data:
        logging.debug(line)
        card = get_card_data(line)
        if card is None:
            logging.error("card is None")
            continue
        card_array = card['winning_numbers']
        user_data = get_user_data(line)
        common_numbers_count = count_common_numbers(card_array, user_data)
        logging.debug("common numbers count: %s", common_numbers_count)
        wins = count_winnings(common_numbers_count)
        total += wins
        logging.debug("wins: %s", wins)
        logging.debug("")
    logging.info("total: %s", total)
    logging.debug("end %s\n", part_one.__name__)


def part_two(data: list) -> None:
    logging.info("%s()", part_two.__name__)
    for line in data:
        logging.debug("%s", line)
        card = get_card_data(line)
        if card is None:
            logging.error("card is None")
            continue
        card_array = card['winning_numbers']
        user_data = get_user_data(line)
        common_numbers_count = count_common_numbers(card_array, user_data)
        logging.debug("common numbers count: %s", common_numbers_count)
    logging.debug("end %s\n", part_two.__name__)


def main() -> None:
    setup_logger(logging.DEBUG)
    file_type = FileType.TEST
    data = get_data(file_type)
    #part_one(data)
    part_two(data)
    logging.debug("exit()")


if __name__ == "__main__":
    main()
