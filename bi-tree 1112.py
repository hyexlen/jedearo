class tree_node:
    def __init__(self, value):
        self.left = None
        self.data = None
        self.right = None

root_node = tree_node()
root.node.data = "커피"

node1 = tree_node()
Node1.data = "녹차"
root_node.left = node1

node2=tree_node()
node2.data="꿀물"
root_node.right = node2

node3=tree_node()
node3.data="아이스티"
node1.left = node3

node4=tree_node()
node4.data="레몬에이드"
node1.right = node4

node5=tree_node()
node5.data="밀크티"
node2.left= node5



print(root.node.data, end=" ")
print()
print(root_node.left, root_node.right.data, end="")
print()
print(root_node.left.left.data, root_node.left.right.data, root_node_right.left)

