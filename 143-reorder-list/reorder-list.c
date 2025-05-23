/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
  struct ListNode*reverse(struct ListNode*head){
   
    struct ListNode*prev=NULL;
    struct ListNode*curr=head;
    while(curr){
        struct ListNode*next=curr->next;
        curr->next=prev;
        prev=curr;
        curr=next;
    }
    return prev;
  }
void reorderList(struct ListNode* head) {
   if(!head||!head->next||!head->next->next) return;
   struct ListNode* slow=head;
   struct ListNode* fast=head;
   while(fast&&fast->next&&fast->next->next){
    slow=slow->next;
    fast=fast->next->next;
   } 
   struct ListNode*second=reverse(slow->next);
   slow->next=NULL;
   struct ListNode*first=head;
   while(second){
    struct ListNode*temp1=first->next;
    struct ListNode*temp2=second->next;
    first->next=second;
    second->next=temp1;
    first=temp1;
    second=temp2;
   }
}