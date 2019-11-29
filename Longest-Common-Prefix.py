class Solution:
    # @param A : list of strings
    # @return a strings
    def longestCommonPrefix(self, A):
        prefix = A[0]
        for string in A:
            prefix = self.getCommon(prefix, string)
            if prefix == "":
                break
        
        return prefix
    
    def getCommon(self, str1, str2):
        prefix = ""
        for i in range(min(len(str1), len(str2))):
            if (str1[i]==str2[i]):
                prefix += str1[i]
            else:
                break
        
        return prefix