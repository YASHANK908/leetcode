int divide(int dividend, int divisor) {
    if(dividend==INT_MIN && divisor==-1) return INT_MAX;
    long long ldevidend=llabs((long long)dividend);
    long long ldevisor=llabs((long long)divisor);
    int sign=((dividend<0)^(divisor<0)?-1:1);
   long long res=0;
    while(ldevidend>=ldevisor){
       long long temp=ldevisor;
       long long multiple=1; 
        while(ldevidend>=(temp<<1)){
            temp<<=1;
            multiple <<=1;
        }
        ldevidend-=temp;
        res+=multiple;
    }
     res = sign * res;

    // Clamp result within 32-bit signed int bounds
    if (res > INT_MAX) return INT_MAX;
    if (res < INT_MIN) return INT_MIN;
    return (int)res;
}