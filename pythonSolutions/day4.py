with open("day4.txt") as file:
    lines = file.read().splitlines()

matching_numbers_count = []
total_points = 0
for line in lines:
    winning_numbers = line[line.index(":") + 1:].split('|')[0].split(' ')
    your_numbers = line[line.index(":") + 1:].split('|')[1].split(' ')
    winning_numbers = [x for x in winning_numbers if x != '']

    points = sum([1 for number in winning_numbers if number in your_numbers])
    matching_numbers_count.append(points)
    if points > 0:
        total_points += 2**(points - 1)

# part 2
cards = [1 for i in range(len(matching_numbers_count))]
for i in range(len(matching_numbers_count)):
    for j in range(1, matching_numbers_count[i] + 1):
        cards[i + j] += cards[i]

print("Part 1: ", total_points)
print("Part 2:", sum(cards))