def part_one(data):
    lowest_fuel_cost = sum([d for d in data])  # cost at zero index
    i = 1
    while i < max(data):
        fuel_cost = sum([abs(d-i) for d in data])
        if not lowest_fuel_cost:
            lowest_fuel_cost = fuel_cost
        elif fuel_cost < lowest_fuel_cost:
            lowest_fuel_cost = fuel_cost
        i += 1
    return lowest_fuel_cost


def part_two(data):
    i = min(data)
    j = max(data)
    mid = j/2
    low_fuel = None

    def _low_fuel(index):
        fuel = sum([diff*(diff+1)/2 for d in data if (diff := abs(d - index))])
        if not low_fuel:
            return fuel
        return fuel if fuel < low_fuel else low_fuel

    while i < mid < j:
        low_fuel = _low_fuel(i)
        low_fuel = _low_fuel(j)
        i += 1
        j -= 1
    return low_fuel


if __name__ == "__main__":
    data = [int(i) for i in open("input.txt", "r").read().splitlines()[0].split(",") if i]
    print(part_one(data))
    print(part_two(data))
