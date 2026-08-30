class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for str in strs:
            count = tuple(sorted(Counter(str).items()))
            ans[count].append(str)
        
        return list(ans.values())