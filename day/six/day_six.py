def exponential_fish(data, days):
    # a fish creates 1 fish every 7 days (including 0)
    # new fish needs 2 days to start the 7 day cycle create a fish
    fish = [0]*9
    for i in sorted(data):
        fish[i] += 1
    while days > 0:
        num_created = fish[0]
        if num_created > 0:
            fish[7] += fish[0]
        fish = fish[1:]
        fish.append(num_created)
        days -= 1

    return sum(fish)


if __name__ == "__main__":
    data = [int(fish) for fish in open("input.txt", "r").read().splitlines()[0].split(",")]
    print(exponential_fish(data, 256))
