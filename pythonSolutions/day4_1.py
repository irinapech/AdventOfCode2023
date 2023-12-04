with open("day4.txt") as file:
    lines = file.read().splitlines()

total_points = 0
for line in lines:
    winning_numbers = line[line.index(":") + 1:].split('|')[0].split(' ')
    your_numbers = line[line.index(":") + 1:].split('|')[1].split(' ')
    winning_numbers = [x for x in winning_numbers if x != '']

    points = sum([1 for number in winning_numbers if number in your_numbers])
    if points > 0:
        total_points += 2**(points - 1)

print(total_points)