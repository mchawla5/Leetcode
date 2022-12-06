'''
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false

SOLUTION
    Method1 (Used Stack):
        |_ O(n)
    Method2 (Two Pointers):
        |_ O(n)
    Method3 (recursion):
        |_ O(n)
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def method1(head):
    stack = []
    dummy = head
    while dummy:
        stack.append(dummy.val)
        dummy = dummy.next
    while head:
        if stack.pop() != head.val:
            return False
        else:
            head = head.next
    return True

def method2(head):
    if not head or not head.next:
        return True
    slow = fast = head
    reversed_list = None

    while fast is not None and fast.next is not None:
        tmp = slow
        slow = slow.next
        fast = fast.next.next
        tmp.next = reversed_list
        reversed_list = tmp

    if fast is not None:
        slow = slow.next

    while reversed_list is not None and reversed_list.val == slow.val:
        reversed_list = reversed_list.next
        slow = slow.next

    return reversed_list is None

def method3(head):
    left = ListNode(-1, head)
    return isPal(head, left)

def isPal(head, left):
    if not head:
        return True
    right = isPal(head.next, left)
    left = left.next
    return right and left.val == head.val