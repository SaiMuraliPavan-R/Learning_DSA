class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        dist = x^y;
        counter = 0;
        while (dist !=0):
            dist = dist & (dist -1)
            counter +=1;
        return counter;
            
        