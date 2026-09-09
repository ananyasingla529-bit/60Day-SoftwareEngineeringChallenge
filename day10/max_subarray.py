# Using Kadane's Algorithm
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
current_sum = numbers[0]
max_sum = numbers[0]
start = 0
best_start = 0
best_end = 0
for i in range(1, len(numbers)):
  current_sum = max(numbers[i], current_sum + numbers[i])

  if current_sum > max_sum:
        max_sum = current_sum
        best_start = start
        best_end = i

# Get the maximum subarray
max_subarray = numbers[best_start:best_end + 1]

print("\nOriginal array:", numbers)
print("Maximum subarray:", max_subarray)
print("Maximum subarray sum:", max_sum)
