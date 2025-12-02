
with open('input.txt', 'r') as f:
    lines = list(map(lambda l: l.strip(), f.readlines()))

print(lines)

p = 0
curr = 50

for l in lines:
    print(l)
    op = l[0]
    val = int(l[1:]) % 100
    if op == 'R':
        curr = (curr + val) % 100
    elif op == 'L':
        curr = (curr - val) % 100
    if curr == 0:
        p += 1
print("the password is:", p)

