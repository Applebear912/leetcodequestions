class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        hash_map = dict()
        for i in s:
            if i in hash_map:
                hash_map[i] += 1
            else: 
                hash_map[i] = 1
        
        for j in t:
            if j not in hash_map:
                return False
            else: 
                hash_map[j] -= 1
            if hash_map[j] == 0:
                del hash_map[j]
        
        for key in hash_map:
            if key:
                return False
        return True

            
        