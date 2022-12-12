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
    #print(f'{line=}')
    is_action = actions.findall(line)
    #print(f'{is_action=}')
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
        if max_size > 0 and dir_total <= max_size:
            total += dir_total
        elif max_size == 0:
            total += dir_total
        #print(f'{str(dir_total)} = {dir_total <= max_size}')
    return total


def part_one(data: list, count_max: int, print_data: bool) -> dict:
    if print_data:
        print(f"\n{part_one.__name__}()\n---------")
    filesystem = {}
    current_dir = []
    for line in data:
        action = get_action(line)
        if print_data:
            print(f'{action=}')
        if action is not None:
            if action["action"] == 'cd':
                if action["param"] == '/':
                    filesystem[action["param"]] = mkdir(action["param"], None)
                    current_dir = ['/']
                elif action["param"] != '..':
                    full_dir_name = ''.join(current_dir)
                    #parent_dir_name = ''.join(current_dir[:-1])
                    new_dir_name = full_dir_name + action["param"]
                    filesystem[new_dir_name] = mkdir(action["param"], current_dir)
                    current_dir.append(action["param"])
                else:
                    current_dir.pop()
        else:
            is_file_or_dir = get_file_or_dir(line)
            full_dir_name = ''.join(current_dir)
            if is_file_or_dir['type'] == 'dir':
                new_dir_name = full_dir_name + is_file_or_dir['name']
                filesystem[full_dir_name]['children'].append(new_dir_name)
            else:
                the_file = touch(is_file_or_dir['name'], is_file_or_dir['size'])
                filesystem[full_dir_name]['files'].append(the_file)
                filesystem[full_dir_name]['size'] += int(the_file['size'])
    if print_data:
        print(json.dumps(filesystem, sort_keys=True, indent=4) + '\n')
    total = count_total_in_dirs(filesystem, count_max)
    if print_data:
        print(f'\n{total=}')
    return filesystem


def part_two(data: list) -> None:
    print(f"\n{part_two.__name__}()\n---------")
    disk_size = 70000000
    unused_space_needed = 30000000
    max_used_disk_size = disk_size - unused_space_needed
    filesystem = part_one(data, 0, False)
    print(f'{max_used_disk_size=}')
    items = filesystem.items()
    root_size = 0
    for item in items:
        print(item[1]['name'], item[1]['parent'])
        if item[1]['parent'] == '/':
            print("item has parent /")
            root_size += item[1]['size']
    print(f'{root_size=}')
    print('/ size: ', filesystem["/"]["size"])
    for item in items:
        item_size = item[1]['size']
        print(f'{item_size=}')
        print('disk_size - item_size: ', disk_size - item_size)
        print('disk_size - item_size < max_used_disk_size: ', disk_size - item_size < max_used_disk_size)
    #for line in data:
    #    print(line)


def main() -> None:
    data = get_data(False)
    part_one(data, 100000, True)
    part_two(data)
    print("\n------\nexit()")


if __name__ == "__main__":
    main()
