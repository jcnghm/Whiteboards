# Given a lowercase string that has alphabetic characters only and no spaces, return the highest value of consonant substrings. Consonants are any letters of the alphabet except "aeiou".

# We shall assign the following values: a = 1, b = 2, c = 3, .... z = 26.

# For example, for the word "zodiacs", let's cross out the vowels. We get: "z o d ia cs"

def solve(s):

    # Define letters and list for storing indexes
    alp = "abcdefghijklmnopqrstuvwxyz"
    newlist = []

    # Replace vowels with spaces and split the word on spaces
    for i in s:
        if i in "aeiou":
            s = s.replace(i," ")
    split = s.split(' ')

    # Set variable to store sums of conson groups
    sums = []
    for i in split:

        # If conson group length > 1 letter append and sum the indexes, then reset sums to []
        if len(i) > 1:
            for j in i:
                sums.append(alp.index(j)+1)
            newlist.append(sum(sums))
            sums = []
            
        # If conson group is one letter just append the alp index of the letter
        elif len(i) == 1:
            newlist.append(alp.index(i)+1)

    # Return the max sum of conson groups
    return max(newlist)
          


solve("chruschtschov")