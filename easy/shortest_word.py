# Shortest Word
# Given a string of words, return the length of the shortest word(s).
# String will never be empty and you do not need to account for different data types.
# Example Input: words = ["will bitcoin take over the world maybe who knows perhaps"]
# Example Output: 3
# Example Input: words = ["Brady wins again"]
# Example Output: 4

def shortest_word(words):
    words = words.split()
    items = [len(item) for item in words]
    minimum = min(items)
    print(minimum)

shortest_word("Brady wins again")

# # OR One Liner with list comprehension

# def shortest_word(words):
#     return min([len(word) for word in words.split()]) 

# print(shortest_word("Brady wins again"))