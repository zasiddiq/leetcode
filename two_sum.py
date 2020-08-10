def two_sum(nums: list, target: int) -> list:
    lookup = {}
    for index, item in enumerate(nums):
        if(target - item) in lookup:
            return [lookup[target-item],index]
        else:
            lookup[item] = index


if __name__ == '__main__':
    print ( two_sum([2,7,11,15],9) ) # should be [0,1]
    print ( two_sum([2,7,11,15],26) ) # should be [2,3]
    print ( two_sum([3,2,4],6) ) # should be [1,2]
    print ( two_sum([3,5,3],6) ) # should be [0,1]