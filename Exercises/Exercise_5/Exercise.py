# rewrite this solution to scan each number and any possible sequences

from functools import reduce
import numpy as np


def load_grid(filename):
    grid = []
    with open(filename) as f:
        for line in f.readlines():
            grid.append([int(x) for x in line.strip()])

    return grid


def list_to_int(num_list):
    num = reduce(lambda x, y: x + y, map(str, num_list))
    return int(num)


def transpose(grid):
    np_array = np.array(grid)
    transpose_array = np_array.transpose()
    return transpose_array.tolist()


def diag_top_left_bottom_right(grid):
    np_array = np.fliplr(np.transpose(np.array(grid)))
    diag_grid = []
    for i in range(len(grid) - 1, -len(grid), -1):
        diag_grid.append(np_array.diagonal(offset=i))

    return diag_grid


def diag_bottom_left_top_right(grid):
    np_array = np.array(grid)
    diag_grid = []
    for i in range(-len(grid) + 1, len(grid)):
        diag_grid.append(np_array.diagonal(offset=i))
    return diag_grid


def max_num_row(row, num_digits):
    current_max = list_to_int(row[:num_digits])
    row_length = len(row)
    for i in range(1, row_length - num_digits + 1):
        next_num = list_to_int(row[i:i + num_digits])
        if next_num > current_max:
            current_max = next_num
    return current_max


def max_num_in_rows(grid, num_digits):
    return (max([max_num_row(row, num_digits) for row in grid]))


def max_num_adv(grid, num_digits):
    max_of_rows = max_num_in_rows(grid, num_digits)
    # all we need to do is generate the transpose and the list of diagonals
    columns = transpose(grid)
    #print_grid(columns)
    max_of_cols = max_num_in_rows(columns, num_digits)
    #print()
    diag_t_l_b_r = diag_top_left_bottom_right(grid)
    #print_grid(diag_t_l_b_r)
    max_of_t_l_b_r = max_num_in_rows(diag_t_l_b_r, num_digits)
    diag_b_r_t_l = diag_bottom_left_top_right(grid)
    #print_grid(diag_b_r_t_l)
    max_of_b_r_t_l = max_num_in_rows(diag_b_r_t_l, num_digits)

    return max([max_of_rows, max_of_cols, max_of_t_l_b_r, max_of_b_r_t_l])


def print_grid(grid):
    for line in grid:
        for x in line:
            print(f"{x}  ", end="")
        print("\n")


if __name__ == "__main__":
    filename = "grid_5_by_5.txt"
    grid = load_grid(filename)
    print(grid)
    print_grid(grid)  # print the grid
    print(max_num_in_rows(grid, 3))  # prints 912
    print(max_num_adv(grid, 3))  # prints 971
