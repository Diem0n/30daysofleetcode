# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self, left, right):
        dummy = ListNode()
        current = dummy
        
        while left and right:
            if left.val < right.val:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next
            current = current.next
        
        if left:
            current.next = left
        elif right:
            current.next = right
        
        while current.next:
            current = current.next
        
        return dummy.next

    def split(self, head, step):
        i = 1
        while head and i < step:
            head = head.next
            i += 1
        if not head:
            return None
        next_head = head.next
        head.next = None
        return next_head

    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        length = 0
        current = head
        while current:
            length += 1
            current = current.next

        dummy = ListNode()
        dummy.next = head

        step = 1
        while step < length:
            current = dummy.next
            tail = dummy
            while current:
                left = current
                right = self.split(left, step)
                current = self.split(right, step)
                tail.next = self.merge(left, right) # Fix here
                while tail.next:
                    tail = tail.next
            step *= 2

        return dummy.next