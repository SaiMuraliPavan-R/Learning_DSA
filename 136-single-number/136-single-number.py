class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        bits = nums[0]
        for x in nums[1:]: bits ^= x;
        return bits;