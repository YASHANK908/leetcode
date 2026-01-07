class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        freq=[0]*26
        for ch in tiles:
            freq[ord(ch)-ord('A')]+=1
        
        def dfs():
            total=0
            for i in range(26):
                if freq[i]==0:
                    continue
                total+=1
                freq[i]-=1
                total+=dfs()
                freq[i]+=1
            return total
        return dfs()
        