with open("day4.txt") as file:
    lines = file.read().splitlines()

matching_numbers_count = []
for line in lines:
    winning_numbers = line[line.index(":") + 1:].split('|')[0].split(' ')
    your_numbers = line[line.index(":") + 1:].split('|')[1].split(' ')
    winning_numbers = [x for x in winning_numbers if x != '']

    count = sum([1 for number in winning_numbers if number in your_numbers])
    matching_numbers_count.append(count)

card_instances = [1 for i in range(len(matching_numbers_count))]

for i in range(len(matching_numbers_count)):
    for j in range(1, matching_numbers_count[i] + 1):
        card_instances[i + j] += card_instances[i]

print(sum(card_instances))