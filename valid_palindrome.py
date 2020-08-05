# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/883/
from collections import defaultdict
from copy import deepcopy

def valid_palindrome(s: str) -> bool:
    if s == '':
            return True
    s_list = list()
    for l in s:
        if l != ' ' and l.isalnum():
            s_list.append(l.lower())
    original_list = deepcopy(s_list)
    start = 0
    end = len(s_list) - 1
    while start < end:
        s_list[start], s_list[end] = s_list[end], s_list[start]
        start += 1
        end -= 1
    if original_list == s_list:
        return True
    return False

if __name__ == '__main__':
    print( valid_palindrome('') ) # Should be True
    print( valid_palindrome('A man, a plan, a canal: Panama') ) # Should be True
    print( valid_palindrome('race a car') ) # Should be False
    print( valid_palindrome('bba') ) # Should be False