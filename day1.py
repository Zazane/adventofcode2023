# On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number
# Have to add them all together to get final answer

answer = 0
file = open(r"day1_input.txt", "r")

for line in file:
    print(line)
    number = 0
    numbers = "".join([num for num in line if num.isdigit()]) # Keep digits
    if (len(numbers) > 2): # First and last
        number = numbers[0] + numbers[-1]
    elif (len(numbers) == 1): # If only one then have it twice
        number = numbers[0] + numbers[0]
    elif (len(numbers) == 2): # If two then keep as is
        number = numbers
    if (len(numbers) > 0):
        answer = answer + int(number)
    print(number)

print(answer)
file.close()