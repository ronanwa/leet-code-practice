class Solution(object):
    def isPalindrome(self, s):
        
        # empty string used for building a string with only the allowed characters to be considered a palindrome
        cleanedString = ""
        
        # list of allowable characters (alphanumeric) to be recognized as part of the palindrome
        alphaNum = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0']
        
        # for every character in string s, see if the character is in the list of allowable characters
        for i in range(len(s)):
            if s[i].lower() in alphaNum:
                # if character is an allowable character, concatenate it to cleanedString to build a string that we can compare
                cleanedString+=s[i].lower()
        
        # Takes built string, compares to the reversed version of said string; if equal, they're a palindrome, otherwise, they're not
        if cleanedString == cleanedString[::-1]:
            return True
        else:
            return False
