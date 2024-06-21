class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        sub_string = ''
        for i in range(1, len(s)):
            if s[i] == s[0]:
                sub_string = s[0:i]
                j = len(sub_string)
                if sub_string == s[i:i + len(sub_string)]:
                    while j <= len(s):
                        if sub_string != s[j:j+len(sub_string)]:
                            break
                        if j+len(sub_string) == len(s):
                            return True
                        j += len(sub_string)

        return False