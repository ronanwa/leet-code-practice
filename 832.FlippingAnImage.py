class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        
        newA = []
        
        for row in A:
            row = row[::-1]
            newRow = []
            for bit in row:
                if bit == 1:
                    newRow.append(0)
                else:
                    bit = 1
                    newRow.append(1)
            newA.append(newRow)
        
        return newA
