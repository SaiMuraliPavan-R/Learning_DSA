class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        once = twice = 0;
        for value in nums:
            once =   ~(twice) & (once ^ value)
            twice =   ~(once) & (twice ^ value)
        return once;