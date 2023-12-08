number = "1234567890"
total = 0
number_spelled = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "zero": "0"
}
with open('input.txt') as input_file:
    for line in input_file:
        first_number = 0
        last_number = 0
        digits = ""
        found_flag = False
        for char in line:
            if char in number:
                first_number = char
                digits = ""
                found_flag = True
                break
            else:
                digits += char
                for key in number_spelled:
                    if key in digits:
                        first_number = number_spelled[key]
                        digits = ""
                        found_flag = True
                        break
                if found_flag:
                    break
        found_flag = False
        for char in reversed(line):
            if char in number:
                last_number = char
                digits = ""
                found_flag = True
                break
            else:
                char += digits
                digits = char
                for key in number_spelled:
                    if key in digits:
                        last_number = number_spelled[key]
                        digits = ""
                        found_flag = True
                        break
                if found_flag:
                    break

        line_number = (first_number + last_number)
        total += int(line_number)
    print("Total is:", total)