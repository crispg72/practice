import math


def get_row_col_for_sub_square(grid, sub_square_id, sub_square_index):
    total_numbers = len(grid)
    sub_square_size = int(math.sqrt(total_numbers))

    row = (int(sub_square_id / sub_square_size) * sub_square_size)+ int(sub_square_index / sub_square_size)
    col = int(sub_square_index % sub_square_size) + (int(sub_square_id % sub_square_size) * sub_square_size)

    return row, col

def main():
    print("Hi!")

if __name__ == "__main__":
    main()