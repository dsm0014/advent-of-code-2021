def part_one(data):
    h, depth = 0, 0
    for l in data:
        d, val = l.split(" ")
        val = int(val)
        h, depth = [
            h+val if"for" in d else h,
            depth+val if"dow" in d else depth-val if"for"not in d else depth
        ]
    return h*depth


def part_two(data):
    aim, h, depth = 0, 0, 0
    for l in data:
        d, val = l.split(" ")
        val = int(val)
        aim, h, depth = [
            aim+val if"dow" in d else aim-val if"up" in d else aim,
            h+val if"for" in d else h,
            aim*val+depth if"for" in d else depth
        ]
    return h*depth


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        data = file.read().splitlines()
    print(part_one(data))
    print(part_two(data))
