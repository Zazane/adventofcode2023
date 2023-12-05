# Which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes
# Add game numbers to get result
# Part 2 - minumum amount of cubes multiplied together for each game and then all added together

red = 12
green  = 13
blue = 14
answer = 0

max_red = 0
max_green = 0
max_blue = 0
multiplied = 0
answer_part_2 = 0

file = open(r"day2_input.txt", "r")
for line in file:
    games = line.split(": ")
    game = games[0]
    gameNumber = game.split(" ")[1]
    
    hands = games[1].split("; ")
    error = False

    for hand in hands:
        colors = hand.split(", ")
        for color in colors:
            number = "".join([num for num in color if num.isdigit()])
            if ("red" in color):
                if (max_red < int(number)):
                    max_red = int(number)
                if (int(number) > 12):
                    error = True
            elif ("green" in color):
                if (max_green < int(number)):
                    max_green = int(number)
                if (int(number) > 13):
                    error = True
            elif ("blue" in color):
                if (max_blue < int(number)):
                    max_blue = int(number)
                if (int(number) > 14):
                    error = True

    multiplied = max_red * max_green * max_blue
    max_red = 0
    max_green = 0
    max_blue = 0
    answer_part_2 = answer_part_2 + multiplied
    if (not error):
        answer = answer + int(gameNumber)

print(answer)
print(answer_part_2)
file.close()