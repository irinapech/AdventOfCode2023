with open("day3.txt") as file:
    lines = file.readlines()

for line in lines:
    line = line.replace('\n', '')

sum_of_part_numbers = 0
for k in range(len(lines)):
    lines[k] = lines[k].strip()
    i = 0
    while i < len(lines[k]):
        if lines[k][i].isdigit():
            is_part_number = False

            chars_below = ""
            chars_above = ""

            start = i
            j = i + 1
            while (j < len(lines[k]) and lines[k][j].isdigit()):
                j += 1
            end = j - 1
            number = lines[k][start:end + 1]

            if k > 0:
                if start == 0 and end == len(lines[k - 1]) - 1:
                    chars_above = lines[k - 1][start:end + 1]
                elif start == 0 and end < len(lines[k - 1]) - 1:
                    chars_above = lines[k - 1][start:end + 2]
                elif start > 0 and end == len(lines[k - 1]) - 1:
                    chars_above = lines[k - 1][start - 1:end + 1]
                elif start > 0 and end < len(lines[k - 1]) - 1:
                    chars_above = lines[k - 1][start - 1:end + 2]
                chars_above = chars_above.replace('.', '')
                chars_above = chars_above.replace('0', '')
                chars_above = chars_above.replace('1', '')
                chars_above = chars_above.replace('2', '')
                chars_above = chars_above.replace('3', '')
                chars_above = chars_above.replace('4', '')
                chars_above = chars_above.replace('5', '')
                chars_above = chars_above.replace('6', '')
                chars_above = chars_above.replace('7', '')
                chars_above = chars_above.replace('8', '')
                chars_above = chars_above.replace('9', '')
                chars_above = chars_above.replace(' ', '')
                chars_above = chars_above.replace('\n', '')
                if len(chars_above) > 0:
                    is_part_number = True

            if k < len(lines) - 1:
                if start == 0 and end == len(lines[k + 1]) - 1:
                    chars_below = lines[k + 1][start:end + 1]
                elif start == 0 and end < len(lines[k + 1]) - 1:
                    chars_below = lines[k + 1][start:end + 2]
                elif start > 0 and end == len(lines[k + 1]) - 1:
                    chars_below = lines[k + 1][start - 1:end + 1]
                elif start > 0 and end < len(lines[k + 1]) - 1:
                    chars_below = lines[k + 1][start - 1:end + 2]
                
                chars_below = chars_below.replace('.', '')
                chars_below = chars_below.replace('0', '')
                chars_below = chars_below.replace('1', '')
                chars_below = chars_below.replace('2', '')
                chars_below = chars_below.replace('3', '')
                chars_below = chars_below.replace('4', '')
                chars_below = chars_below.replace('5', '')
                chars_below = chars_below.replace('6', '')
                chars_below = chars_below.replace('7', '')
                chars_below = chars_below.replace('8', '')
                chars_below = chars_below.replace('9', '')
                chars_below = chars_below.replace(' ', '')
                chars_below = chars_below.replace('\n', '')

                if len(chars_below) > 0:
                    is_part_number = True

            if start > 0:
                if lines[k][start - 1] != '.':
                    is_part_number = True

            if end < len(lines[k]) - 1:
                if lines[k][end + 1] != '.':
                    is_part_number = True

            if is_part_number:
                sum_of_part_numbers += int(lines[k][start:end + 1])
            
            i += end - start

        i += 1
        
print(sum_of_part_numbers)