def is_invalid_id(id):
    id_s = str(id)
    if len(id_s) % 2 == 1: # numero di cifre dispari
        return False
    half = len(id_s) // 2 
    # le due metà sono uguali?
    return id_s[:half] == id_s[half:]

def is_invalid_id_2(id):
    # mappa divisori {2: [2], 3: [3], 4: [2, 4], 5: [5], 6: [2, 3, 6], 7: [7], 8: [2, 4, 8], 9: [9], 10: [2, 5, 10]}
    id_s = str(id)
    digits = len(id_s)
    divisor = 2
    while divisor <= digits:
        if digits % divisor == 0: # se il numero di cifre è un divisibile per divisore
            # divido il numero 'digits' in 'divisor' elementi
            size = digits // divisor # la lunghezza degli split che vado a confrontare
#            splits = []
#            for i in range(digits, step=size): # es: i = {0, 1} if divisor = 2
#                splits.append(digits[i:i+size])
            splits = [id_s[i:i+size] for  i in range(0, digits, size)]
            all_equals = True 
            for s in splits[1:]:
                if splits[0] != s:
                    all_equals = False
                    break
            if all_equals:
                return True
        divisor += 1
    return False

def sum_invalid_ids(input, validity_funciont=is_invalid_id):
    ranges = [r for r in input.split(',')]
    invalids = []
    for r in ranges:
        range_start, range_end = r.split('-')
        range_start = int(range_start)
        range_end = int(range_end)

        current = range_start
        while current <= range_end:
            if validity_funciont(current):
                invalids.append(current)
            current += 1
    return sum(invalids)

with open('input.txt') as f:
    INPUT = f.readline().strip('/n')
TEST_INPUT = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

print("TEST INPUT:", sum_invalid_ids(TEST_INPUT, validity_funciont=is_invalid_id_2))
print("REAL INPUT:", sum_invalid_ids(INPUT, validity_funciont=is_invalid_id_2))
