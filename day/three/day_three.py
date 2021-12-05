from collections import Counter

def part_one(data):
    unpacked = [[], [], [], [], [], [], [], [], [], [], [], []]
    [[unpacked[i].append(b) for i, b in enumerate(binary)] for binary in data]
    gamma, epsilon = "", ""
    for totals in unpacked:
        counter = Counter(totals)
        gamma += max(totals, key=counter.get)
        epsilon += min(totals, key=counter.get)
    return int(gamma, 2) * int(epsilon, 2)


def _decoder(maxormin, data, index, nums=None, last_maxormin=""):
    nums_index = [n[index] for n in nums]
    reverse_nums_index = nums_index
    reverse_nums_index.reverse()
    # python returns the first element encountered in the case of min/max Counter ties
    # according to problem spec, we should return 1
    nums_maxormin = maxormin(nums_index, key=Counter(nums_index).get)
    if maxormin(reverse_nums_index, key=Counter(reverse_nums_index).get) != nums_maxormin:
        last_maxormin += "1"
    else:
        last_maxormin += nums_maxormin
    nums = [d for d in data if d.startswith(last_maxormin)]
    if len(nums) > 1:
        index += 1
        nums = _decoder(maxormin, data, index, nums, last_maxormin)
    elif type(nums) == list:
        return nums[0]
    return nums


def part_two(data):
    mini, maxi = _decoder(min, data, 0, data), _decoder(max, data, 0, data)
    return int(mini, 2) * int(maxi, 2)


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        data = file.read().splitlines()
    print(part_one(data))
    print(part_two(data))
