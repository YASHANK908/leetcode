/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
    int len=0;
 struct ListNode* temp=head;
   while(temp){
    len++;
    temp=temp->next;
   }
   if(n==len){
 struct ListNode* newhead=head->next;
    free(head);
    return newhead;
   }
    temp =head;
   for(int i=1;i<len-n;i++) temp=temp->next;
  struct ListNode* del=temp->next;
   temp->next=del->next;
   free(del);
   return head;
}