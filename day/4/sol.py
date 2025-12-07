with open('input.txt', 'r') as f:
    INPUT = [ [c for c in line.strip('\n')] for line in f.readlines()]

def print_mat(mat):
    for row in mat:
        for c in row:
            print(c, end='')
        print('\n')
print_mat(INPUT)

def fork_count(mat):
    DIRS = [(0, 1), 
            (1, 1),
            (1, 0),
            (-1, 0),
            (1, -1),
            (0, -1),
            (-1, -1),
            (-1, 1)]
    tot_count = 0
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
                tot_count += 1
    return tot_count

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

test_mat = [ [ c for c in line] for line in test.split('\n')]
print_mat(test_mat)
print(fork_count(test_mat))

print(fork_count(INPUT))

