class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        len_of_word=0
        i=len(s)-1

        while i>=0 and s[i]==" ":
            i-=1
        while i>=0 and s[i]!=" ":
            len_of_word+=1
            i-=1

            

        return len_of_word