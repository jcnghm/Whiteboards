# Remove vowels

# Write a function that will remove all vowels from a given string. The function should return a string.
# Example:
# Input: ‘Hello World’
# Output: ‘Hll wrld’


# SOLUTION: 

def rem_vowel(str):
   vowels = ('a', 'e', 'i', 'o', 'u') 
   for x in str.lower():
       if x in vowels:
           str = str.replace(x, "")
   return str
 
def removeVowels(word):
    return ''.join([char for char in word if char.lower() not in 'aeiou'])


string = "Hello World"

print(rem_vowel(string))
print(removeVowels(string))
