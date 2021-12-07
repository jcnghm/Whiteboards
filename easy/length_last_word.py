# Length of Last word
# Create a function that given a string as a parameter of upper/lower case letters and empty space characters (“ “), 
# return the length of the last word. Meaning, the word that appears far most to the right if we loop through the words.
# Example Input: "Hello world how are you today"
# Example Output: 5

def lenLast(str):
   list = str.split()
   return len(list[-1])

print(lenLast("Hello world how are you today"))

def lenlast1(str):
    count = 0
    for x in range(len(str)-1,0,-1):
        if str[x] == " ":
            return count
        count += 1

print(lenlast1("Hello world how are you today"))