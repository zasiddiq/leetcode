class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        
        output = []
        
        for index, value in enumerate(A):
            
            if value % 2 == 0:
                output.append(value)
        
        for index, value in enumerate(A):
            
            if value % 2 != 0:
                output.append(value)
        
        return output