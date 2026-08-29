class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub(r"[^a-z0-9]", "", s)
        reverse_s = s[::-1]
        print(s)
        print(reverse_s)
        return s == reverse_s