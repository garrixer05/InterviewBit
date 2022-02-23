/*
Given a Linked List A consisting of N nodes.

The Linked List is binary i.e data values in the linked list nodes consist of only 0's and 1's.

You need to sort the linked list and return the new linked list.

Problem Constraints
 1 <= N <= 105

 A.val = 0 or A.val = 1



Input Format
First and only argument is the head pointer of the linkedlist A.



Output Format
Return the head pointer of the new sorted linked list.



Example Input
Input 1:

 1 -> 0 -> 0 -> 1
Input 2:

 0 -> 0 -> 1 -> 1 -> 0


Example Output
Output 1:

 0 -> 0 -> 1 -> 1
Output 2:

 0 -> 0 -> 0 -> 1 -> 1


Example Explanation
Explanation 1:

 The sorted linked list looks like:
  0 -> 0 -> 1 -> 1
Explanation 2:

 The sorted linked list looks like:
  0 -> 0 -> 0 -> 1 -> 1
*/

/**
 * Definition for singly-linked list.
 * class ListNode {
 *     public int val;
 *     public ListNode next;
 *     ListNode(int x) { val = x; next = null; }
 * }
 */
public class Solution {
    public ListNode solve(ListNode A) {
        ListNode fake = new ListNode(-1);
        ListNode curr = A, prev = fake;
        fake.next = A;
        int count = 0;
        while(curr.next != null){
            if(curr.val == 1){
                count+=1;
                prev.next = curr.next;
                curr = curr.next;
            }else{
                curr = curr.next;
                prev = prev.next;
            }


        }
        for (int i = 1; i<=count; i++){
            ListNode newNode = new ListNode(1);
            curr.next = newNode;
            curr = curr.next;
        }
        return fake.next;
    }
}
