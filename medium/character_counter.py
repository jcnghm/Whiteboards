# You are going to be given a word. Your job will be to make sure that each character
# in that word has the exact same number of occurrences. You will return true if it is valid, or false if it is not.

# Capitals are considered the same as lowercase letters. Therefore: "A" == "a"

# The input is a string (with no spaces) containing [a-z],[A-Z],[0-9] and common symbols. The length will be 0 < length < 100.

# Examples:
#  input = "abcabcd"
#  output = False
#  input = "AbcCBa"
#  output = True


def validate_word(word):
    w = word.lower()
    lis = []
    for i in w:
        lis.append(i)
    list = []
    for i in lis:
        list.append(w.count(i))
    list = set(list)
    if len(list) == 1:
        return True
    return False

print(validate_word("AbcCBa"))


from collections import Counter
def validate_words(word):
    return len(set(Counter(word.lower()).values())) == 1

print(validate_words("abcabcd"))