"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = [2]
    if number_of_primes > 0:
        n = 2
        while len(list) != number_of_primes:
            prime = True
            for number in list:
                if n%number == 0:
                    prime = False
            if prime:
                list.append(n)
            n = n+1
    else:
        raise ValueError("Input must be greater than 0")
    return list