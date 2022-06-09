class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max_times = len(nums) //2;
        hash_map = {};
        if len(nums) in {0,1}:
            return 1;
        for value in nums:
            if value not in hash_map:
                hash_map[value] = 1;
            else:
                hash_map[value] += 1;
                if hash_map[value] > max_times:
                    return value;
        