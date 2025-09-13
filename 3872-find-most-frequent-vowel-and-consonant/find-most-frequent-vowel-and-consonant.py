from collections import Counter

class Solution(object):
    def maxFreqSum(self, s):
        s = s.lower()
        vowels = 'aeiou'
        letters = [char for char in s if char.isalpha()]
        
        if not letters:
            return 0
        
        letter_counts = Counter(letters)
        vowel_counts = {char: count for char, count in letter_counts.items() if char in vowels}
        consonant_counts = {char: count for char, count in letter_counts.items() if char not in vowels}
        
        max_vowel_freq = max(vowel_counts.values()) if vowel_counts else 0
        max_consonant_freq = max(consonant_counts.values()) if consonant_counts else 0
        
        return max_vowel_freq + max_consonant_freq
