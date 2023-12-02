with open("pythonSolutions\day2.txt") as file:
    lines = file.readlines()

num_of_red_cubes = 12
num_of_green_cubes = 13
num_of_blue_cubes = 14

sum_of_ids_of_possible_games = 0
for line in lines:
    is_game_possible = True

    game, cubes_drawn = line.split(":")
    game_ID = int(game.split(" ")[1])
    sets = cubes_drawn.strip().split(";")

    for s in sets:
        cubes = s.split(",")

        for cube in cubes:  
            cube = cube.strip()
            number, color = cube.split(" ")
            number = int(number)

            if (color == "red" and number > num_of_red_cubes
                or color == "green" and number > num_of_green_cubes
                or color == "blue" and number > num_of_blue_cubes):
                is_game_possible = False

    if is_game_possible:
        sum_of_ids_of_possible_games += game_ID
        
print(sum_of_ids_of_possible_games)