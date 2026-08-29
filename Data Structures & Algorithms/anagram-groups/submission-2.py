class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for s in strs:
            Count = Counter(s)
            ans[tuple(sorted(Count.items()))].append(s)
        return list(ans.values())
