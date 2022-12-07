import re
import json
import sys



sys.setrecursionlimit(1500)


actions = re.compile(r'\$ (\w+)\s*(.*)')
is_file = re.compile(r'(\d+)\s*(.*)')
is_dir = re.compile(r'dir\s*(\w+)')

def get_data(is_test: bool) -> list:
    """Get data from file."""
    file_name = 'data.txt' if is_test is True else 'test_data.txt'
    with open(file_name, 'r', encoding='utf-8') as the_file:
        return the_file.read().splitlines()


def get_action(line: str) -> dict | None:
    is_action = actions.findall(line)
    if len(is_action) > 0:
        action = list(is_action[0])
        param = None
        if action[1] != '':
            param = action[1]
        return {
            "action": action[0],
            "param": param
        }
    return  None


def get_file_or_dir(line: str) -> dict | None:
    line_is_file = is_file.findall(line)
    if line_is_file:
        this_file = line_is_file[0]
        return {
            'type': 'file',
            'size': this_file[0],
            'name': this_file[1]
        }
    line_is_dir = is_dir.findall(line)
    if line_is_dir:
        this_dir = line_is_dir[0]
        return mkdir(this_dir, None)
    return None


def mkdir(name: str, parent: str) -> dict:
    return {
        'type': 'dir',
        'name': name,
        'parent': parent,
        'children': [],
        'files': [],
        'size': 0
    }


def touch(name: str, size: int) -> dict:
    return {
        'name': name,
        'size': size,
    }


def get_total(files: list) -> int:
    total: int = 0
    for file in files:
        #print(f'{file["name"]}\t{file["size"]}')
        total += int(file['size'])
    return total


def get_total_from_dir_recursive(dir_name: str, filesystem: dict) -> int:
    #print(f'dir {dir_name} children: {str(filesystem[dir_name]["children"])}')
    total = get_total(filesystem[dir_name]['files'])
    for child in filesystem[dir_name]['children']:
        if len(filesystem[child]["children"]) > 0:
            total += get_total_from_dir_recursive(child, filesystem)
        else:
            total += get_total(filesystem[child]['files'])
    return total


def get_parent_total_recursive(dir_name: str, filesystem: dict) -> int:
    total = get_total(filesystem[dir_name]['files'])
    direct = filesystem[dir_name]
    #print(f'{direct=}')
    if direct['parent'] is not None:
        parent = direct['parent']
        total += get_parent_total_recursive(parent, filesystem)
    #print(f'get_parent_total_recursive(): {total}')
    return total


def count_total_in_dirs(filesystem: dict, max_size: int) -> int:
    total = 0
    """for direct in filesystem:
        dir_total = get_parent_total_recursive(direct, filesystem)
        if dir_total <= max_size:
            total += dir_total
        print(f'{str(dir_total)} = {dir_total <= max_size}')"""
    for direct in filesystem:
        dir_total = get_total_from_dir_recursive(direct, filesystem)
        if dir_total <= max_size:
            total += dir_total
        #print(f'{str(dir_total)} = {dir_total <= max_size}')
    return total


def part_one(data: list) -> None:
    print(f"\n{part_one.__name__}()\n---------")
    filesystem = {}
    current_dir = []
    #add_files = False
    for line in data:
        #print(f'{current_dir=}')
        action = get_action(line)
        if action is not None:
            #add_files = False
            #print(f'{action=}')
            if action["action"] == 'cd':
                if action["param"] == '/':
                    filesystem[action["param"]] = mkdir(action["param"], None)
                    current_dir = ['/']
                elif action["param"] != '..':
                    if action["param"] in filesystem:
                        print(f'Error? {filesystem[action["param"]]}')
                        # folders can have same name, group by dir path?
                    filesystem[action["param"]] = mkdir(action["param"], current_dir[-1])
                    current_dir.append(action["param"])
                else:
                    current_dir.pop()
            #if action["action"] == 'ls':
            #    add_files = True
        else:
            is_file_or_dir = get_file_or_dir(line)
            if is_file_or_dir['type'] == 'dir':
                filesystem[current_dir[-1]]['children'].append(is_file_or_dir['name'])
            else:
                the_file = touch(is_file_or_dir['name'], is_file_or_dir['size'])
                filesystem[current_dir[-1]]['files'].append(the_file)
                filesystem[current_dir[-1]]['size'] += int(the_file['size'])
            #print(f'adding file/dir: {is_file_or_dir=}')
    #total = get_total_from_dir_recursive('/', filesystem)
    #print(json.dumps(filesystem, sort_keys=True, indent=4) + '\n')
    #test = get_parent_total_recursive('e', filesystem)
    #print(f'{test=}')
    total = count_total_in_dirs(filesystem, 100000)
    print(f'\n{total=}')


def part_two(_data: list) -> None:
    print(f"\n{part_two.__name__}()\n---------")
    #for line in data:
    #    print(line)


def main() -> None:
    data = get_data(True)
    part_one(data)
    part_two(data)
    print("\n------\nexit()")


if __name__ == "__main__":
    main()
