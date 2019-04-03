class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        
        sortedArray = []
        
        for i in range(len(A)):
            if A[i] % 2 == 0:
                sortedArray.append(A[i])
        
        for i in range(len(A)):
            if A[i] % 2 != 0:
                sortedArray.append(A[i])
            
        return sortedArray
