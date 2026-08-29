class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for s in strs:
            count = tuple(sorted(Counter(s).items()))
            ans[count].append(s)
        return list(ans.values())