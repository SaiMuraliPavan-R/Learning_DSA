class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0]* (n+1);
        for value in range(1,n+1):
            output[value] = output[value & (value-1)] + 1
        return output        
                