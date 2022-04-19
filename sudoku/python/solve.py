import math
import sys


def get_row_col_for_sub_square(grid, sub_square_id, sub_square_index):
    total_numbers = len(grid)
    sub_square_size = int(math.sqrt(total_numbers))

    row = (int(sub_square_id / sub_square_size) * sub_square_size) + int(
        sub_square_index / sub_square_size
    )
    col = int(sub_square_index % sub_square_size) + (
        int(sub_square_id % sub_square_size) * sub_square_size
    )

    return row, col


def calc_sub_squares(grid):
    sub_squares = []
    sub_square_size = int(math.sqrt(len(grid)))

    for i in range(len(grid)):
        sub_square = []
        for n in range(len(grid)):
            row, col = get_row_col_for_sub_square(grid, i, n)
            print(row, col)
            value = grid[row][col]
            if value != "x":
                sub_square.append(value)
        sub_squares.append(sub_square)

    return sub_squares


def read_grid(filename):
    with open(sys.argv[1]) as f:
        lines = f.readlines()
        grid = []
        for line in lines:
            row = line.split()
            grid.append(row)

    return grid


def main():
    grid = read_grid(sys.argv[1])
    print(calc_sub_squares(grid))


if __name__ == "__main__":
    main()
