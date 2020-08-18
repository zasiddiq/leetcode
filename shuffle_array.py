def shuffle(nums, n):
    if len(nums) == 0:
        return list()
        
    s_list = []
    p1 = 0
    p2 = n
    while p2 < len(nums):
        s_list.append(nums[p1])
        s_list.append(nums[p2])
        p1 += 1
        p2 += 1
    return s_list

if __name__ == '__main__':
    print( shuffle([2,5,1,3,4,7], 3) )