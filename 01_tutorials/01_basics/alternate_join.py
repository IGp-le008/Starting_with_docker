class Solution():
    def join_alternately(self,word1,word2):
        len1=len(word1)
        len2=len(word2)
        maxlen=max(len1,len2)
        minlen=min(len1,len2)
        concatWord=""

        for i in range(0,minlen,1):
            concatWord+=word1[i]+word2[i]

        if minlen!=maxlen:
            if len1==minlen:
                concatWord+=word2[minlen::1]
            else:  
                concatWord+=word1[minlen::1]
        return concatWord


word1=input("Enter the first Word: ")
word2=input("Enter the second Word: ")

sol=Solution()
print(f"Alternately joined word= {sol.join_alternately(word1,word2)}")
