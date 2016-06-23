# Find the first non-repeated (unique) character in a given string.
# efficient use of a hashtable needed.
import collections

def firstUnique(str):
    count=collections.defaultdict(int)
    for letter in str:
        count[letter]+=1
    for letter in str
        if count[letter]==1
        return letter
