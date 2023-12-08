""" Advent of code 2023 """

import enum
import logging
import argparse
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


def get_instructions(data: list) -> str:
    return data[0]


def create_nodes(data: list) -> dict:
    nodes = {}
    found_start = False
    for line in data:
        match = re.match(r'(\w+)\s*=\s*\((\w+),\s*(\w+)\)', line)
        if match:
            if not found_start:
                nodes['start'] = match.group(1)
                found_start = True
            logging.debug("match: %s = %s, %s", match.group(1), match.group(2), match.group(3))
            nodes[match.group(1)] = {
                'L': match.group(2),
                'R': match.group(3)
            }
    return nodes


def part_one(data: list) -> None:
    logging.info("%s()", part_one.__name__)
    instructions = get_instructions(data)
    logging.debug("instructions: %s", instructions)
    nodes = create_nodes(data)
    logging.debug("nodes: %s", nodes)
    steps = 0
    current_node = 'AAA'
    logging.debug("starting node: %s, steps: %s", current_node, steps)
    while True:
        for s in instructions:
            steps += 1
            logging.debug("this instruction: %s", s)
            logging.debug("node info: %s", nodes[current_node])
            current_node = nodes[current_node][s]
            logging.debug("current_node: %s, steps: %s", current_node, steps)
            if current_node == 'ZZZ':
                logging.info("found ZZZ! total steps needed: %s", steps)
                return


def part_two(data: list) -> None:
    logging.info("%s()", part_two.__name__)
    for line in data:
        logging.debug("%s 2", line)
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
    logging.debug("end %s\n", part_one.__name__)
    logging.debug("exit()")


if __name__ == "__main__":
    main()
