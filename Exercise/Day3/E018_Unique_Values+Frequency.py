numbers = [2, 5, 2, 8, 5, 2, 8, 9]
unique_numbers = []
for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)
high_frequency = 0
high_frequency_number = None
for number in unique_numbers:
    frequency = numbers.count(number)
    print(f"Number: {number}, Frequency: {frequency}")
    if frequency > high_frequency:
        high_frequency = frequency
        high_frequency_number = number
print(f"High frequency number: {high_frequency_number}")