import argparse
import os
import shutil

def main() -> None:
    parser = argparse.ArgumentParser(description='Copy template')
    parser.add_argument('year', type=str, help='Year')
    parser.add_argument('day', type=str, help='Day')
    args = parser.parse_args()

    src_dir = './template/'
    dst_dir = os.path.join(args.year, args.day)

    if os.path.exists(dst_dir):
        raise FileExistsError(f"Destination directory {dst_dir} already exists")

    shutil.copytree(src_dir, dst_dir)

if __name__ == "__main__":
    main()