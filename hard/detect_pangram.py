# A pangram is a sentence that contains every single letter of the alphabet 
# at least once. For example, the sentence "The quick brown fox jumps over 
# the lazy dog" is a pangram, because it uses the letters A-Z at least once 
# (case is irrelevant).

# Given a string, detect whether or not it is a pangram. Return True if it is, 
# False if not. Ignore numbers and punctuation.


def is_pangram(s):
    alph = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
    for i in set(s):
        if i in alph:
            alph.remove(i)
    if len(alph) == 0:
        return True
    return False

    # alph = 'abcdefghijklmnopqrstuvwxyz'
    # list = []
    
    # for i in alph:
    #     list.append(i)

    # for i in s.lower():
    #     if i in list:
    #         list.remove(i)

    # list = set(list)
    # length = len(list)

    # if length > 0:
    #     return False
    # return True

print(is_pangram('abcdefghijklmnopqrstuvwxyz'))