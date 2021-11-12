# Complete the solution so that it splits the string into pairs of two characters.
#If the string contains an odd number of characters then it should replace the 
# missing second character of the final pair with an underscore ('_').

# Examples:

# solution('abc') # should return ['ab', 'c_']
# solution('abcdef') # should return ['ab', 'cd', 'ef']

def solution(s):
    if len(s) == 0:
        return []
    elif len(s) == 1:
        return [s + "_"]
    else:
        return [s[:2]] + solution(s[2:])

print(solution('abcdef'))
print(solution('abc'))