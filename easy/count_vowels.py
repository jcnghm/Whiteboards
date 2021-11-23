# Return the number (count) of vowels in the given string.
# We will consider a, e, i, o, u as vowels (but not y).
# The input string will only consist of lower case letters and/or spaces.
# Input = "hello world"
# Output = 3

import time


string = "hello world"
def count_vowels(string):
    # return sum(l in 'aeiou' for l in string)
    counter = 0
    vowels = {"a","e","i","o","u"}
    for i in string:
        if i in vowels:
            counter += 1
    return counter


start = time.time()
print(count_vowels(string))
time.sleep(0.5)
end = time.time()
print("With set")
duration = ((end - start) * 1000.0)
print(f"Function took {duration} ms")




def count_vowels2(string):
    # return sum(l in 'aeiou' for l in string)
    counter = 0
    vowels = ["a","e","i","o","u"]
    for i in string:
        if i in vowels:
            counter += 1
    return counter


start2 = time.time()
print(count_vowels2(string))
time.sleep(0.5)
end2 = time.time()
print("With list")
duration2 = ((end2 - start2) * 1000.0)
print(f"Function took {duration2} ms")

