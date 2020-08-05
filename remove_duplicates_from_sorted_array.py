# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/

def remove_duplicates_from_sorted_array(nums) -> int:
    start = 0
    next_val = 1
    while len(set(nums)) != len(nums):
        while nums[start] == nums[next_val]:
            nums.pop(next_val)
        start += 1
        next_val += 1
    return len(nums)

if __name__ == '__main__':
    print( remove_duplicates_from_sorted_array([0,0,1,1,1,2,2,3,3,4]) )
    print( remove_duplicates_from_sorted_array([1,1,2]) )