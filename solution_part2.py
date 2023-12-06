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

    for match in re.finditer(pattern, string):
        if match.start()-1 <= index < match.end()+1:
            return match.group()

    return None

with open(r'C:\Users\vlatk\Desktop\GitHub Repos\Brainster_vsc_repos\AdventOfCode\Day3\input.txt') as file:
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
            astrix = matches_atrix[y]
            start_index = astrix[1]

            # try:
            above_row_number = find_number_with_index(content[i-1], start_index)
            below_row_number = find_number_with_index(content[i+1], start_index)
            middle_row_number = find_number_with_index(content[i], start_index)

            if above_row_number != None and below_row_number != None:
                print(f"The numbers are {above_row_number} and {below_row_number}")
                gear_ratios.append(int(above_row_number) * int(below_row_number))
            elif middle_row_number != None and below_row_number != None:
                print(f"The numbers are {middle_row_number} and {below_row_number}")
                gear_ratios.append(int(middle_row_number) * int(below_row_number))
            elif above_row_number != None and middle_row_number != None:
                print(f"The numbers are {middle_row_number} and {above_row_number}")
                gear_ratios.append(int(middle_row_number) * int(above_row_number))
            # except:
            #     pass
           
print(sum(gear_ratios))
        # for i in range(len(above_row)):
        #     gear_ratios.append(above_row[i]*below_row[i])



    # try:
    #     print(above_row)
    #     print('------------------')
    #     print(below_row)
    # except:
    #     pass

        # if re.search('*', content[i-1][start_index:end_index]) != None or re.search(char_regex, content[i+1][start_index:end_index]) != None or re.search(char_regex, content[i][start_index:end_index]):
        #     gear_ratios.append(int(number[0]))

# print(sum(gear_ratios))
# 
# 
# for match_in_above_row in matches_numbers_above_row:
#     if start_index in range(match_in_above_row[1]-1, match_in_above_row[2]+1):
#          gear_ratios.append(match_in_above_row[0]*below_row[i])

# above_row = [int(number[0]) for number in matches_numbers_above_row if start_index in range(number[1]-1, number[2]+1)]
# below_row = [int(number[0]) for number in matches_numbers_below_row if start_index in range(number[1]-1, number[2]+1)]