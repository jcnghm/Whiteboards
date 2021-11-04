# Lucky Numbers
# Given an array of integers arr, a lucky integer is an integer which has a frequency in the array equal to its value.
# Return a lucky integer in the array. If there are multiple lucky integers return the largest of them. If there is no lucky integer return -1.
# Example 1:
# Input: arr = [2,2,3,4]
# Output: 2
# Explanation: The only lucky number in the array is 2 because frequency[2] == 2.
# Example 2:
# Input: arr = [1,2,2,3,3,3]
# Output: 3
# Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.


def luckyNumber(arr):
   set_arr = set(arr)
   max_unique = 0
   for num in set_arr:
       if num == arr.count(num):
           if max_unique < num:
               max_unique = num
   return max_unique