with open("day3.txt") as file:
    lines = file.readlines()

for line in lines:
    line = line.replace('\n', '')

numbers_adjacent_to_star = {}

sum_of_part_numbers = 0
for k in range(len(lines)):
    lines[k] = lines[k].strip()
    i = 0
    while i < len(lines[k]):
        if lines[k][i].isdigit():
            is_number_adjacent_to_star = False

            chars_below = ""
            chars_above = ""

            start = i
            j = i + 1
            while (j < len(lines[k]) and lines[k][j].isdigit()):
                j += 1
            end = j - 1
            number = lines[k][start:end + 1]

            # check if there is * adjacent above
            if k > 0:
                if start == 0 and end == len(lines[k - 1]) - 1:
                    chars_above = lines[k - 1][start:end + 1]
                elif start == 0 and end < len(lines[k - 1]) - 1:
                    chars_above = lines[k - 1][start:end + 2]
                elif start > 0 and end == len(lines[k - 1]) - 1:
                    chars_above = lines[k - 1][start - 1:end + 1]
                elif start > 0 and end < len(lines[k - 1]) - 1:
                    chars_above = lines[k - 1][start - 1:end + 2]
                if '*' in chars_above:
                    is_number_adjacent_to_star = True
                    index_of_star_in_chars_above = chars_above.index('*')
                    if start != 0:
                        index_of_star = str(k - 1) + '_' + str(start - 1 + index_of_star_in_chars_above)
                    else:
                        index_of_star = str(k - 1) + '_' + str(start + index_of_star_in_chars_above)

            # check if there is * adjacent below
            if k < len(lines) - 1:
                if start == 0 and end == len(lines[k + 1]) - 1:
                    chars_below = lines[k + 1][start:end + 1]
                elif start == 0 and end < len(lines[k + 1]) - 1:
                    chars_below = lines[k + 1][start:end + 2]
                elif start > 0 and end == len(lines[k + 1]) - 1:
                    chars_below = lines[k + 1][start - 1:end + 1]
                elif start > 0 and end < len(lines[k + 1]) - 1:
                    chars_below = lines[k + 1][start - 1:end + 2]
                
                if '*' in chars_below:
                    if '*' in chars_below:
                        is_number_adjacent_to_star = True
                        index_of_star_in_chars_below = chars_below.index('*')
                        if start != 0:
                            index_of_star = str(k + 1) + '_' + str(start - 1 + index_of_star_in_chars_below)
                        else:
                            index_of_star = str(k + 1) + '_' + str(start + index_of_star_in_chars_below)


            # check if there is * adjacent left
            if start > 0:
                if lines[k][start - 1] == '*':
                    is_number_adjacent_to_star = True
                    index_of_star = str(k) + '_' + str(start - 1)

            # check if there is * adjacent right
            if end < len(lines[k]) - 1:
                if lines[k][end + 1] == '*':
                    is_number_adjacent_to_star = True
                    index_of_star = str(k) + '_' + str(end + 1)

            if is_number_adjacent_to_star:
                if index_of_star not in numbers_adjacent_to_star:
                    numbers_adjacent_to_star[index_of_star] = []
                numbers_adjacent_to_star[index_of_star].append(int(number))
            
            i += end - start

        i += 1

SUM = 0
for key in numbers_adjacent_to_star:
    if len(numbers_adjacent_to_star[key]) == 2:
        SUM += numbers_adjacent_to_star[key][0] * numbers_adjacent_to_star[key][1]
print(SUM)