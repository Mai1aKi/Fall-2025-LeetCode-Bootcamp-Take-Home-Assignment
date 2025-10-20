# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev, curr = None, slow
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        
        first, second = head, prev
        while second.next:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2

sol = Solution()
# Example usage:
# Creating a linked list 1 -> 2 -> 3 -> 4
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
print("Before reordering:")
curr = head
while curr:
    print(curr.val, end=" -> " if curr.next else "\n")
    curr = curr.next
sol.reorderList(head)
print("After reordering:")
curr = head
while curr:
    print(curr.val, end=" -> " if curr.next else "\n")
    curr = curr.next

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print("Before reordering:")
curr = head
while curr:
    print(curr.val, end=" -> " if curr.next else "\n")
    curr = curr.next
sol.reorderList(head)
print("After reordering:")
curr = head
while curr:
    print(curr.val, end=" -> " if curr.next else "\n")
    curr = curr.next
