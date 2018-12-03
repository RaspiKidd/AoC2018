import numpy as np

def gen_grid():
    grid = np.zeros((1000, 1000))
    vals = []
    with open("input.txt") as f:
        for row in f.readlines():
            id, sep, start, size = row.split()
            x_start, y_start = map(int, start[: -1].split(","))
            x_size, y_size = map(int, size.split("x"))
            grid[x_start:x_start + x_size, y_start:y_start + y_size] += 1
            vals.append((id, (x_start, y_start), (x_size, y_size)))
    return grid, vals

def pt1():
    grid, _= gen_grid()
    return (grid >= 2).sum()

print(pt1())

def pt2():
    grid, vals = gen_grid()
    for id, (x_start, y_start), (x_size, y_size) in vals:
        if (grid[x_start:x_start + x_size, y_start:y_start + y_size] == 1).all():
            return id
    return None

print(pt2())
