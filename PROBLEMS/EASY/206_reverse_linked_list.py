'''
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []

SOLUTION
method1 (used 2 pointers)
method2 (recursion)
'''

def method1(head):
    if head is None:
        return None
    curr = head
    prev = None
    while head.next != None:
        head = head.next
        curr.next = prev
        prev = curr
        curr = head
    head.next = prev
    return head

def method2(head):
    return help(head)

def help(curr, prev= None):
    if curr is None:
        return prev
    new = curr.next
    curr.next = prev
    return help(new, curr)