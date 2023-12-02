with open("pythonSolutions\day2.txt") as file:
    lines = file.readlines()

sum_of_powers = 0

for line in lines:
    num_of_maxred = 0
    num_of_maxblue = 0
    num_of_maxgreen = 0
    
    game, cubes_drawn = line.split(":")
    game_ID = int(game.split(" ")[1])
    sets = cubes_drawn.split(";")

    for s in sets: # one set of a line
        cubes = s.split(",")

        for cube in cubes:  
            cube = cube.strip()
            number, color = cube.split(" ")
            number = int(number)

            if (color == "red" and number > num_of_maxred):
                num_of_maxred = number
            elif (color == "green" and number > num_of_maxgreen):
                num_of_maxgreen = number
            elif (color == "blue" and number > num_of_maxblue):
                num_of_maxblue = number

    power_of_set = num_of_maxblue * num_of_maxgreen * num_of_maxred
    sum_of_powers += power_of_set
        
print(sum_of_powers)