class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        pointer = 0
        result = ''
        while pointer < len(word1) or pointer < len(word2):
            if pointer == len(word1):
                result += word2[pointer:]
                break
            if pointer == len(word2):
                result += word1[pointer:]
                break
            result += word1[pointer] + word2[pointer]
            pointer += 1
        return result
