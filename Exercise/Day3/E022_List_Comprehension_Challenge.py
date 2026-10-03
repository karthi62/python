square = [i**2 for i in range(1,11)]
print("Squares of numbers from 1 to 10:", square)
words = ["apple", "banana", "orange", "grape", "elephant", "umbrella"]
start_with_vowel = [word for word in words if word[0].lower() in "aeiou"]
print("Words starting with a vowel:", start_with_vowel)
divisible_by_3_and_not_divisble_by_9 = [i for i in range(1,51) if i%3 ==0 and i%9 != 0]
print("Numbers divisible by 3 but not by 9:", divisible_by_3_and_not_divisble_by_9)