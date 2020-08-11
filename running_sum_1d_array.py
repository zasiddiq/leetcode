# https://leetcode.com/problems/running-sum-of-1d-array/

def running_sum(nums: list) -> list:
    sum_list = []
    sum = 0
    for i in nums:
        sum += i
        sum_list.append(sum)
    return sum_list

if __name__ == '__main__':
    print( running_sum([1,2,3,4]) ) # should be [1,3,6,10]
    print( running_sum([1,1,1,1,1]) ) # should be [1,2,3,4,5]