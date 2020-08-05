# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/882/
from collections import defaultdict

def isAnagram(s: str, t: str) -> bool:
    hash_table_s = defaultdict(int)
    hash_table_t = defaultdict(int)

    for letter in s:
        hash_table_s[letter] += 1
    for letter in t:
        hash_table_t[letter] += 1
    
    if hash_table_s == hash_table_t:
        return True
    return False
    

if __name__ == '__main__':
    print( isAnagram('anagram', 'nagaram') ) # should be True
    print( isAnagram('rat', 'car') ) # should be False
