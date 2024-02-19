# Jonathan Lindahl
# 2/9/2024
# Youtube Link: 
# I have not given or received any unauthorized assistance on this assignment.



import random
import bisect

def find_two_sum(numbers, target_sum):
    """
    Finds two numbers in 'numbers' that sum to 'target_sum'.
    Assumes 'numbers' is sorted.
    """
    for i in range(len(numbers)):
        complement = target_sum - numbers[i]
        if binary_search(numbers, complement, i + 1):
            return True
    return False

def binary_search(numbers, target, start):
    """
    Searches 'numbers' for 'target' starting from 'start' index using binary search.
    """
    end = len(numbers) - 1
    while start <= end:
        mid = (start + end) // 2
        if numbers[mid] == target:
            return True
        elif numbers[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return False

# Main program starts here
length = int(input("Enter the number of integers: "))
sum_to_find = int(input("Enter the sum to find: "))

# Generate list of random integers and sort it
random_numbers = [random.randint(0, 100) for _ in range(length)]
random_numbers.sort()

# Determine if two numbers sum to 'sum_to_find'
if find_two_sum(random_numbers, sum_to_find):
    print(f"Two numbers in the list sum to {sum_to_find}.")
else:
    print(f"No two numbers in the list sum to {sum_to_find}.")
