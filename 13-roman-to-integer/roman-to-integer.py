class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        val = 0
        data = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        i = 0
        while i < len(s):
            if i == len(s) - 1:
                val += data[s[i]]
                return val

            if s[i] == 'I' and s[i + 1] == 'V':
                val += 4
                i += 2
            elif s[i] == 'I' and s[i + 1] == 'X':
                val += 9
                i += 2
            elif s[i] == 'X' and s[i + 1] == 'L':
                val += 40
                i += 2
            elif s[i] == 'X' and s[i + 1] == 'C':
                val += 90
                i += 2
            elif s[i] == 'C' and s[i + 1] == 'D':
                val += 400
                i += 2
            elif s[i] == 'C' and s[i + 1] == 'M':
                val += 900
                i += 2
            else:
                val += data[s[i]]
                i += 1
        return val