# Create a function that takes a positive integer and returns the next bigger number that can be formed by rearranging its digits. For example:

# 12 ==> 21
# 513 ==> 531
# 2017 ==> 2071
# nextBigger(num: 12)   // returns 21
# nextBigger(num: 513)  // returns 531
# nextBigger(num: 2017) // returns 2071
# If the digits can't be rearranged to form a bigger number, return -1 (or nil in Swift):

# 9 ==> -1
# 111 ==> -1
# 531 ==> -1
# nextBigger(num: 9)   // returns nil
# nextBigger(num: 111) // returns nil
# nextBigger(num: 531) // returns nil

def next_bigger(n):
    lst = list(str(n))
    one = list()
    two = list()
    for i in range(len(lst)):
        lst[i] = int(lst[i])
    for index in range(1,len(lst)+1):
        try:
            if lst[-index] > lst[-(index+1)]:
                one = lst[:-(index+1)]
                two = lst[-(index+1):]
                one.append(two.pop(two.index(min(i for i in two if i > two[0]))))
                one.extend(sorted(two))
                for i in range(len(one)):
                    one[i] = str(one[i])
                return int(''.join(one))
        except:
            return -1 
print(next_bigger(12))