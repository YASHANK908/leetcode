class Solution(object):
    def maximum69Number (self, num):
        num_str = str(num)
        num_list = list(num_str)
    
        for i in range(len(num_list)):
            if num_list[i] == '6':
                num_list[i] = '9'
                break
        return int("".join(num_list))
         
        