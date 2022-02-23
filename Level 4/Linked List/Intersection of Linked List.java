/*
Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:


A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3

begin to intersect at node c1.
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
	public ListNode getIntersectionNode(ListNode a, ListNode b) {
	    ArrayList<ListNode> nodes = new ArrayList<>();
	    ListNode currA = a, currB = b;

	    if (currA == null || currB == null){
	        return null;
	    }

	    while(currA != null){
	        nodes.add(currA);
	        currA = currA.next;
	    }
	    while(currB != null){
	        if (isThatNode(nodes, currB)){
	            return currB;
	        }
	        currB = currB.next;
	    }
	    return null;
	}
	public boolean isThatNode(ArrayList<ListNode> a, ListNode node){
	    for(int i = 0; i<a.size(); i++){
	        if(a.get(i) == node){
	            return true;
	        }

	    }
	    return false;
	}
}
