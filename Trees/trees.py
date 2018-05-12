"""
Implementation of Trees

The BST implemented here is as per the description given in CLRS.
Page253-254 second edition.
"""


class Node(object):
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left_child = None
        self.right_child = None
        self.parent = None


class BST(object):
    def __init__(self):
        self.counter = 0
        self.root = None

    def insert(self, key, data):
        node = Node(key, data)
        node.left_child = None
        node.right_child = None
        node.parent = None

        def insert_left(current_node):
            if current_node.left_child is None:
                current_node.left_child = node
                node.parent = current_node
            elif node.key <= current_node.key:
                current_node = current_node.left_child
                insert_left(current_node)
            else:
                current_node = current_node.right_child
                insert_right(current_node)

        def insert_right(current_node):
            if current_node.right_child is None:
                current_node.right_child = node
                node.parent = current_node
            elif node.key >= current_node.key:
                current_node = current_node.right_child
                insert_right(current_node)
            else:
                current_node = current_node.left_child
                insert_left(current_node)

        if self.counter is 0:
            self.root = node
            self.counter += 1

        elif node.key <= self.root.key:
            insert_left(self.root)

        else:
            insert_right(self.root)


if __name__ == '__main__':
    bst = BST()
    bst.insert(5, 4)
    bst.insert(3, 4)
    bst.insert(7, 4)
    bst.insert(2, 4)
    bst.insert(8, 4)
    k = bst.root.right_child.right_child
    print(k.parent)
    print(k.parent.key)
    print(bst.counter, bst.root, bst.root.key, bst.root.right_child.left_child)
