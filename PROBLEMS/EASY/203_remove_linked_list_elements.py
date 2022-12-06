'''
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

Example 1:
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]

Example 2:
Input: head = [], val = 1
Output: []

Example 3:
Input: head = [7,7,7,7], val = 7
Output: []

SOLUTION
method1 (recursion)
method2 (2 pointers)
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def method1(head, val):
    if head is None:
        return None
    head.next = method1(head.next, val)
    return head.next if head.val == val else head

def method2(head, val):
    prev_head = ListNode(-1)
    prev_head.next = head

    curr = head
    prev = prev_head
    while curr:
        if curr.val == val:
            prev.next = curr.next
            curr = curr.next
        else:
            prev = curr
            curr = curr.next
    return prev_head.next
