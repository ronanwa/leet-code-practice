class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        
        uniqueAddresses = []
        
        for i in range(len(emails)):
            emailOg = emails[i]
            emailFirst = emailOg[0:emailOg.find("@")]
            emailFirst = emailFirst[:emailFirst.find('+')].replace(".","")
            emailRevised = emailFirst+emailOg[emailOg.find("@"):len(emailOg)]
            
            if uniqueAddresses == []:
                uniqueAddresses.append(emailRevised)
            else:
                y = 0
                for i in range(len(uniqueAddresses)):
                    if emailRevised == uniqueAddresses[i]:
                        y = 1
                        break
                if y == 0:
                    uniqueAddresses.append(emailRevised)
        
        return len(uniqueAddresses)
