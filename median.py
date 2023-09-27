"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""


while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)

def median(numbers):
    sorted_lst = sorted(numbers)
    n = len(sorted_lst)

    if n % 2 == 1:
        return f"The median is: {sorted_lst[n//2]}"
    else:
        middle_one = sorted_lst[n // 2 - 1]
        middle_two = sorted_lst[n // 2]
        find_median = (middle_one + middle_two) / 2
        return f"{find_median}"
    
print(median(numbers))
