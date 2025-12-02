import logging

logging.basicConfig(level=logging.DEBUG)


def solve(operations, start=50):
    p = 0
    curr = start
    rotations = 0
    for op in operations: # 'L20'
        print('curr:', curr)
        direction = op[0]
        N = int(op[1:])
        circles = N // 100
        print('circles:',circles)
        remaining = N % 100
        dist_from_zero = 100 - curr if direction == 'R' else curr
        print(dist_from_zero)
        if direction == 'R':
            curr = (curr + remaining) % 100
        elif direction == 'L':
            curr = (curr - remaining) % 100
        #if curr == 0:
        #    p += 1
        p += circles 
        if remaining >= dist_from_zero and dist_from_zero != 0:
            print(f"remaining >= dist from zero after op {op}")
            p += 1
    return p

def main():
    
    test_inputs = [
        (6, ['L68', 'L30', 'R48', 'L5', 'R60', 'L55', 'L1', 'L99', 'R14', 'L82'])
    ]

    for real_pass, test in test_inputs:
        test_pass = solve(test)
        print(test_pass)
        assert test_pass == real_pass

    INPUT_FILE = "input.txt"
    with open(INPUT_FILE, 'r') as f:
        operations = list(map(lambda l: l.strip(), f.readlines()))
    input_pass = solve(operations)
    logging.info(f"the input password is: {input_pass}")

if __name__ == '__main__':
    main()

