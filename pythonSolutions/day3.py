with open("day3.txt") as file:
    lines = file.readlines()

def get_bread(line_index, start, end):
    if start == 0 and end == len(lines[line_index]) - 1:
        return lines[line_index][start:end + 1]
    elif start == 0 and end < len(lines[line_index]) - 1:
        return lines[line_index][start:end + 2]
    elif start > 0 and end == len(lines[line_index]) - 1:
        return lines[line_index][start - 1:end + 1]
    elif start > 0 and end < len(lines[line_index]) - 1:
        return lines[line_index][start - 1:end + 2]

def get_star_index(line_index, start, line):
    index_of_star_in_chars_below = line.index('*')
    if start != 0:
        return str(line_index) + '_' + str(start - 1 + index_of_star_in_chars_below)
    else:
        return str(line_index) + '_' + str(start + index_of_star_in_chars_below)

import re
def get_only_symbols(line):
    line = re.sub('^[\.0-9]*$', '', line)
    line = line.replace('\n', '')
    return line

numbers_adjacent_to_star = {}

sum_of_part_numbers = 0
for k in range(len(lines)):
    lines[k] = lines[k].strip()
    i = 0
    while i < len(lines[k]):
        if lines[k][i].isdigit():
            is_part_number = False
            is_number_adjacent_to_star = False

            chars_below = ""
            chars_above = ""

            # find the whole number
            number_start = i
            j = i + 1
            while j < len(lines[k]) and lines[k][j].isdigit():
                j += 1
            number_end = j - 1
            number = lines[k][number_start:number_end + 1]

            # check the line of characters above the number
            if k > 0:
                chars_above = get_bread(k - 1, number_start, number_end)
                chars_above = get_only_symbols(chars_above)
                if len(chars_above) > 0:
                    is_part_number = True
                # check if there is * adjacent above
                if '*' in chars_above:
                    is_number_adjacent_to_star = True
                    index_of_star = get_star_index(k - 1, number_start, chars_above)

            # check the line of characters below the number
            if k < len(lines) - 1:
                chars_below = get_bread(k + 1, number_start, number_end)
                chars_below = get_only_symbols(chars_below)
                if len(chars_below) > 0:
                    is_part_number = True
                # check if there is * adjacent below
                if '*' in chars_below:
                    is_number_adjacent_to_star = True
                    index_of_star = get_star_index(k + 1, number_start, chars_below)

            # check the character to the left of the number
            if number_start > 0:
                if lines[k][number_start - 1] != '.':
                    is_part_number = True
                # check if there is * adjacent left
                if lines[k][number_start - 1] == '*':
                    is_number_adjacent_to_star = True
                    index_of_star = str(k) + '_' + str(number_start - 1)

            # check the character to the right of the number
            if number_end < len(lines[k]) - 1:
                if lines[k][number_end + 1] != '.':
                    is_part_number = True
                # check if there is * adjacent right
                if lines[k][number_end + 1] == '*':
                    is_number_adjacent_to_star = True
                    index_of_star = str(k) + '_' + str(number_end + 1)

            if is_part_number:
                sum_of_part_numbers += int(lines[k][number_start:number_end + 1])
            
            if is_number_adjacent_to_star:
                if index_of_star not in numbers_adjacent_to_star:
                    numbers_adjacent_to_star[index_of_star] = []
                numbers_adjacent_to_star[index_of_star].append(int(number))

            i += number_end - number_start

        i += 1
        
print("part 1:", sum_of_part_numbers)
sum_of_gear_ratios = 0
for key in numbers_adjacent_to_star:
    if len(numbers_adjacent_to_star[key]) == 2:
        sum_of_gear_ratios += numbers_adjacent_to_star[key][0] * numbers_adjacent_to_star[key][1]
print("part 2: ", sum_of_gear_ratios)