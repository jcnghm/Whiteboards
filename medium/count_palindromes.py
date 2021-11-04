# Count Palindromes
# GIven a list of strings, count the number of palindromes that occur inside of the list (a palindrome is a word that is spelled the same backwards and forward).

# Example input: [‘dog’, ‘racecar’, ‘wildebeest’]
# Output: 1
# Explanation: ‘racecar’ is the only palindrome in the list

def palCount(n):
    counter = 0
    for i in n:
        if i == i[::-1]:
            counter += 1
    return counter


print(palCount(['dog', 'racecar', 'wildebeast']))
