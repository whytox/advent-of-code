from copy import deepcopy
with open('input.txt', 'r') as f:
    INPUT = [ [c for c in line.strip('\n')] for line in f.readlines()]

def print_mat(mat):
    for row in mat:
        for c in row:
            print(c, end='')
        print('\n')
#print_mat(INPUT)

def fork_count_2(mat):
    DIRS = [(0, 1), 
            (1, 1),
            (1, 0),
            (-1, 0),
            (1, -1),
            (0, -1),
            (-1, -1),
            (-1, 1)]
    tot_count = 0
    new_mat = deepcopy(mat)
    for r, row in enumerate(mat):
        for i, c in enumerate(row):
            if not c == '@': continue
            cell_adj_count = 0
            for dir in DIRS:
                adj_r = r + dir[1]
                adj_c = i + dir[0]
                if 0 <= adj_r < len(mat) and 0 <= adj_c < len(mat[0]) \
                    and mat[adj_r][adj_c] == '@':
                        cell_adj_count += 1
            if cell_adj_count < 4:
                new_mat[r][i] = '.'
                tot_count += 1
    return tot_count, new_mat

test = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

def remove_recursively(mat):
    total_removed = 0
    removed, new_mat = fork_count_2(mat)
    i = 0 
    print(i, "removed", removed)
    while removed > 0:
        total_removed += removed
        removed, new_mat = fork_count_2(new_mat)
        i += 1
        print(i, "removed", removed)
    return total_removed

test_mat = [ [ c for c in line] for line in test.split('\n')]
print_mat(test_mat)
print(remove_recursively(test_mat))

print(remove_recursively(INPUT))