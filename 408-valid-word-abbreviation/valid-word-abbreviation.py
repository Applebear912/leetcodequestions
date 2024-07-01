class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = j = 0
        while i < len(abbr) and j < len(word):
            if abbr[i].isdigit():
                if abbr[i] == '0':
                    return False
                skip = 0
                while i < len(abbr) and abbr[i].isdigit():
                    skip = skip * 10 + int(abbr[i])
                    i += 1
                j += skip 
            else:
                if word[j] != abbr[i]:
                    return False
                i += 1
                j += 1
        return j == len(word) and i == len(abbr)
