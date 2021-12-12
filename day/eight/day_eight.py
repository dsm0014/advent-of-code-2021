
def part_one(data):
    return sum([sum(len(b) in {2, 3, 4, 7} for b in a) for a in data])


def part_two(data):
    key = {
        "abcdefg": "8",
        "abdfg": "5",
        "acdfg": "3",
        "abcdfg": "9",
        "abdefg": "6",
        "abcefg": "0",
    }
    total = 0
    for a in data:
        decode = ""
        print(a)
        for b in a:
            print(b)
            if len_b := len(b):
                if len_b == 2:
                    decode += "1"
                elif len_b == 3:
                    decode += "7"
                elif len_b == 4:
                    decode += str(len_b)
                elif len_b == 7:
                    decode += "8"
                else:
                    decode += key["".join(sorted(b))]
        print(decode)


        total += int(decode)

    return total


if __name__ == "__main__":
    data = [i.split(" | ")[1].split(" ") for i in open("input.txt", "r").read().splitlines()]
    # print(data)
    print(part_one(data))
    # print(part_two(data))
