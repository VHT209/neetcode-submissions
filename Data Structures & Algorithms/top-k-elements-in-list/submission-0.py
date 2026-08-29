class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        count = Counter(nums).most_common(k) #Return a tuple(with both number and frequencies)
        for nums, freq in count:
            ans.append(nums)
        return ans