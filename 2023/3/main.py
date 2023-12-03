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
            lines = the_file.read().splitlines()
            return lines
    except FileNotFoundError:
        logging.error("File not found: %s", file_name)
        return []


class SymbolObject:
    def __init__(self, symbol: str, index: int, line_num: int):
        self.symbol = symbol
        self.index = index
        self.line_num = line_num


class NumberObject:
    def __init__(self, number: int, index: int, line_num: int, length: int):
        self.number = number
        self.index = index
        self.line_num = line_num
        self.length = length


def part_one(data: list) -> None:
    logging.info("%s()", part_one.__name__)
    symbol_arr = []
    num_arr = []
    total = 0
    for i, line in enumerate(data):
        logging.debug(line)
        nums = get_numbers(line)
        if nums is not None:
            for num in nums:
                ind = 0
                index = get_number_index(line, num)
                num_arr.append(NumberObject(num, index, i, len(num)))


        is_symbols = find_symbols(line)
        if is_symbols is not None:
            logging.debug("symbols found: %s", is_symbols)
            symbol_index_dict = {}
            for sym in is_symbols:
                if sym in symbol_index_dict:
                    symbol_index_dict[sym] += 1
                else:
                    symbol_index_dict[sym] = 0
                ind = symbol_index_dict[sym]
                logging.debug(symbol_index_dict)
                index = get_symbol_index(line, sym, ind)
                symbol_arr.append(SymbolObject(sym, index, i))
        else:
            logging.debug("no symbols found")
    for num in num_arr:
        touching = is_touching(num, symbol_arr)
        if touching:
            logging.debug("%s is touching (%s)", num.number, touching)
            logging.info("total: %s + %s = %s\n", total, int(num.number), total + int(num.number))
            total += int(num.number)
        else:
            logging.debug("not touching (%s)\n", touching)
    logging.info("total: %s", total)
    logging.debug("end %s\n", part_one.__name__)


def is_touching(number: NumberObject, symbol: list) -> bool:
    logging.debug("%s(number: %s, index: %s, line: %s, length: %s)", 
                  is_touching.__name__, number.number, number.index, number.line_num, number.length)
    for sym in symbol:
        if abs(number.line_num - sym.line_num) <= 1:
            #debug_symbol(sym)
            #logging.debug("lines touching: num.line_num: %s, sym.line_num: %s, abs(): %s", number.line_num, sym.line_num, abs(number.line_num - sym.line_num) <= 1)
            if is_within_range(sym.index, number.index - 1, number.index + number.length):
                logging.debug("symbols touching [symbol: %s, index: %s, line_num: %s]", sym.symbol, sym.index, sym.line_num)
                return True
    return False


def is_within_range(number: int, start: int, end: int) -> bool:
    return start <= number <= end


def get_numbers(line: str) -> list or None:
    numbers = re.findall(r'\d+', line)
    if numbers:
        logging.debug("numbers: %s", numbers)
        return numbers
    return None


def debug_instances(instances: list, type: str) -> None:
    if type == "symbol":
        for instance in instances:
            debug_symbol(instance)
    elif type == "number":
        for instance in instances:
            debug_number(instance)


def debug_symbol(symbol: SymbolObject) -> None:
    logging.debug("symbol: %s, index: %s, line: %s", symbol.symbol, symbol.index, symbol.line_num)
def debug_number(number: NumberObject) -> None:
    logging.debug("number: %s, index: %s, line: %s, length: %s", number.number, number.index, number.line_num, number.length)

def find_symbols(line: str) -> list or None:
    symbols = re.findall(r'[^a-zA-Z0-9.]', line)
    if symbols:
        return symbols
    return None


def get_number_index(line: str, number: str) -> int or None:
    match = re.search(r'\b' + re.escape(number) + r'\b', line)
    if match:
        logging.debug("get_number_index: %s", match.start())
        return match.start()
    return None


def get_symbol_index(line: str, symbol: str, ind: int) -> int or None:
    indices = []
    start = 0
    while True:
        try:
            start = line.index(symbol, start)
            indices.append(start)
            start += 1
        except ValueError:
            break
    logging.debug("indices: %s", indices)
    return indices[ind]


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
