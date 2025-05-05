from collections import deque

class treenode:
    def __init__(self,value,left = None,right= None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)


def dfs(node):
    if not node:
        return 
    print(node)
    dfs(node.left)
    dfs(node.right)

def bfs(node):
    q = deque()
    q.append(node)

    while q:
        node = q.popleft()
        print(node)
        if node.left :q.append(node.left)
        if node.right :q.append(node.right)


node1 = treenode(1)
node2 = treenode(2)
node3 = treenode(3)
node4 = treenode(4)
node5 = treenode(5)
node6 = treenode(6)
node7 = treenode(7)
node8 = treenode(8)
node9 = treenode(9)
node10 = treenode(10)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.right = node6
node6.left = node7
node6.right = node8
node8.left = node9
node8.right = node10


bfs(node1)
# dfs(node1)