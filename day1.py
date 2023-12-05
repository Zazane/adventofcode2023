# On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number
# Have to add them all together to get final answer
# Part 2: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits"
# Written digits can be blended together like eightwo = 82

answer = 0
file = open("day1_input.txt", "r")

written = {
  "one": '1',
  "two": '2',
  "three": '3',
  "four": '4',
  "five": '5',
  "six": '6',
  "seven": '7',
  "eight": '8',
  "nine": '9'
}

for line in file:
    number = 0
    line.lower()

    first = 0
    last = 0
    write = ''
    for ele in line:
        if (ele.isdigit() and first == 0):
            first = ele
        elif (ele.isdigit()):
            last = ele
            write = ''
        else:
            write = write + ele
            if (len(write) > 2):
                for key in written:
                    if (key in write):
                        if (first == 0):
                            first = written[key]
                            write = key[1:]
                        else:
                            last = written[key]
                            write = key[1:]

    if (last == 0):
        last = first
    answer = answer + int(str(first) + str(last))

print(answer)
file.close()