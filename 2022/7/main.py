import re
import json
import sys
#import copy



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


def get_file_or_dir(line: str, parent: str) -> dict | None:
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
        print(f'{line_is_dir=}')
        print(f'{parent=}')
        this_dir = line_is_dir[0]
        return mkdir(this_dir, parent)
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
        #print(f'{child=}')
        #print(f'{filesystem[dir_name]=}')
        key_name = dir_name + child
        print(f'{key_name=}')
        print(f'{key_name} children: {filesystem[key_name]["children"]}')
        if len(filesystem[key_name]["children"]) > 0:
            total += get_total_from_dir_recursive(key_name, filesystem)
        else:
            total += get_total(filesystem[key_name]['files'])
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

def get_item_parent_name(items, item):
    parent_name = item[1]["parent"] + item[1]["name"]
    print(f'{item[1]["parent"]=}')

    return parent_name


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
                    filesystem[new_dir_name] = mkdir(action["param"], current_dir[-1])
                    current_dir.append(action["param"])
                else:
                    if print_data:
                        print(f'{current_dir=}')
                    last = current_dir.pop()
                    if print_data:
                        print('pop: ', last)
        else:
            full_dir_name = ''.join(current_dir)
            is_file_or_dir = get_file_or_dir(line, current_dir[-1])
            if is_file_or_dir['type'] == 'dir':
                new_dir_name = full_dir_name + is_file_or_dir['name']
                print(f'{is_file_or_dir["name"]=}')
                print(f'{new_dir_name=}')
                filesystem[full_dir_name]['children'].append(is_file_or_dir["name"])
            else:
                the_file = touch(is_file_or_dir['name'], is_file_or_dir['size'])
                filesystem[full_dir_name]['files'].append(the_file)
                filesystem[full_dir_name]['size'] += int(the_file['size'])
    #if print_data:
        #print(json.dumps(filesystem, sort_keys=True, indent=4) + '\n')
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
    print(json.dumps(filesystem, sort_keys=True, indent=4) + '\n')
    print(f'{max_used_disk_size=}')
    items = filesystem.items()
    root_size = 0
    filesystem_sizes = {}
    for item in items:
        filesystem_sizes[item[0]] = item[1]['size']
        print(f'{item[1]["name"]} parent: {item[1]["parent"]}')
        if item[1]['parent'] is None:
            root_size += item[1]['size']
        elif item[1]['parent']:
            root_size += item[1]['size']
            parent_name = get_item_parent_name(items, item) #item[1]["parent"] + item[1]["name"]
            print(f'{parent_name=}')
            filesystem_sizes[parent_name] += item[1]['size']
    print(f'{root_size=}')
    print(f'{filesystem_sizes=}')
    print('/ size: ', filesystem["/"]["size"])
    can_be_removed = []
    for item in items:
        if item[1]['parent'] is not None:
            print(f'\n{item[0]}')
            print(f'parent: {item[1]["parent"]}')
            item_size = item[1]['size']
            print(f'{item_size=}')
            print('root_size - item_size: ', root_size - item_size)
            print('root_size - item_size < max_used_disk_size: ', root_size - item_size < max_used_disk_size)
            if root_size - item_size < max_used_disk_size:
                can_be_removed.append(item)
    print('\ncan be removed:')
    for line in can_be_removed:
        print(line[0], line[1]['size'])


def main() -> None:
    data = get_data(False)
    part_one(data, 100000, True)
    part_two(data)
    print("\n------\nexit()")


if __name__ == "__main__":
    main()
