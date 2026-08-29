class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list) #Handling missing values by default
        for str in strs:
            count = tuple(sorted(Counter(str).items())) #sorted cuz counter show the frequencies of word in the way they're put in
            ans[count].append(str)
        return list(ans.values())