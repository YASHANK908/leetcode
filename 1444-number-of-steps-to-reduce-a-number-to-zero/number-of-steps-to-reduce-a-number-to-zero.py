class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num==0:
            return 0
        return num.bit_count() + num.bit_length()-1
        