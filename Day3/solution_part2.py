# --- Part Two ---
# The engineer finds the missing part and installs it in the engine! As the engine springs to life, you jump in the closest gondola, finally ready to ascend to the water source.

# You don't seem to be going very fast, though. Maybe something is still wrong? Fortunately, the gondola has a phone labeled "help", so you pick it up and the engineer answers.

# Before you can explain the situation, she suggests that you look out the window. There stands the engineer, holding a phone in one hand and waving with the other. You're going so slowly that you haven't even left the station. You exit the gondola.

# The missing part wasn't the only issue - one of the gears in the engine is wrong. A gear is any * symbol that is adjacent to exactly two part numbers. Its gear ratio is the result of multiplying those two numbers together.

# This time, you need to find the gear ratio of every gear and add them all up so that the engineer can figure out which gear needs to be replaced.

# Consider the same engine schematic again:

# 467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..
# In this schematic, there are two gears. The first is in the top left; it has part numbers 467 and 35, so its gear ratio is 16345. The second gear is in the lower right; its gear ratio is 451490. (The * adjacent to 617 is not a gear because it is only adjacent to one part number.) Adding up all of the gear ratios produces 467835.

import re

def find_number_with_index(string, index):
    pattern = r'\d+'
    number_ = 1
    counter = 0

    for match in re.finditer(pattern, string):
        if match.start()-1 <= index < match.end()+1:
            number_ *= int(match.group())
            counter += 1

    if number_:  
        return number_, counter
    else:
        return None

with open(r'/Users/vlatko/Desktop/AdventOfCode/AdventOfCode/Day3/input.txt') as file:
    content = [line for line in file]

    file.close()

# Regular expression to find all numbers in the string
number_regex = r'\d+'

# Regular expression to find all characters except '.'
astrix_regex = r'\*'

gear_ratios = []

for i in range(len(content)):
    if i == 0 or i == len(content) - 1:
        pass
    else:
        matches_atrix = [(match.group(), match.start(), match.end()) for match in re.finditer(astrix_regex, content[i])]

        for y in range(len(matches_atrix)):
            gear_ratio_number = 1
            counter = 0
            astrix = matches_atrix[y]
            start_index = astrix[1]

            gear_ratio_number_1, counter_1 = find_number_with_index(content[i-1], start_index)
            gear_ratio_number_2, counter_2 = find_number_with_index(content[i+1], start_index)
            gear_ratio_number_3, counter_3 = find_number_with_index(content[i], start_index)

            print((counter_1, counter_2, counter_3))

            if counter_1 == 2:
                gear_ratios.append(gear_ratio_number_1)
                print("Counter == 2 for gear_ratio_number 1: ", gear_ratio_number_1)
            elif counter_2 == 2:
                gear_ratios.append(gear_ratio_number_2)
                print("Counter == 2 for gear_ratio_number 2: ", gear_ratio_number_2)
            elif counter_3 == 2:
                gear_ratios.append(gear_ratio_number_3)
                print("Counter == 2 for gear_ratio_number 3: ", gear_ratio_number_3)
            else:
                if counter_1 == 1 and counter_2 == 1: 
                    gear_ratios.append(gear_ratio_number_1 * gear_ratio_number_2)
                    print(f"Counter is 1 for number 1 and number 2: {gear_ratio_number_1} and {gear_ratio_number_2}")
                elif counter_2 == 1 and counter_3 == 1:
                    gear_ratios.append(gear_ratio_number_2 * gear_ratio_number_3)
                    print(f"Counter is 1 for number 2 and number 3: {gear_ratio_number_2} and {gear_ratio_number_3}")
                elif counter_1 == 1 and counter_3 == 1:
                    gear_ratios.append(gear_ratio_number_1 * gear_ratio_number_3)
                    print(f"Counter is 1 for number 1 and number 3: {gear_ratio_number_1} and {gear_ratio_number_3}")

print(sum(gear_ratios))