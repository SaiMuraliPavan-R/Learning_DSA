class Solution:
    def countBits(self, n: int) -> List[int]:
        counter = 0;
        output = [];
        for value in range(n+1):
            if value == 0: output.append(value)
            elif value == 1: output.append(value)
            else:
                counter  = 0;
                while (value !=0):
                    value = value & (value -1)
                    counter +=1 ;
                output.append(counter)
        return output        
                