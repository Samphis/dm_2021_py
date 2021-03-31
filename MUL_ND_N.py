# multiplier - digit (0-9) for number to be multiplied by
# number - array containing digits of natural number. Number format: [n, B(n-1)...B(0)]
#where n - digit count of the number, B(0)-B(n-1) - digits of the number

def multiply(multiplier, number):
    if multiplier == 0:
        number[:] = [0, 0]
    else:
        overflow = number[len(number) - 1] * multiplier // 10  # variable storing value left to add to the next digit
        number[len(number) - 1] = number[len(number) - 1] * multiplier % 10
        for i in range(len(number) - 2, 0, -1):
            tmp = number[i]
            number[i] = (number[i] * multiplier + overflow) % 10
            overflow = (tmp * multiplier + overflow) // 10
        if overflow > 0:
            number.insert(1, overflow)
            number[0] += 1
