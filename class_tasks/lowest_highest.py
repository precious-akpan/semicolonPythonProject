array_of_numbers = [10, 12, 5, 23, 9, 0, 100, -7643245]
lowest = array_of_numbers[0]
for number in array_of_numbers:
    if lowest > number:
        lowest = number
print("Lowest is:", lowest)

highest = array_of_numbers[0]

for number in array_of_numbers:
    if highest < number:
        highest = number
print("Highest:", highest)

# array_of_numbers.