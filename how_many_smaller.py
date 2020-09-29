class Solution:
    def smallerNumbersThanCurrent(self, nums):

        sorted_nums = sorted(nums)
        
        output = []

        for val in nums:
            output.append( sorted_nums.index(val) )

        return output

        # brute force
        # output = []
        
        # current = 0
        
        # add_val = 0
        
        # while current < len(nums):
        
        #     for index, value in enumerate(nums):
                
        #         if current != index:
                    
        #             if nums[current] > nums[index]:
                        
        #                 add_val += 1
            
        #     output.append(add_val)
        #     add_val = 0
        #     current += 1
        
        # return output

if __name__ == "__main__":

    x = Solution()

    print( x.smallerNumbersThanCurrent( [8,1,2,2,3] ) ) # should be [4,0,1,1,3]