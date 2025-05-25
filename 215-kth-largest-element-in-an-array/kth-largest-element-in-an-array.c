void swap(int *a,int *b){
 int t = *a;
 *a=*b;
 *b=t;
}
void heapifydown(int heap[],int n,int i){
    int smallest=i;
    int left= 2*i + 1,right= 2*i + 2;
    if(left<n && heap[left]<heap[smallest]) smallest=left;
    if(right<n && heap[right]<heap[smallest]) smallest=right;
    if(smallest!=i){
        swap(&heap[i],&heap[smallest]);
        heapifydown(heap,n,smallest);
    }
}
void heapifyup(int heap[],int i){
while(i!=0 && heap[(i-1)/2]>heap[i]){
    swap(&heap[i],&heap[(i-1)/2]);
    i=(i-1)/2;
}
}
void insertheap(int heap[],int *size,int val){
    heap[*size]=val;
    heapifyup(heap,*size);
    (*size)++;
}
void popheap(int heap[],int *size){
     heap[0]=heap[--(*size)];
    heapifydown(heap,*size,0);
}
int findKthLargest(int* nums, int numsSize, int k) {
    int heap[k],size=0;
    for(int i=0;i<numsSize;i++){
        if(size<k){
            insertheap(heap,&size,nums[i]);
        }
        else if(nums[i]>heap[0]){
            popheap(heap,&size);
            insertheap(heap,&size,nums[i]);
        }
    }
    return heap[0];
}