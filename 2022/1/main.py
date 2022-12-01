def get_data() -> list():
  data_arr = []
  with open('data.txt', 'r') as f:
    data = f.readlines()
    temp = 0
    for line in data:
      if line.strip() == "":
        data_arr.append(temp)
        temp = 0
      else:
        temp = temp + int(line)
    if temp > 0:
      data_arr.append(temp)
  return data_arr

def find_max(list) -> dict():
  max_value = max(list)
  return {
    "max_value": max_value,
    "max_index": list.index(max_value)
  }

def part_one() -> None:
  data = get_data()
  part_one = find_max(data)
  print(f"Part one:\n {part_one['max_value']=}\n {part_one['max_index']=}")

def part_two() -> None:
  data = get_data()
  print("Part two:")
  total = 0
  for i in range(3):
    temp = find_max(data)
    total += temp['max_value']
    print(f"{temp['max_value']=}\n {temp['max_index']=}")
    del data[temp['max_index']]
  print(f"{total=}")

def main() -> None:
  part_one()
  part_two()

if __name__ == "__main__":
  main()