class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        def isvowel(c):
            if c=='a' or c=='e' or c=='i' or c=='o' or c=='u':
                return True
            else:
                return False
        left=0
        count=0
        maxcount=0
        for right in range(len(s)):
            if isvowel(s[right]):
                count+=1
            if right-left+1==k:
                maxcount=max(maxcount,count)
            if right-left+1>=k:
                if isvowel(s[left]):
                    count-=1
                left+=1
        return maxcount
        