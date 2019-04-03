import math

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        
        hammingCounter = 0
        
        xBin = format(x,'b')
        yBin = format(y,'b')
        
        if len(xBin) > len(yBin):
            yBin = "0"*(len(xBin)-len(yBin))+yBin
        else:
            xBin = "0"*(len(yBin)-len(xBin))+xBin
        
        for i in range(len(xBin)):
            if xBin[i] != yBin[i]:
                hammingCounter+=1
            else:
                continue
        
        return hammingCounter
