def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def list_primes(list):
    primes=[]
    for number in list:
        if is_prime(number):
            primes.append(number)
    print(primes)
    return primes


list_primes([1, 4, 6, 7, 13, 9, 67])
print("""""")
list_primes(range(0,1000,2))