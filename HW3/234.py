# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        if not head or not head.next:
            return True
        
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
        while second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        
        return True
    
sol = Solution()
# Example usage:

# Creating a linked list 1 -> 2 -> 2 -> 1
head = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
print("Is palindrome?", sol.isPalindrome(head))  # Output: True

# Creating a linked list 1 -> 2
head = ListNode(1, ListNode(2))
print("Is palindrome?", sol.isPalindrome(head))  # Output: False
