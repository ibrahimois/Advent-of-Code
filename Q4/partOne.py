total = 0
ln = 0
with open('input.txt') as input_file:
    for line in input_file:
        print(line)
        matches = 0
        winning_number = line.split(":")[1].strip().split("|")[0].strip().split(" ")
        my_numbers = line.split(":")[1].strip().split("|")[1].strip().split(" ")
        for i in winning_number:
            if len(i) == 0:
                winning_number.remove(i)
        for i in my_numbers:
            if len(i) == 0:
                my_numbers.remove(i)
        for i in winning_number:
            if i in my_numbers:
                matches += 1
        if matches > 0:
            total += pow(2, matches-1) 
print(total)
