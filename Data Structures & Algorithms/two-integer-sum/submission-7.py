class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        hash_table = {}

        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in hash_table:
                ans.extend([hash_table.get(difference), i])
            else:
                hash_table[nums[i]] = i
        return ans