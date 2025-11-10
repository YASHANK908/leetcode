class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        def isvowel(c):
            return c in {'a','e','i','o','u'}
        maxvowel=0
        vowel=0
        left=0
        for i in range(len(s)):
            if isvowel(s[i]):
                vowel+=1
            if (i-left+1)==k:
                maxvowel=max(maxvowel,vowel)
                if isvowel(s[left]):
                    vowel-=1
                left+=1
        return maxvowel            

        