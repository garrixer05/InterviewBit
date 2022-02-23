/*
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,

Given 1->4->3->2->5->2 and x = 3,

return 1->2->2->4->3->5.
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
    public ListNode partition(ListNode A, int B) {
        ListNode fake = new ListNode(-1);
        ListNode anchor1 = null, anchor2 = null, n = A, prev = fake;
        boolean flag = true;
        ArrayList<Integer> a = new ArrayList<>();
        fake.next = A;
        while (n != null){
            if (n.val >= B && flag == true){
                anchor1 = prev;
                anchor2 = n;
                flag = false;

            }
            if (n.val < B && flag == false){
                a.add(n.val);
                prev.next = n.next;
                n = n.next;
            }else{
                prev = prev.next;
                n = n.next;
            }

        }
        // System.out.println(a);
        // System.out.println(anchor1.val);
        // System.out.println(anchor2.val);

        for (int i = 0; i<a.size(); ++i){
            ListNode newNode = new ListNode(a.get(i));
            anchor1.next = newNode;
            anchor1 = newNode;
            newNode.next = anchor2;
        }
        return fake.next;
    }
}
