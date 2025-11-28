class Solution:
    def sumAndMultiply(self, n: int) -> int:
        num=str(n)
        digits=""
        Suma=0
        for number in num:
            if number!='0':
                Suma+=int(number)
                digits+=number
        if digits == "":
            return 0
         
        return int(digits)*Suma
        