# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/549/
from collections import defaultdict

def single_number(nums):
    hash_table = defaultdict(int)
    for n in nums:
        hash_table[n] += 1
    for val in hash_table.items():
        if val[1] == 1:
            return val[0]

if __name__ == '__main__':
    print( single_number([2,2,1]) ) # Should return 1
    print( single_number([4,1,2,1,2]) ) # Should return 4