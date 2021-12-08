# Find the greatest common divisor of two positive integers. The integers can be large, 
# so you need to find a clever solution.

# The inputs x and y are always greater or equal to 1, so the greatest common divisor will 
# always be an integer that is also greater or equal to 1.


# Brute Force (Don't do this)

def mygcd(x, y):
    divs = []
    if x > y:
        for i in range(1, x+1):
            if x % i == 0 and y % i == 0:
                divs.append(i)
    if y > x:
        for i in range(1, y+1):
            if x % i == 0 and y % i == 0:
                divs.append(i)
    if divs == []:
        return 1
    print(divs)
    return max(divs)

print(mygcd(30, 12))


# Euclidean Algorithm

def mygcd2(a, b):
    if b == 0:
            return a
    print(a%b)
    return mygcd2(b, a % b)



print(mygcd2(30,12))


