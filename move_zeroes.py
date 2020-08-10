# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/567/

def move_zeroes(nums: list) -> None:
    pos = 0
    for i in range(len(nums)):
        el = nums[i]
        if el != 0:
            nums[pos], nums[i] = nums[i], nums[pos]
            pos += 1
    # should not return anything
    print(nums)

if __name__ == '__main__':
    print( move_zeroes( [0,1,0,3,12] ) ) # should be [1,3,12,0,0]