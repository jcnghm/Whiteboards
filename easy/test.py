def are_coprime(n,m):
    for i in range (2, 100):
        if n % i == 0 and m % i == 0:
            return False
    return True


print(are_coprime(12,39))