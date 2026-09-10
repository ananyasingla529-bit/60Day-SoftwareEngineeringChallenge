numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
position = 0

# Move all non-zero elements to the front
for i in range(len(numbers)):

    if numbers[i] != 0:
        numbers[position] = numbers[i]
        position += 1

# Fill the remaining positions with zeroes
while position < len(numbers):
    numbers[position] = 0
    position += 1

print("Array after moving zeroes:", numbers)
