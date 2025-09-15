class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        broken_set = set(brokenLetters)
        words = text.split()
        count = 0
        
        for word in words:
            if all(char not in broken_set for char in word):
                count += 1
        
        return count

        