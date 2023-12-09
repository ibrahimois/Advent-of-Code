total = 0
ln = 0
lines = []
with open('input.txt') as input_file:
    for line in input_file:
        lines.append(line)
index = 0
for line in lines:
    matches = 0
    game_id = line.split(":")[0].split(" ")[-1]
    print(f"started game id {game_id}")
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
            lines.append(lines[int(game_id) - 1 + matches])
print(len(lines))
print("finished")