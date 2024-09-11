class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window
        longest = 0
        substring = set()
        l = 0
        for r in range(len(s)):
            while s[r] in substring:
                substring.remove(s[l])
                l += 1
            substring.add(s[r])
            longest = max(longest, len(substring))
        return longest