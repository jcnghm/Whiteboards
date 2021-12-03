# Given an integer n return "odd" if the number of its divisors is odd. Otherwise return "even".

# Note: big inputs will be tested.

# Examples:
# All prime numbers have exactly two divisors (hence "even").

# For n = 12 the divisors are [1, 2, 3, 4, 6, 12] – "even".

# For n = 4 the divisors are [1, 2, 4] – "odd".

import math
def oddity(n):
    count = 0  
    for num in range(1, int((math.sqrt(n)) + 2)):
        if (n % num == 0) :
            if( n // num == num) :
                count = count + 1
            else :
                count = count + 2
    if (count % 2 == 0) :
        return 'even'
    else :
        return 'odd'

print(oddity(20))