def max_joltage(bank):
    N = len(bank)
    i = 0
    j = 1
    for k in range(1, N):
        if bank[k] > bank[i] and k < N - 1:
            i = k
            j = i + 1
        elif bank[k] > bank[j]:
            j = k

    return int(bank[i] + bank[j])

print(max_joltage('3412'))
print(max_joltage('12'))
print(max_joltage('987654321111111'))
print(max_joltage('811111111111119'))
print(max_joltage('71116'))
print(max_joltage('13241'))
print(max_joltage('9891'))
print(max_joltage('234234234234278'))
print(max_joltage('818181911112111'))

total = 0
with open('input.txt') as f:
    #res = sum([max_joltage(l.strip('/n')) for l in f.readlines()])
    res = 0
    for l in f.readlines():
        #print(l)
        
        res += max_joltage(l.strip('\n'))

print(res)
