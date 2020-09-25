class Solution:
    def maxProduct(self, nums) -> int:
        
        if len(nums) == 0:
            return 0

        result = nums[0]

        for i in range(len(nums)):
            accu = 1
            for j in range(i, len(nums)):
                accu *= nums[j]
                result = max(result, accu)

        return result

if __name__ == "__main__":

    x = Solution()
    # print( x.maxProduct([0,2]) ) # should be 2
    print( x.maxProduct( [3,-1,4] )) # should be 4
    # print( x.maxProduct ([-2,0,-1]) ) # should be 0