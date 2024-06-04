class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # clean the string first, remove all non-alphanumeric characters, converting all uppercase letters into lowercases
        # have two pointer one start from 0 index, another start from the end, move towards each other
        # two pointer will stop when they meet each other.
        # lowercase = s.lower()
        # real_char = ''
        # for i in range(len(lowercase)):
        #     if lowercase[i].isalnum():
        #         real_char += lowercase[i]
        
        # p1 = 0
        # p2 = len(real_char)-1
        # while p1 <= p2:
        #     if real_char[p1] != real_char[p2]:
        #         return False
        #     p1 += 1
        #     p2 -= 1
        # return True
        l, r = 0, len(s)-1
        while l < r:
            while l < r and not self.is_valid(s[l]):
                l += 1
            while l < r and not self.is_valid(s[r]):
                r -= 1
            if l < r and s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
    def is_valid(self, char):
        return char.isdigit() or char.isalpha()