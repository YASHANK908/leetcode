from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        anagram_map=defaultdict(list)
        for word in strs:
            count=[0]*26
            for c in word:
                count[ord(c)-ord('a')]+=1
            key= '#'.join(str(x) for x in count)
            anagram_map[key].append(word) 
        return list(anagram_map.values())       

        