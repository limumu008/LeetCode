class Solution:
    def longestSubstring(self, s:str, k:int)->int:
        for c in set(s):
            if s.count(c)<k:
                xs = max([self.longestSubstring(t,k) for t in s.split(c)])
                return xs 
        return len(s)

print(Solution().longestSubstring('ababbcbbaa',2))