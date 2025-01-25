
'''-------------------------      IMPORTS        -------------------------'''
import re
import math
from collections import Counter
'''-------------------------     END IMPORTS     -------------------------'''

############################################################
def array_diff(a, b):
    return [x for x in a if x not in set(b)]

from collections import Counter
def array_diff(a, b):
    set_b = set(b)
    o = []
    for item in a:
        if item not in set_b:
            o.append(item)
    return o
############################################################

#2
def open_or_senior(data):
    return ["Senior" if age > 54 and handicap > 7 else "Open" for (age,handicap) in data]

#1
def open_or_senior(data):
    output = [0] * len(data)
    for i,datum in enumerate(data):
        [age, handicap] = datum
        if age > 54 and handicap > 7:
            output[i] = "Senior"
        else:
            output[i] = "Open"
    return output

############################################################

''' Checking letters in a set '''
#2
def get_count(sentence):
    return sum(1 for c in sentence if c in "aeiou")

#1
def get_count(sentence):
    letter_set = set("aeiou")
    count = 0
    for c in sentence:
        if c in letter_set:
            count += 1
    return count

############################################################

''' Checking if a number is a float or not '''
import math
def is_square(n):    
    if n < 0: return False
    root = math.sqrt(n)
    return root % 1 == 0

############################################################

''' Comparing string lengths '''
#1
def is_isogram(string):
    return len(string) == len(set(string.lower()))

#2
import re
def is_isogram(string):
    if not len(string): return True
    if len(set(string.lower())) != len(string):
        return False
    if re.search(r'\d', string):
        return False

# print(is_isogram("Dermatoglyphics"))
# print(is_isogram("aba"))
# print(is_isogram("mo0se"))
# print(is_isogram("mouse"))


############################################################

''' String selection '''
my_string = "assman"
''' print(my_string[0:4:2]) '''

############################################################

''' Splitting Strings '''
def string_to_array(s):
    return s.split(" ")

############################################################

''' flooring values '''
def litres(time):
    return time // 2
    return math.floor(time * 0.5)

############################################################



#################### REVIEW SHEET ####################
