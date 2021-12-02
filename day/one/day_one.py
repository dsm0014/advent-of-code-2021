def part_one(data):
    len_data = len(data)
    return sum([1 for i in range(len_data) if i+1 < len_data and int(data[i]) < int(data[i+1])]) 


def part_two(data):
    len_data = len(data)
    return part_one([sum([int(data[i]), int(data[i+1]), int(data[i+2])]) for i in range(len_data) if i+2 < len_data])

if __name__ == "__main__":
    with open("input.txt", "r") as file:
        data = file.read().splitlines()
    print(part_one(data))
    print(part_two(data))

