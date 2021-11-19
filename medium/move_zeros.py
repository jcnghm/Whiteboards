# Move Zeros
# Given an array numbers, write a function to move all 0's to the end of it 
# while maintaining the relative order of the non-zero elements.
# Example:
# Input: [0,1,0,3,2,12]
# Output: [1,3,2,12,0,0]
# Example Input: [0,0,11,2,3,4]
# Example Output: [11,2,3,4,0,0]


def moveZeros(array):
    counter = 0
    while 0 in array:
       array.remove(0)
       counter += 1
    for i in range(counter):
       array.append(0)
      
    return array

print(moveZeros([0,1,0,3,12,0,44,2,77,0,43,13]))


def move_zeros(array):
    for i in array:
        if i == 0:
            array.remove(i)
            array.append(i)
    return array

print(move_zeros([0,1,0,3,12,0,44,2,77,0,43,13]))