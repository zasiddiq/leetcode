# https://leetcode.com/problems/jewels-and-stones/
from collections import defaultdict

def jewels_and_stones(j,s):
    if len(j) == 0 or len(s) == 0:
        return 0

    s_hash_map = defaultdict(int)

    for i in s:
        s_hash_map[i] += 1

    jewel_count = 0
    for stone in s_hash_map:
        if stone in j:
            jewel_count += s_hash_map[stone]

    return jewel_count

if __name__ == '__main__':
    print( jewels_and_stones('aA', 'aAAbbbb' ) ) # should be 3
    print( jewels_and_stones('z', 'ZZ' ) ) # should be 3