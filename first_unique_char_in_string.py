# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/881/
from collections import defaultdict

def first_unique(s: str) -> int:
    hash_table = defaultdict(int)
    for letter in s:
        hash_table[letter] += 1

    potential_letters = list()
    for val in hash_table.items():
        if val[1] == 1:
            potential_letters.append(val[0])
    
    indexes = list()
    for potential in potential_letters:
        indexes.append(s.find(potential))
    
    if len(indexes) == 0:
        return -1
    return min( indexes )


if __name__ == '__main__':
    print( first_unique('leetcode') ) # return 0
    print( first_unique('loveleetcode') ) # return 2
    print( first_unique('') ) # return -1
    print( first_unique('eeeeeaa') ) # return -1