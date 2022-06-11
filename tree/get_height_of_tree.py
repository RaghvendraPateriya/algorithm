"""
Get the height of tree. 

"""



class Node:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def get_height(root):

    if not root:
        return 0
    
    return 1 + max(get_height(root.left), get_height(root.right))


# Driver Code
if __name__ == '__main__':
    # Create Tree
    root = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))

    print(get_height(root))