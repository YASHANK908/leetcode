int numberOfArithmeticSlices(int* nums, int numsSize) {
    if(numsSize<3) return 0;
    int current=0,count=0;
    for(int i=2;i<numsSize;i++){
        if(nums[i]-nums[i-1]==nums[i-1]-nums[i-2]){
            current+=1;
            count+=current;
        }
        else{
            current=0;
        }
    }
    return count;
}