#!/usr/bin/env python

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
#    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    def mergeTwoLists(self, l1, l2):
        mhead = ListNode(-1);
        prev = mhead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next;
            else:
                prev.next = l2;
                l2 = l2.next;
            prev = prev.next;

        prev.next = l1 if l1 is not None else l2;
        return mhead.next;

def main():
    s = Solution();
    l1 = ListNode(0);
    l2 = ListNode(0);
    n1 = ListNode(1);
    n2 = ListNode(2);
    n3 = ListNode(3);
    n4 = ListNode(4);
    n5 = ListNode(5);
    n6 = ListNode(6);
    n7 = ListNode(7);
    n8 = ListNode(8);
    n9 = ListNode(7);
    l1.next = n1;
    n1.next = n3;
    n3.next = n5;
    n5.next = n7;
    n7.next = n9;

    l2.next = n2;
    n2.next = n4
    n4.next = n6
    n6.next = n8

    m = ListNode(0);
    m = s.mergeTwoLists(l1,l2);
    while m:
        #print(m.val, end=',');
        m = m.next;

if __name__ == '__main__':
    main();
