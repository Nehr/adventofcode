""" Advent of code 2023 """

import enum
import logging
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


def extract_times_and_distances_part_one(data: list) -> dict:
    times = []
    distances = []
    for index, line in enumerate(data):
        for item in re.findall(r'(\d+)', line):
            if index == 0:
                times.append(int(item))
            else:
                distances.append(int(item))
    return {'times': times, 'distances': distances}


def extract_times_and_distances_part_two(data: list) -> dict:
    times = []
    distances = []
    for index, line in enumerate(data):
        new_line = ''.join(line.split())
        for item in re.findall(r'(\d+)', new_line):
            if index == 0:
                times.append(int(item))
            else:
                distances.append(int(item))
    return {'times': times, 'distances': distances}


def get_values(times: list, distances: list) -> dict:
    values = {}
    for time_index, time in enumerate(times):
        logging.debug("time: %s", time)
        logging.debug("time_index: %s", time_index)
        for i in range(times[time_index]):
            distance_calc = i * (times[time_index] - i)
            logging.debug("i * (times[time] - i) = %s", distance_calc)
            if distance_calc > distances[time_index]:
                if times[time_index] not in values:
                    values[times[time_index]] = 0
                values[times[time_index]] += 1
    logging.debug("values: %s", values)
    return values



def part_one(data: list) -> int:
    logging.info("%s()", part_one.__name__)
    times_and_distances = extract_times_and_distances_part_one(data)
    times = times_and_distances['times']
    distances = times_and_distances['distances']
    logging.debug("times: %s", times)
    logging.debug("distances: %s", distances)
    values = get_values(times, distances)
    total = calc_values(values)
    logging.info("total: %s", total)
    logging.debug("end %s\n", part_one.__name__)


def calc_values(values: dict) -> int:
    logging.debug("%s()", calc_values.__name__)
    total = 0
    for _key, value in values.items():
        if total == 0:
            total = value
        else:
            total *= value
    return total


def part_two(data: list) -> None:
    logging.info("%s()", part_two.__name__)
    times_and_distances = extract_times_and_distances_part_two(data)
    times = times_and_distances['times']
    distances = times_and_distances['distances']
    logging.debug("times: %s", times)
    logging.debug("distances: %s", distances)
    values = get_values(times, distances)
    total = calc_values(values)
    logging.info("total: %s", total)
    logging.debug("end %s\n", part_two.__name__)


def main() -> None:
    setup_logger(logging.INFO)
    file_type = FileType.REAL
    data = get_data(file_type)
    part_one(data)
    part_two(data)
    logging.debug("exit()")


if __name__ == "__main__":
    main()
