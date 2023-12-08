number = "1234567890"
total = 0
with open('input.txt') as input_file:
    for line in input_file:
        first_number = 0
        last_number = 0
        for char in line:
            if  char in number and first_number == 0: 
                first_number = char
                last_number = char
            elif char in number:
                last_number = char
        line_number = (first_number + last_number)
        total += int(line_number)
    print("Total is:", total)