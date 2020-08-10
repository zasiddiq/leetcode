# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/674/
from collections import defaultdict

def intersect(nums1, nums2):
    hash_table1 = defaultdict(int)
    hash_table2 = defaultdict(int)
    for letter in nums1:
        hash_table1[letter] += 1
    for letter in nums2:
        hash_table2[letter] += 1
    i_hash_table = defaultdict(int)
    for i in hash_table1:
        if i in hash_table2:
            i_hash_table[i] = min( hash_table1[i], hash_table2[i] )
    i_list = list()
    for letter in i_hash_table:
        while i_hash_table[letter] > 0:
            i_list.append(letter)
            i_hash_table[letter] -= 1
    return i_list
    

if __name__ == '__main__':
    print( intersect( [1,2,2,1], [2,2] ) ) # should be [2,2]
    print( intersect( [4,9,5], [9,4,9,8,4] ) ) # should be [4,9]
    print( intersect( [1,2,2,1], [2] ) ) # should be [2]