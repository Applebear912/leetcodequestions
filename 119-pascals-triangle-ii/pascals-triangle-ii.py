class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = 0
        pre_array = []
        current_array = []

        while row <= rowIndex:
            current_array = []
            row += 1
            for i in range(row):
                if i == 0 or i == row-1:
                    current_array.append(1)
                else:
                    current_array.append(pre_array[i-1] + pre_array[i])
            pre_array = current_array
        return current_array