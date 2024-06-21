class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ''
        for i in s:
            if 65 <= ord(i) <= 90:
                lower_ascii = chr(122 - (90 - ord(i)))
                result += lower_ascii
            else:
                result += i
        return result