# expect key to return value
def high(x):
    return max(x.split(), key = lambda word: sum(ord(c) - 96 for c in word))