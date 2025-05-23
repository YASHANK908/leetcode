bool isPalindrome(int x) {
    double org=x, rev=0,dig;
    while(x>0){
         dig=x%10;
        rev=rev*10+dig;
        x=x/10;
    }
    if(rev==org){
        return true;
    }
    else{
        return false;
    }
}