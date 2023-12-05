# Which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes
# Add game numbers to get result
# Part 2 - minumum amount of cubes multiplied together for each game and then all added together

red = 12
green  = 13
blue = 14
answer = 0

maxRed = 0
maxGreen = 0
maxBlue = 0
multiplied = 0
answerPart2 = 0

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
                if (maxRed < int(number)):
                    maxRed = int(number)
                if (int(number) > 12):
                    error = True
            elif ("green" in color):
                if (maxGreen < int(number)):
                    maxGreen = int(number)
                if (int(number) > 13):
                    error = True
            elif ("blue" in color):
                if (maxBlue < int(number)):
                    maxBlue = int(number)
                if (int(number) > 14):
                    error = True

    multiplied = maxRed * maxGreen * maxBlue
    maxRed = 0
    maxGreen = 0
    maxBlue = 0
    answerPart2 = answerPart2 + multiplied
    if (not error):
        answer = answer + int(gameNumber)

print(answer)
print(answerPart2)
file.close()