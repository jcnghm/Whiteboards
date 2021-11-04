# Reverse a String in a list
# Write a function that reverses a string. The input string is given as an array of characters char[].
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
# You may assume all the characters consist of printable ascii characters.
# Example 1:
# Input: ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:
# Input: ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]


def reversedList(lst):
   length = len(lst) // 2
   for x in range(length):
       lst[x], lst[len(lst)-x-1] = lst[len(lst)-x-1], lst[x]
   return lst


print(reversedList(["h","e","l","l","o"]))