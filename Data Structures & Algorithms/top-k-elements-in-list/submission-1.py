class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        count = Counter(nums).most_common(k)
        for num, freq in count:
            ans.append(num)
        return ans