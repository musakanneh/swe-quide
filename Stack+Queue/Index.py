# 155. Min Stack
import collections


class Solution(object):

    def __init__(self):
        self.items = []

    def push(self, item):
        current_min = self.get_min()
        if current_min == None or current_min > item:
            current_min = item
        self.items.append((item, current_min))

    def pop(self):
        self.items.pop()

    def top(self):
        return self.items[-1][0] if self.items else None

    def get_min(self):
        return self.items[-1][1] if self.items else None


obj = Solution()
obj.push(-2)
obj.push(-2)
obj.push(0)
obj.push(-3)
obj.get_min()  # return -3
obj.pop()
obj.top()  # return 0
# print(obj.get_min())  # return -2


# 20. Valid Parentheses
class Solution(object):

    def isEqual(self, c1, c2):
        if c1 == '(' and c2 == ')':
            return True
        if c1 == '(' and c2 == ')':
            return True
        if c1 == '(' and c2 == ')':
            return True
        return False

    def balancedBrackets(self, string):
        stack = []
        for characters in string:
            if len(stack) != 0:
                li = stack[-1]
                if self.isEqual(li, characters):
                    stack.pop()
                    continue
            stack.append(characters)
        return len(stack) == 0


# string = Solution()
string = "([])(){(())()()"
# print(Solution().balancedBrackets(string))


# 103. Binary Tree Zigzag Level Order Traversal
"""
Algorithms
Create a queue th
Traverse the list, get unique element from each iterations and append them to an ans array
"""


class Solution(object):

    def level_order(self, root):
        if root is None:
            return ans

        ans = []
        q = deque([root])

        while q:
            n = len(q)
            temp = []

            for i in range(0,  n):
                f = q.popleft()
                temp.append(f.val)

                if f.left is not None:
                    q.append(f.left)
                if f.right is not None:
                    q.append(f.right)

            if len(temp) > 0:
                ans.append(temp[:])
                temp.clear()

        return ans


root = [3, 9, 20, 15, 7]
# print(Solution().zigzag_level_traversal(root))


# 103. Binary Tree Zigzag Level Order Traversal
"""
Use BFS to traverse the tree level by level
 
"""

# Definition for a binary tree node.
# class TreeNode:
#     def init(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = collections.deque()

        zigzag = False
        q.append(root)

        while q:
            level = []
            for _ in range(len(q)):
                if zigzag:
                    node = q.pop()
                    level.append(node.val)
                    if node.right:
                        q.appendleft(node.right)
                    if node.left:
                        q.appendleft(node.left)

                else:
                    node = q.popleft()
                    level.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            res.append(level)
            zigzag = not zigzag

        return res


root = [3, 9, 20, 15, 7]
# print(Solution().zigzag_level_traversal(root))


# 145. Binary Tree Postorder Traversal
"""
Create two stacks
1. s1 to substitute the co-stack we have a recursive solution
2. s2 to act as a container of our solution
so, we take elements from s1 and append it to s2 and that's all

"""

class Solution(object):
    def post_order_traversal(self, root):
        if not root:
            return

        ans = []
        s1 = []
        s2 = []

        s1.append(root)

        while s1:
            x = s1[-1]
            s1.pop()
            s2.append(x)

            if x.left:
                s1.append(x.left)
            if x.right:
                s1.append(x.right)

        while s2:
            y = s2[-1]
            s2.pop()
            ans.append(y.val)

        return ans


root = [1, null, 2, 3]
print(Solution().post_order_traversal())
