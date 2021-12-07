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


def palCount1(n):
   sorted_n = n.sort(key = len, reverse = True)
   for i in range(len(n)):
       if n[i] == n[i][::-1]:
           return len(n[i])
   return 0

print(palCount1(['dog', 'racecar', 'wildebeast']))
