class Bingo:
    nums_to_call = []
    boards = []

    def __init__(self, data):
        self.nums_to_call = [int(d) for d in data[0].split(",")]
        self.boards = self._get_boards(data)

    def _get_boards(self, data):
        board, boards = [], []
        for row in data[1:]:
            if not row:
                continue
            clean_row = [int(data) for data in row.strip().split(" ") if data]  # input gets read weird
            if clean_row:
                board.append(clean_row)
            if len(board) == 5:
                boards.append(board)
                board = []
        return boards

    def _check_boards(self, nums_index, board, find_last = False):
        match = False
        misses = []
        nums_called = self.nums_to_call[:nums_index]
        for y, row in enumerate(board):
            for x, val in enumerate(row):
                if val not in nums_called:
                    misses.append(val)
                if y == 0 and {board[y][x], board[y+1][x], board[y+2][x], board[y+3][x], board[y+4][x]}.issubset(nums_called):
                    match = True
                if x == 0 and {board[y][x], board[y][x+1], board[y][x+2], board[y][x+3], board[y][x+4]}.issubset(nums_called):
                    match = True
        if match and find_last:
            self.boards.remove(board)
        return match, misses

    def part_one(self):
        for i in range(len(self.nums_to_call)):
            if i < 4:
                continue
            for board in self.boards:
                is_bingo, misses = self._check_boards(i, board)
                # Return first board with bingo
                if is_bingo:
                    return sum(misses) * int(self.nums_to_call[i-1])

    def part_two(self):
        for i in range(len(self.nums_to_call)):
            if i < 4:
                continue
            all_boards = self.boards
            for board in all_boards:
                is_bingo, misses = self._check_boards(i, board, find_last=True)
                # Return last board to bingo
                if len(self.boards) == 0:
                    self.boards = all_boards
                    return sum(misses) * int(self.nums_to_call[i-1])


if __name__ == "__main__":
    data = open("input.txt", "r").read().splitlines()
    bingo = Bingo(data)
    print(bingo.part_one())
    print(bingo.part_two())
