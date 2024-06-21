class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
#         translate operation to score
#         keep a sum variable adds up each score
        arr = []
        for i in operations:
            if i == 'C':
                arr.remove(arr[-1])
            elif i == 'D':
                arr.append(2 * arr[-1])
            elif i == '+':
                arr.append(arr[-1] + arr[-2])
            else:
                arr.append(int(i))

        return sum(arr)