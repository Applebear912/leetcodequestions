class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        hash_map = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }

        stack = []
        
        for i in range(len(s)):
            if s[i] in hash_map:
                if stack and hash_map[s[i]] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])
    
        return True if not stack else False

            

