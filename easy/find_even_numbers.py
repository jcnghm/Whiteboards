# Find Even numbers
# Create a function that, given a list as a parameter, finds the even numbers inside the list. The function should then return a list.
# Example:
# Input: [2, 7, 10, 11, 12]
# Output: [2, 10, 12]

# SOLUTION:

def findEven(lst):
   evens = []
   for num in lst:
       if num % 2 == 0:
           evens.append(num)
   return evens
 
def findEvens(lst):
   return [num for num in lst if num % 2 == 0]
