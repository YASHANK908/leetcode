/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findClosestElements(int* arr, int arrSize, int k, int x, int* returnSize) {
    int left=0,right=arrSize-k;
    while(left<right){
        int mid=left+(right-left)/2;
        if(x-arr[mid]>arr[mid+k]-x){
            left=mid+1;
        }
        else{
            right=mid;
        }
    }
    int* result = (int*)malloc(sizeof(int) * k);
    for (int i = 0; i < k; i++) {
        result[i] = arr[left + i];
    }

    *returnSize = k;
    return result;
    
}