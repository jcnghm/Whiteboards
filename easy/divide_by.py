# Your task is to create the function is_divide_by to check 
# if an integer number is divisible by both integers a and b.

# Examples:
# (-12, 2, -6)  ->  True
# (-12, 2, -5)  ->  False


def is_divide_by(number, a, b):
    if number % a == 0 and number % b == 0:
        return True
    return False


print(is_divide_by(-12, 2, -6))