class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        morseCode = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        morseMap = {}
        morseFinal = []
        
        for i in range(len(morseCode)):
            morseMap[alphabet[i]] = morseCode[i]
            
        for i in range(len(words)):
            code = ""
            for j in range(len(words[i])):
                code+=morseMap[words[i][j]]
            print(code)
            if code in morseFinal:
                continue
            else:
                morseFinal.append(code)
        
        return len(morseFinal)
