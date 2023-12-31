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

import re
def get_only_symbols(line):
    line = re.sub('^[\.0-9]*$', '', line)
    line = line.replace('\n', '')
    return line

sum_of_part_numbers = 0
for k in range(len(lines)):
    lines[k] = lines[k].strip()
    i = 0
    while i < len(lines[k]):
        if lines[k][i].isdigit():
            is_part_number = False

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

            # check the line of characters below the number
            if k < len(lines) - 1:
                chars_below = get_bread(k + 1, number_start, number_end)
                chars_below = get_only_symbols(chars_below)

                if len(chars_below) > 0:
                    is_part_number = True

            # check the character to the left of the number
            if number_start > 0:
                if lines[k][number_start - 1] != '.':
                    is_part_number = True

            # check the character to the right of the number
            if number_end < len(lines[k]) - 1:
                if lines[k][number_end + 1] != '.':
                    is_part_number = True

            if is_part_number:
                sum_of_part_numbers += int(lines[k][number_start:number_end + 1])
            
            i += number_end - number_start

        i += 1
        
print(sum_of_part_numbers)