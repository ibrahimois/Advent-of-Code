total = 0
with open('input.txt') as input_file:
    for line in input_file:
        colors = {
            "blue": 0,
            "green": 0,
            "red": 0
        }
        game_id = int(line.split(":")[0].split(" ")[1])
        for set in line.split(":")[1:]:
            for scoop in set.split(";"):
                for color_selection in scoop.split(","):
                    color = color_selection.split(" ")[2].strip()
                    occourance = color_selection.split(" ")[1]
                    if int(occourance) >= colors[color]:
                        colors[color] = int(occourance)
                    
        if colors["red"] <= 12 and colors["green"] <= 13 and colors["blue"] <= 14:
            total += game_id
print(total)