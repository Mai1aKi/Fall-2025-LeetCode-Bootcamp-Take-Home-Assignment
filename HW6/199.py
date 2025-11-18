# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque

def list_to_tree(arr):
    if not arr:
        return None

    root = TreeNode(arr[0])
    q = deque([root])
    i = 1

    while q and i < len(arr):
        node = q.popleft()

        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            q.append(node.left)
        i += 1

        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            q.append(node.right)
        i += 1

    return root

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []

        q = deque([root])
        res = []

        while q:
            size = len(q)
            for i in range(size):
                node = q.popleft()

                if i == size - 1:
                    res.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return res


Sol = Solution()

# Example 1
root1 = list_to_tree([1,2,3, None,5, None,4])
print(Sol.rightSideView(root1))   # [1, 3, 4]

# Example 2
root2 = list_to_tree([1,2,3,4, None, None, None, 5])
print(Sol.rightSideView(root2))   # [1, 3, 4, 5]

# Example 3
root3 = list_to_tree([1, None, 3])
print(Sol.rightSideView(root3))   # [1, 3]

# Example 4
root4 = list_to_tree([])
print(Sol.rightSideView(root4))   # []
