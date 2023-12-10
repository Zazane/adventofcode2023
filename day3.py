# any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. Periods are not symbols.

def find_number(line, placement):
    number_end = ''
    number_start = ''
    start = 0

    for index, digit in enumerate(line[placement:]):
        if (digit.isdigit()):
            number_end = number_end + str(digit)
        else:
            start = placement + index
            break

    for digit in line[:placement][::-1]:
        if (digit.isdigit()):
            number_start = number_start + str(digit)
        else:
            break

    return [int(number_start[::-1] + number_end), start]

def check_lines(previous_line, current_line, same_line_check = True):
    answer = 0
    last_place = -1

    if (len(previous_line) != 0):
        for index, symbol in enumerate(previous_line):
            if (symbol.isdigit()):
                if (index > last_place and 
                    ((index > 0 and not current_line[index-2].isdigit() and current_line[index] != '.' and current_line[index] !='\n') or
                    (index > 0 and not current_line[index-1].isdigit() and current_line[index-1] != '.' and current_line[index-1] !='\n') or
                    (index < len(current_line) and not current_line[index].isdigit() and current_line[index+1] != '.' and current_line[index+1] !='\n'))):
                    number = find_number(previous_line, index)
                    answer = answer + number[0]
                    last_place = number[1]
                    print(number[0])
                elif (same_line_check and index > 0 and index > last_place and
                      ((not previous_line[index-1].isdigit() and previous_line[index-1] != '.' and previous_line[index-1] !='\n') or
                      (index < len(previous_line) - 2 and not previous_line[index+1].isdigit() and previous_line[index+1] != '.' and previous_line[index-1] !='\n'))):
                    number = find_number(previous_line.rstrip(), index, True)
                    answer = answer + number[0]
                    last_place = number[1]
                    if (number[0] == 520):
                        print("index " + str(index) + " len " + str(len(previous_line)) + " here " + str(previous_line[index+1]) + " last place " + str(last_place))

    return answer

file = open(r"day3_input.txt", "r")
answer = 0

if file:
    current_line = file.readline()

for line in file:
    previous_line = current_line
    current_line = line

    answer = answer + check_lines(previous_line, current_line) + check_lines(current_line, previous_line, False)

print(answer)
file.close()