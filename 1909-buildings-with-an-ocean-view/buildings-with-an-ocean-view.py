class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        max_height = -1
        res = []
        for i in range(len(heights)-1, -1, -1):
            if heights[i] > max_height:
                res.append(i)
                max_height = heights[i]
        
        res.reverse()
        return res