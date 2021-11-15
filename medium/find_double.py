# Check if Number and its double exists
# Given an array arr of integers, check if there exists two integers where one is the double of the other.

# Example 1:
# Input: arr = [10,2,5,3]
# Output: true
# Explanation: 10 is the double of 5,that is, 10 = 2 * 5.
# Example 2:
# Input: arr = [7,1,14,11]
# Output: true
# Explanation: 14 is the double of 7,that is, 14 = 2 * 7.
# Example 3:
# Input: arr = [3,1,7,11]
# Output: false
# Explanation: In this case does not exist 


def findDouble(lst):
  for num in lst:
      if num * 2 in lst:
          return True
  return False


  #Another solution
def double(array):
   seen = set()
   for i in array:
       if i * 2 in seen or (i / 2 in seen):
           return True
       else:
           seen.add(i)
   return False
