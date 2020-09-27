class Solution:
    def isPowerOfThree(self, n: int) -> bool:

        if n == 1:
            return True
        
        power = 3
        
        while power <= n:
            
            if power == n:
                return True
            
            power *= 3
            
        return False

if __name__ == "__main__":

    x = Solution()

    print( x.isPowerOfThree(45) ) # should be true