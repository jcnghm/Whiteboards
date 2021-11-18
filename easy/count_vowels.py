# Return the number (count) of vowels in the given string.
# We will consider a, e, i, o, u as vowels (but not y).
# The input string will only consist of lower case letters and/or spaces.
# Input = "hello world"
# Output = 3

def count_vowels(string):
    return sum(l in 'aeiou' for l in string)
    # counter = 0
    # for i in string:
    #     if i in "aeiou":
    #         counter += 1
    # return counter

print(count_vowels("hello world"))