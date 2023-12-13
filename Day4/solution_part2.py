# # There's no such thing as "points". Instead, scratchcards only cause you to win more scratchcards equal to the number of winning numbers you have.

# # Specifically, you win copies of the scratchcards below the winning card equal to the number of matches. So, if card 10 were to have 5 matching numbers, you would win one copy each of cards 11, 12, 13, 14, and 15.

# # Copies of scratchcards are scored like normal scratchcards and have the same card number as the card they copied. So, if you win a copy of card 10 and it has 5 matching numbers, it would then win a copy of the same cards that the original card 10 won: cards 11, 12, 13, 14, and 15. This process repeats until none of the copies cause you to win any more cards. (Cards will never make you copy a card past the end of the table.)

# # This time, the above example goes differently:

# # Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# # Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# # Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# # Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# # Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# # Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
# # Card 1 has four matching numbers, so you win one copy each of the next four cards: cards 2, 3, 4, and 5.
# # Your original card 2 has two matching numbers, so you win one copy each of cards 3 and 4.
# # Your copy of card 2 also wins one copy each of cards 3 and 4.
# # Your four instances of card 3 (one original and three copies) have two matching numbers, so you win four copies each of cards 4 and 5.
# # Your eight instances of card 4 (one original and seven copies) have one matching number, so you win eight copies of card 5.
# # Your fourteen instances of card 5 (one original and thirteen copies) have no matching numbers and win no more cards.
# # Your one instance of card 6 (one original) has no matching numbers and wins no more cards.
# # Once all of the originals and copies have been processed, you end up with 1 instance of card 1, 2 instances of card 2, 4 instances of card 3, 8 instances of card 4, 14 instances of card 5, and 1 instance of card 6. In total, this example pile of scratchcards causes you to ultimately have 30 scratchcards!

# def check_copy_cards(string):

from collections import Counter

def add_card_numbers(line):
    left_numbers = line.split('|')[0].split(':')[1]
    right_numbers = line.split('|')[1]

    counter = 0
    card_numbers = []
    for number in left_numbers.split(' '):

        if number in right_numbers.split(' ') and number.isdigit():
            # winning_numbers number
            card_number = int(line.split(':')[0].split(' ')[-1])
            counter += 1
            all_instances.append(card_number)

            if card_number + counter > len(all_set):
                pass
            else:
                card_number += counter

            card_numbers.append(card_number)
    
    return card_numbers
    
def extend_values_recursively(original_dict, key, visited=None, depth=0):
    if visited is None:
        visited = set()

    if key in visited:
        return
    visited.add(key)

    # print(f'this is the starting {key}')
    # print('\n')

    original_values = list(original_dict[key])  # Copy to prevent modification
    # print(original_values)
    temp_list = original_dict[key]  # Create a temporary list for new values
    # print(temp_list)
    for referenced_key in original_values[:-1]:
        print(referenced_key)
        print(f'This is the key {key}')
        temp_list.extend(original_dict[referenced_key])
        # print(temp_list)
        extend_values_recursively(original_dict, referenced_key, visited, depth + 1)

    # original_dict[key] = list(temp_list)  # Update with unique values


def find_instances():
    global all_instances, i

    while i < len(all_set):
        line = all_set[i].replace('\n', '')

        dict_answer[i+1] = add_card_numbers(line)
        i += 1

        return find_instances()
    
    original_dict = dict_answer.copy()

    # Use the recursive function here
    for key in list(original_dict.keys()):
        extend_values_recursively(original_dict, key)
        # print(original_dict)

    for key in original_dict:
        original_dict[key].append(key)

    counter = Counter()

    # Iterate through each list in the dictionary values and update the counter
    for value_list in original_dict.values():
        counter.update(value_list)

    return original_dict, counter

with open(r"C:\Users\vlatk\Desktop\GitHub Repos\Brainster_vsc_repos\AdventOfCode\Day4\input-2.txt") as file:
    total_winning_numbers = 0
    all_set = [line for line in file]

    file.close() 

all_instances = []
dict_answer = {}
i = 0

dict_answer, counter = find_instances()

print(dict_answer, counter, sum(counter.values()))

# print(all_instances)
