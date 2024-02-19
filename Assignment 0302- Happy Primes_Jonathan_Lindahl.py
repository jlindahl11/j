# Jonathan Lindahl
# 1/31/2024
# Youtube Link: https://youtu.be/TXtN-RO6bNE
# I have not given or received any unauthorized assistance on this assignment.

def prime(number):
    """
    Check if a number is prime.
    
    Parameters:
    number (int): The number to check.
    
    Returns:
    bool: True if the number is prime, False otherwise.
    """

    if number < 2:
        return False

    for x in range(2, int(int(number**0.5) + 1)): # Only check up to the square root of the number
        if number % x == 0:
            return False 
            

    return True



def is_happy(number):
    """
    Determine if a number is a happy number.
    A happy number is defined by a process of summing the squares of its digits repeatedly 
    until the sum is 1, or it loops endlessly in a cycle that does not include 1.
    
    """

    checked_numbers = set() # Keep track of numbers already checked
    while number != 1 and number not in checked_numbers:
        checked_numbers.add(number)
        number = sum(int(digit)**2 for digit in str(number))  # Sum the squares of the digits
        print(number)
    return number == 1


def get_num():
    """
    Prompt the user to enter a positive integer. Repeat until a valid integer is entered.
    
    Returns:
    int: The positive integer input by the user.
    """
    try:
        chosen_num = int((input("Enter a positive integer please. ")))
        return chosen_num
    except ValueError:
        print("Invalid. Please enter a positive integer.")
        return get_num()
    
    
                 
def main():
    """
    Main function to check if a number is both prime and happy.
    """

    number = get_num()
    happy = is_happy(number)
    prime_numbers = prime(number)
    
    # Output results based on the happiness and primality of the number
    if happy and prime:
        print(f"The number {number} is a happy prime.")
    elif not happy and prime:
        print(f"The number {number} is a sad prime.")
    elif happy and not prime:
        print(f"The number {number} is a happy non-prime.")
    else:
        print(f"The number {number} is a sad non-prime.")
        

    

    
