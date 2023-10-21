/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
//两两交换链表节点
class Solution {
    public ListNode swapPairs(ListNode head) {
        if(head!=null){
            ListNode dummy_head=new ListNode(-1,head);//虚拟头结点
            ListNode cur=dummy_head;
            while(cur.next!=null && cur.next.next!=null){
                ListNode tmp1=cur.next;
                ListNode tmp2=cur.next.next;
                //一轮变换
                cur.next=tmp2; 
                tmp1.next=tmp2.next;
                tmp2.next=tmp1;
                //
                cur=tmp1;  
            }
            return dummy_head.next;
        }
        return head;
        
        
        

    }
}
