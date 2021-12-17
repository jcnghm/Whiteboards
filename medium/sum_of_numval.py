# Implement a function to calculate the sum of the numerical values in a nested list. 

# For example :
# sum_nested([1, [2, [3, [4]]]]) -> 10
# sum_nested([])  ->  0
# sum_nested([1, [1], [1, [1]], [1, [1], [1, [1]]]])   ->   8

# Recursion

def sum_nested(lst):
    cur_sum = 0
    for elem in lst:
        if type(elem) == type(1):
            cur_sum+=elem
        else:
            cur_sum+=sum_nested(elem)
    return cur_sum

print(sum_nested([1, [1], [1, [1]], [1, [1], [1, [1]]]]))