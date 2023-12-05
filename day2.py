# Which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes
# Add game numbers to get result

red = 12
green  = 13
blue = 14
answer = 0

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
            if (not error):
                if ("red" in color):
                    if (int(number) > 12):
                        error = True
                elif ("green" in color):
                    if (int(number) > 13):
                        error = True
                elif ("blue" in color):
                    if (int(number) > 14):
                        error = True
    if (not error):
        answer = answer + int(gameNumber)

print(answer)
file.close()