print("Enter 5 numbers:")
numbers = []
for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)
ascending_numbers = sorted(numbers)
decending_numbers = sorted(numbers, reverse=True)
print("Original numbers:", numbers)
print("Ascending order:", ascending_numbers)
print("Descending order:", decending_numbers)