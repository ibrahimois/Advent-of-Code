def check_adjecent(i, j, table):
    found = []
    if i > 0 :
        tl = table[i - 1][j - 1] 
        if tl in numaric: found.append([i - 1, j - 1])
        t = table[i - 1][j]
        if t in numaric: found.append([i - 1, j])
        tr = table[i - 1][j + 1]
        if tr in numaric: found.append([i - 1, j + 1])
    l = table[i][j - 1] 
    if l in numaric: found.append([i, j - 1])
    r = table[i][j + 1]
    if r in numaric: found.append([i, j + 1])

    if i < len(table):
        bl = table[i + 1][j - 1] 
        if bl in numaric: found.append([i + 1, j - 1])
        b = table[i + 1][j]
        if b in numaric: found.append([i + 1, j])
        br = table[i + 1][j + 1]
        if br in numaric: found.append([i + 1, j + 1])
    
    return found
def get_number(fon, table):
    i = fon[0]
    j = fon[1]
    number = table[i][j]
    found = False
    right_found = False
    right = j
    left = j
    while not right_found:
        right += 1
        if right > len(table[i]) - 1: right_found = True
        elif table[i][right] not in numaric: right_found = True
        else: number += table[i][right]
    left_found = False
    while not left_found:
        left -= 1
        if left < 0: left_found = True
        elif table[i][left] not in numaric: left_found = True
        else: 
            temp = table[i][left]
            temp += number
            number = temp
    print(number)
    return number
    
numaric = "0123456789"
#symbol = "!@#$%^&*_+-="
symbol = ",@!#%&=*$-+/*&"
total = 0
table = []
with open('input.txt') as input_file:
    for line in input_file:
        row = []
        for char in line.strip():
            row.append(char.strip())
        table.append(row)
    for row in table:
        print(row)
    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] in symbol:
                found_numbers = check_adjecent(i, j, table)
                print(table[i][j])
                print(found_numbers)
                num_final_form = []
                for fon in found_numbers:
                    num_final_form.append(get_number(fon, table))
                    
                num_final_form = list(set(num_final_form))
                print(num_final_form)
                for n in num_final_form:
                    total += int(n)
print(total)