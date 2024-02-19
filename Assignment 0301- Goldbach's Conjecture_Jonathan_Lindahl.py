# Jonathan Lindahl
# 1/31/2024
# Youtube Link: https://youtu.be/8XX481DIWmA
# I have not given or received any unauthorized assistance on this assignment.

def prime():

    """
    Generates a list of prime numbers up to 100.
    
    This function iterates through numbers from 2 to 100 and checks whether each number is prime. 
    A number is considered prime if it has no divisors other than 1 and itself.
    
    Returns:
        List[int]: A list of prime numbers.
    """

    prime_numbers = [] # Initialize an empty list to store prime numbers.

    # Iterate through numbers from 2 to 100.
    for number in range(2, 101):

        is_prime = True # Assume the number is prime until proven otherwise.

        # Check if the number has any divisor other than 1 and itself.
        for x in range(2, number):
            if number % x == 0:
                is_prime = False # Number is not prime since it has a divisor.
                break

         # If the number is prime, append it to the list.       
        if is_prime:
            prime_numbers.append(number)
    return prime_numbers



    
    
def main():
    """
    Tests Goldbach's Conjecture for all even integers less than 100.

    The function iterates over every even number from 4 to 100 and finds a pair of prime numbers
    from the list of primes (generated by the prime function) that sum up to the even number.
    It prints each pair that meets this criterion.
    """

    prime_numbers = prime() # Get the list of prime numbers.

     # Iterate over even numbers from 4 to 100.
    for even_number in range(4, 101, 2):
    # Check for pairs of primes that sum up to the even number.
        for prime_1 in prime_numbers:
            prime_2 = even_number - prime_1 # Calculate the complementary prime number.
            if prime_2 in prime_numbers:
                print(f"{even_number} = {prime_1} + {prime_2}")
                break # Once a valid pair is found, break to avoid redundant pairs.
                
main()
    
    