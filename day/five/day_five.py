def _mark_horizontal(ans, x, y, xx, yy):
    if x == xx:
        if y > yy:
            while yy <= y:
                pos = f"{x},{yy}"
                ans[pos] = ans.get(pos, 0) + 1
                yy += 1
        else:
            while y <= yy:
                pos = f"{x},{y}"
                ans[pos] = ans.get(pos, 0) + 1
                y += 1
    return ans


def _mark_vertical(ans, x, y, xx, yy):
    if y == yy:
        if x > xx:
            while xx <= x:
                pos = f"{xx},{y}"
                ans[pos] = ans.get(pos, 0) + 1
                xx += 1
        else:
            while x <= xx:
                pos = f"{x},{y}"
                ans[pos] = ans.get(pos, 0) + 1
                x += 1
    return ans


def _mark_diagonal(ans, x, y, xx, yy):
    if abs(x-xx) == abs(y-yy):
        if x > xx and y > yy:
            while xx <= x and yy <= y:
                pos = f"{x},{y}"
                ans[pos] = ans.get(pos, 0) + 1
                x -= 1
                y -= 1
        elif x > xx and yy > y:
            while xx <= x and y <= yy:
                pos = f"{x},{y}"
                ans[pos] = ans.get(pos, 0) + 1
                x -= 1
                y += 1
        elif xx > x and yy > y:
            while x <= xx and y <= yy:
                pos = f"{x},{y}"
                ans[pos] = ans.get(pos, 0) + 1
                x += 1
                y += 1
        elif xx > x and y > yy:
            while x <= xx and yy <= y:
                pos = f"{x},{y}"
                ans[pos] = ans.get(pos, 0) + 1
                x += 1
                y -= 1
    return ans


def part_one(data):
    ans = {}
    for line in data:
        start, end = line.split(" -> ")
        x,y = [int(i) for i in start.split(",")]
        xx,yy = [int(i) for i in end.split(",")]
        ans = _mark_horizontal(ans, x, y, xx, yy)
        ans = _mark_vertical(ans, x, y, xx, yy)
    return len([val for val in ans.values() if val > 1])


def part_two(data):
    ans = {}
    for line in data:
        start, end = line.split(" -> ")
        x,y = [int(i) for i in start.split(",")]
        xx,yy = [int(i) for i in end.split(",")]
        ans = _mark_horizontal(ans, x, y, xx, yy)
        ans = _mark_vertical(ans, x, y, xx, yy)
        ans = _mark_diagonal(ans, x, y, xx, yy)
    return len([val for val in ans.values() if val > 1])


if __name__ == "__main__":
    data = open("input.txt", "r").read().splitlines()

    print(part_one(data))
    print(part_two(data))
