# https://leetcode.com/problems/rotate-array/

def rotate(nums: list, k: int) -> list:
    for i in range(k):
        nums.insert(0,nums[-1])
        nums.pop()
    print(nums)

if __name__ == '__main__':
    print( rotate([1,2,3,4,5,6,7], 3) ) # should be [5,6,7,1,2,3,4]
    print( rotate([-1,-100,3,99], 2) ) # should be [3,99,-1,-100]
    print( rotate([-1,-100,3,99], 1) ) # should be [99,-1,-100,3]
    print( rotate([-1,-100,3,99], 0) ) # should be [-1,-100,3,99]
    print( rotate([], 0) ) # should be []