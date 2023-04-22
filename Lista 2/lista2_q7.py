def primes():
    """
    A generator function that yields prime numbers using the Sieve of Eratosthenes algorithm.
    """
    D = {} # dictionary to store the multiples of primes
    q = 2  # first number to check for primality

    while True:
        if q not in D:
            yield q   # q is a prime number
            D[q*q] = [q] # add q^2 to the dictionary
        else:
            # if q is not a prime, add its multiples to the dictionary
            for p in D[q]:
                D.setdefault(p+q,[]).append(p)
            del D[q]

        q += 1 # check the next number for primality
        #print(D)


primes_list = []
for p in primes():
    primes_list.append(p)
    if p > 1000: break
print(primes_list)