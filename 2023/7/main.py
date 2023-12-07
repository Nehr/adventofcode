""" Advent of code 2023 """

import enum
import logging
from collections import Counter


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


class PokerHandWinning(enum.Enum):
    HIGH_CARD = 'high_card'
    ONE_PAIR = 'one_pair'
    TWO_PAIRS = 'two_pairs'
    THREE_OF_A_KIND = 'three_of_a_kind'
    FULL_HOUSE = 'full_house'
    FOUR_OF_A_KIND = 'four_of_a_kind'
    FIVE_OF_A_KIND = 'five_of_a_kind'


class PokerHandObject:
    def __init__(self, hand: str, winnings: int) -> None:
        self.hand = hand
        self.winnings = winnings
    def __str__(self) -> str:
        return f'PokerHandObject (hand={self.hand}, winnings={self.winnings})'


def check_hand(hand: PokerHandObject) -> PokerHandWinning:
    logging.debug("%s()", check_hand.__name__)
    logging.debug("hand: %s, winnings: %s", hand.hand, hand.winnings)
    
    counts = Counter(hand.hand)
    counts_values = list(counts.values())
    counts_values.sort(reverse=True)

    if counts_values[0] == 5:
        return PokerHandWinning.FIVE_OF_A_KIND
    elif counts_values[0] == 4:
        return PokerHandWinning.FOUR_OF_A_KIND
    elif counts_values[0] == 3 and counts_values[1] == 2:
        return PokerHandWinning.FULL_HOUSE
    elif counts_values[0] == 3:
        return PokerHandWinning.THREE_OF_A_KIND
    elif counts_values[0] == 2 and counts_values[1] == 2:
        return PokerHandWinning.TWO_PAIRS
    elif counts_values[0] == 2:
        return PokerHandWinning.ONE_PAIR
    else:
        return PokerHandWinning.HIGH_CARD


def sort_by_custom_order(array: list) -> list:
    order = 'AKQJT98765432'
    return sorted(array, key=lambda x: [order.index(i) for i in x.hand], reverse=True)


def part_one(data: list) -> None:
    logging.info("%s()", part_one.__name__)
    poker_hands = {
        'high_card': [],
        'one_pair': [],
        'two_pairs': [],
        'three_of_a_kind': [],
        'full_house': [],
        'four_of_a_kind': [],
        'five_of_a_kind': []
    }
    sorted_hands = {
        'high_card': [],
        'one_pair': [],
        'two_pairs': [],
        'three_of_a_kind': [],
        'full_house': [],
        'four_of_a_kind': [],
        'five_of_a_kind': []
    }
    for line in data:
        logging.debug(line)
        line_split = line.split()
        nums = line_split[0]
        winnings = int(line_split[1])
        logging.debug("nums: %s", nums)
        logging.debug("winnings: %s", winnings)
        hand_object = PokerHandObject(nums, winnings)
        logging.debug("hand_object: %s", hand_object)
        checked_hand = check_hand(hand_object)
        logging.debug("checked_hand: %s", checked_hand)
        poker_hands[checked_hand.value].append(hand_object)

    for key, value in poker_hands.items():
        logging.debug("%s is next up", key)
        if len(value) > 1:
            logging.debug("sorting %s (%s)", key, len(value))
            sorted_arr = sort_by_custom_order(value)
            sorted_hands[key] = sorted_arr
        else:
            logging.debug("no need to sort %s (%s)", key, len(value))
            sorted_hands[key] = value

    wins = 0
    total = 0
    for key, value in sorted_hands.items():
        logging.debug("sorted %s:", key)
        for hand in value:
            logging.debug(hand)
            wins += 1
            total += (hand.winnings * wins)
            logging.debug("hand: %s * wins: %s = total: %s", hand.winnings, wins, total)
    logging.info("total: %s", total)


    logging.debug("end %s\n", part_one.__name__)


def part_two(data: list) -> None:
    logging.info("%s()", part_two.__name__)
    for line in data:
        logging.debug("%s 2", line)
    logging.debug("end %s\n", part_two.__name__)


def main() -> None:
    setup_logger(logging.INFO)
    file_type = FileType.REAL
    data = get_data(file_type)
    part_one(data)
    #part_two(data)
    logging.debug("exit()")


if __name__ == "__main__":
    main()
