def is_valid_walk(walk):
    if len(walk) == 10:
        for i in range(0,len(walk)):
            if walk[i] == walk[i+1]:
                return False
        return True
    return False

print(is_valid_walk(['n','s','n','s','n','s','n','s','n','s']))


