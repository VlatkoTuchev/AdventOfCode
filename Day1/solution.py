# f = open(r"C:\Users\vlatk\Desktop\GitHub Repos\Brainster_vsc_repos\AdventOfCode\Day1\input.txt", "r")
# list_ = [x for x in f]
# list_ = [x.replace('\n','') for x in list_]

# all_together_list = []
# for string in list_:
#     list_of_numbers = [x for x in string if x.isdigit()]
#     new_list = []
    
#     if len(list_of_numbers) == 1:
#         list_of_numbers.append(list_of_numbers[0])
#         all_together_list.append(int(''.join(list_of_numbers)))
#     else:
#         new_list.append([list_of_numbers[0], list_of_numbers[-1]])
#         all_together_list.append(int(''.join(new_list[0])))
        
# print(sum(all_together_list))


###### PART 2 ######

# Dict for changing words into numbers
list_digits = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

all_numbers = []

with open(r'C:\Users\vlatk\Desktop\GitHub Repos\Brainster_vsc_repos\AdventOfCode\Day1\input.txt') as file:
    for line in file:
        list_numbers = []
        for index, char in enumerate(line): 
            if char.isdigit():
                list_numbers.append(char)
            else:
                for key, value in list_digits.items():
                    if line[index:].startswith(key):
                        list_numbers.append(value)
    
        first_digit = list_numbers[0]
        last_digit = list_numbers[-1]

        all_numbers.append(int(''.join([first_digit, last_digit])))

print(sum(all_numbers))
