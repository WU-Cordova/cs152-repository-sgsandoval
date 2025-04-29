#4/25/25 in class worksheet

#Part 2:
def mystery(n):
    while n != 0:
        return n * mystery(n -1)
    return 1

print(mystery(4))

#Part 3:

def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return False
    if number % 2 == 0 or number % 3 ==0:
        return False
    for i in range(5, int(number** 0.5) + 1, 6):
        if number % i == 0 or number & (i + 2) == 0:
            return False
    return True

def next_prime_after_double(n):
    return n * 2
    
