'''
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

SOLUTION:
Method1 (using 2 pointers):
    |_ O(min(n,m))
Method2 (using recursion):
    |_ O(n)
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def method1(list1, list2):
    res = curr = ListNode()
    while list1 and list2:
        if list1.val < list2.val:
            curr.next = list1
            list1, curr = list1.next, list1
        else:
            curr.next = list2
            list2, curr = list2.next, list2
    if list1 or list2:
        curr.next = list1 if list1 else list2
    return res.next

def method2(list1,list2):
    if list1 == 'None':
        return list2
    if list2 == 'None':
        return list1
    if list1.val < list2.val:
        list1.next = method2(list1.next, list2)
        return list1
    else:
        list2.next = method2(list1, list2.next)
        return list2