# Sum of a Sequence Recursion

# Your task is to make function, which returns the sum of a sequence of integers.

# The sequence is defined by 3 non-negative values: begin, end, step (inclusive).

# If begin value is greater than the end, function should returns 0 and if the begin number

# equals the end number return the end number

# Examples

# 2,2,2 --> 2
# 2,6,2 --> 12 (2 + 4 + 6)
# 1,5,1 --> 15 (1 + 2 + 3 + 4 + 5)
# 1,5,3  --> 5 (1 + 4)

# Recursion

def sequence_sum(begin_number, end_number, step):

    if begin_number > end_number:
        return 0
    
    if begin_number == end_number:
        return end_number

    return begin_number + sequence_sum(begin_number + step, end_number, step)

print(sequence_sum(1,9,1))

# Incorrect way

def seq_sum(begin_number, end_number, step):
    return sum(range(begin_number, end_number+1, step))

print(seq_sum(1,9,1))