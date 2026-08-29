class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        ans = []
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in hash_table:
                ans.extend([hash_table[difference], i])
            else:
                hash_table[nums[i]] = i
        return ans