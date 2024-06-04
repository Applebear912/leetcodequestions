class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # sliding windows

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
        