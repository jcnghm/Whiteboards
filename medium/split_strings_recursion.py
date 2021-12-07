# Complete the solution so that it splits the string into pairs of two characters.
# If the string is empty return an empty list.
# If the string contains an odd number of characters then it should replace the 
# missing second character of the final pair with an underscore ('_').

# Examples:

# solution('abc') # should return ['ab', 'c_']
# solution('abcdef') # should return ['ab', 'cd', 'ef']

def solution(str):
    if len(str) == 0:
        return []
    elif len(str) == 1:
        return [str + "_"]
    else:
        return [str[:2]] + solution(str[2:])

print(solution('abcdef'))
print(solution('abc'))