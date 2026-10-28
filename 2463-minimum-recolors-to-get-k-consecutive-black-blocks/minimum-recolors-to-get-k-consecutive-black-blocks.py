class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        white_colors=0

        for i in range(k):
            if blocks[i]=="W":
                white_colors+=1
        min_color=white_colors
        for i in range(k,len(blocks)):
            if blocks[i-k]=="W":
                white_colors-=1
            if blocks[i]=="W":
                white_colors+=1
            min_color=min(min_color,white_colors)
        
        return min_color 
        