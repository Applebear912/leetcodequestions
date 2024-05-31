class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        row = 1
        result = []
        result.append([1])

        while row < numRows:
            row += 1
            current_array = [1] * row

            for i in range(row):
                if i == 0 or i == row-1:
                    current_array[i] = 1
                else:
                    current_array[i] = pre_array[i-1] + pre_array[i]
            pre_array = current_array
            result.append(current_array)

        return result
