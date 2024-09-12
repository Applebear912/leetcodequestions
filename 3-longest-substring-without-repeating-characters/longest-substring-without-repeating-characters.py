class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # longest range: sliding windows technique
        # hashing for lookups
        # update longest 
        str = set()
        longest_length = 0
        left = 0
        for right in range(len(s)):
            while s[right] in str:
                str.remove(s[left])
                left += 1
            str.add(s[right])
            longest_length = max(longest_length, len(str))
        return longest_length

        # p, 
        # cur_len = 2, longest = 2