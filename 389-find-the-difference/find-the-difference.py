class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        hash_table = {}
        for i in t:
            if i in hash_table:
                hash_table[i] += 1
            else:
                hash_table[i] = 1

        for i in s:
            hash_table[i] -= 1
            if hash_table[i] == 0:
                del hash_table[i]

        for key in hash_table:
            return key