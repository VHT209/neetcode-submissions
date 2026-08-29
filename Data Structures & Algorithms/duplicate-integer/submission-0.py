class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hasDup = len(nums) != len(set(nums))
        return hasDup