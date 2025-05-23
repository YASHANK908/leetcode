/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* rotateRight(struct ListNode* head, int k) {
    if(!head||!head->next||k==0) return head;
    int len=1;
   struct ListNode*temp=head;
    while(temp->next){
        temp=temp->next;
          len++;
    }
    temp->next=head;
    k=k%len;
    int steps=len-k;
    struct ListNode*ntail=head;
    for(int i=1;i<steps;i++){
        ntail=ntail->next;
    }
    struct ListNode*newhead=ntail->next;
    ntail->next=NULL;
    return newhead;
}