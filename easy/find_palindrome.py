# Find Palindrome
# Given a string of lowercase letters, write a function to see if the word is a palindrome (the same word spelled forward and backwards).
# Example Input: ‘racecar’
# Example Output: True 

# SOLUTION:

def pal(str):
    if str == str[::-1]:
        return True
    else:
        return False
    # return str == str[::-1] ONE LINER


string = "racecar"
print(pal(string))
