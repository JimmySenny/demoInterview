#!/usr/bin/env python3

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None)
class ListNode:
    def __init__(self,x):
        self.val = x;
        self.next = None;

#    def __str__(self,head):
#        while head.next:
#            print(head.val, end='');
#            head = head.next;
    def iter(self):
        head = self;
        while head:
            print(head.val, end=',');
            head = head.next;
        print('');

class Solution:
#    def reverseList(self, head: ListNode) -> ListNode:
    def reverseList(self, head):
        if not head:
            return None;
        prev = head;
        curr = None;

        while prev:
            nextTemp = prev.next;
            prev.next = curr;
            curr = prev;
            prev = nextTemp;
        return curr;            

def main():
    head = ListNode(1);
    n0 = ListNode(3);
    n1 = ListNode(5);
    n2 = ListNode(7);
    n3 = ListNode(11);
    head.next = n0;
    n0.next = n1;
    n1.next = n2;

    s = Solution();
    head.iter();
    print(s.reverseList(head).iter());

if __name__ == '__main__':
    main();
