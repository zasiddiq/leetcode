def maxSubArray(nums):
    if len(nums) == 1:
        return nums[0]
    max_array = []
    running_sum = 0
    for i in nums:
        if i + running_sum < 0:
            running_sum = 0
            max_array.append(i)
        else:
            running_sum += i
            max_array.append(running_sum)
    print(max_array)
    return max(max_array)


if __name__ == '__main__':
    print( maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) )