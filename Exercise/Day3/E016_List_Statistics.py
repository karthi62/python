numbers = [10, 20, 5, 40, 15]
total=0
largest=numbers[0]
smallest=numbers[0]
for number in numbers:
    total += number
    if number > largest:
        largest =number
    if number < smallest:
        smallest =number
print("Total:", total)
print("Average:", total/len(numbers))
print("Largest:", largest)
print("Smallest:", smallest)