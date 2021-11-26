# 21. Merge Two Sorted Lists
class ListNode(object):
    def __str__(self, val=0, next=None):
        self.val = val
        self.next = next

    """
    Create a new list head node and ans to that list head node
    Loop over two lists in parrel as long as the both nodes are valid
    establish comparison between current values in the list
    """

    def merge_two_list(self, l1=[], l2=[]):
        current = ListNode()
        ans = current
        while l1 and l2:
            if l1.val > l2.val:
                current.next = l2  # smallest node gets appended to the end of rhe list
                l2 = l2.next
            else:
                current.next = l1
                l1 = l1_.next
            current = current.next  # always points to the last node
        while l1:
            current.next = l1
            l1 = l1.next
            current = current.next
        while l1:
            current.next = l2
            l2 = l2.next
            current = current.next

        return ans


# print(merge_two_list())


# 141. Linked List Cycle
class Solution(object):

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def has_circle(self, head=[3, 2, 0, -40], pos=1):
        hare = self.head
        turtle = self.head
        
        while turtle and hare and hare.next:
            turtle = turtle.next
            hare = hare.next.next
            if turtle == hare:
                return True

        return False


# print(Solution().has_circle(head, pos))


# 206. Reverse Linked List
class Solution(object):
    def __init__(self):
        node = None
        while head is not None:
            next = head.next
            head = node

    def reverse_list(self, head):
        pass


# 2. Add Two Numbers
"""
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def add_two_num(self, l1, l2):
        ans = empty_node
        pointer = ans
        carry = sum = 0

        while l1 or l2:
            sum = carry
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next

            carry = int(sum / 10)
            pointer.next = empty_node(sum % 10)
            pointer = pointer.next

        if carry == 1:
            pointer.next = empty_node(carry)


# 19. Remove Nth Node From End of List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        ans = ListNode(0)
        ans.next = head
        first = ans
        second = ans

        for i in range(len(0, n+2)):
            first = first.next

        while first is not None:
            first = first.next
            second = second.next

        second.next = first.next.next

        return ans.next
