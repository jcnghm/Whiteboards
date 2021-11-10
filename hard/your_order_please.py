# Your task is to sort a given string. Each word in the string will contain a 
# single number. This number is the position the word should have in the result.

# Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

# If the input string is empty, return an empty string. 
# The words in the input String will only contain valid consecutive numbers.

# Example: 
# input = "is2 Thi1s T4est 3a"
# output = "Thi1s is2 3a T4est"


def order(sentence):
    list = sentence.split(' ')
    nums = []
    dict = {}
    ind = 0
    for i in list:
        for j in i:
            if j in "123456789":
                nums.append(j)
    for i in range(len(list)):
        dict.update({list[i]:nums[ind]})
        ind += 1
    list = sorted(dict.items(), key=lambda kv: kv[1])
    list2 = []
    for i in list:
        list2.append(i[0])
    print(list2)
    return ' '.join(list2)

print(order("is2 Thi1s T4est 3a"))