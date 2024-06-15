class Stack(object):
    def __init__(self):
        self.stack = []
        self.count = 0

    def push(self, data):
        if self.count + 1 <= len(self.stack):
            self.stack[self.count] = data
        else:
            self.stack.append(data)
        self.count += 1

    def pop(self):
        self.count -= 1
        return self.stack[self.count]

    def peak(self):
        return self.stack[self.count-1]

    def is_empty(self):
        return self.count == 0

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
        stack = Stack()
        for i in range(len(s)):
            if s[i] in hash_map:
                if not stack.is_empty() and hash_map[s[i]] == stack.peak():
                    stack.pop()
                else:
                    return False
            else:
                stack.push(s[i])
        return True if stack.is_empty() else False

            

