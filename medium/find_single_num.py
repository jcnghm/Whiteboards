# Find Single Number
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# Example 1:
# Input: nums = [2,2,1]
# Output: 1
# Example 2:
# Input: nums = [4,1,2,1,2]
# Output: 4
# Example 3:
# Input: nums = [1]
# Output: 1

def non_empty(arr):
   arr_s = set(arr)
   for x in arr_s:
       if arr.count(x) == 1:
           return x

print(non_empty([4,1,2,1,2]))
