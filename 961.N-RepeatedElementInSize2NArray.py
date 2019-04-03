class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        
        for i in range(n):
            number = A[i]
            count = 0
            for j in range(n):
                if number == A[j]:
                    count+=1
                if count == n/2:
                    return number
