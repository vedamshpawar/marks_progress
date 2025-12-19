def isprime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True
def range_of_primes(num):
    res = []
    for i in range(num):
        if isprime(num):
            res.append(i)
    return res
    
num = int(input('enter a number: '))
print(range_of_primes(num))
