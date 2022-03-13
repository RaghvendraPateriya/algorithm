"""
Print Tree Level Wise:
Given Tree:

               1         <= level 0
            /     \
            2      3     <= level 1
         /    \   /   \
        4     5   6    7 <= level 2

Output: 1 2 3 4 5 6 7 

"""

class Tree:

    def __init__(self, data, left=None, right=None) -> None:
        self.data = data
        self.left = left
        self.right = right


# In Order Traversal
# In Given Input Tree
# Output: 4 -> 2 -> 5 -> 1 -> 6 -> 3 -> 7
# Steps:
# 1. Traverse Left sub tree
# 2. Traverse Root node
# 3. Traversr Right sub tree
#  Left -> root -> right
def in_order_traversal(root_node):
    node = root_node
    if (node):
        in_order_traversal(node.left)
        print(node.data)
        in_order_traversal(node.right)


# In Pre Order Traversal [ up to bottom]
# In Given Input Tree
# Output: 1 -> 2 -> 4 -> 5 -> 3 -> 6 -> 7
# Steps:
# 1. Traverse Root node
# 2. Traverse Left subtree
# 3. Traverse Right subtree
#  Root -> Left -> Right
def pre_order_traversal(root_node):
    node = root_node
    if (node):
        print(node.data)
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)


# In Post Order Traversal [bottom to up]
# In Given Input Tree
# Output: 4 -> 5 -> 2 -> 6 -> 7 -> 3 -> 1
# Steps:
# 1. Traverse Left Sub Tree
# 2. Traverse Right Sub Tree
# 3. Traverse root node
#  Left -> Right -> Root
def post_order_traversal(root_node):
    node = root_node
    if (node):
        post_order_traversal(node.left)
        post_order_traversal(node.right)
        print(node.data)


# Print Tree Level Wise
def traverse_tree_level_wise(root_node):
    node = root_node
    node_list = [node]
    while node_list:
        temp_list = []
        for nl in node_list:
            print(nl.data)
            if nl.left:
                temp_list.append(nl.left)
            if nl.right:
                temp_list.append(nl.right)
        node_list = temp_list


if __name__ == '__main__':
    # Create Tree
    root_node = Tree(1, Tree(2, Tree(4), Tree(5)), Tree(3, Tree(6), Tree(7)))
    # Print tree left node first
    #print_tree(root_node)
    # Print Tree Level Wise
    # traverse_tree_level_wise(root_node)
    # in_order_traversal(root_node)
    # pre_order_traversal(root_node)
    post_order_traversal(root_node)    
    