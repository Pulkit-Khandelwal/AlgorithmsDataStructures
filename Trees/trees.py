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
        self.root = None

    def insert(self, key, data):
        node = Node(key, data)
        node.left_child = None
        node.right_child = None
        node.parent = None

        def insert_left(current_node):
            if current_node.left_child is None and node.key <= current_node.key:
                current_node.left_child = node
                node.parent = current_node
            elif node.key <= current_node.key:
                current_node = current_node.left_child
                insert_left(current_node)
            else:
                insert_right(current_node)

        def insert_right(current_node):
            if current_node.right_child is None and node.key >= current_node.key:
                current_node.right_child = node
                node.parent = current_node
            elif node.key >= current_node.key:
                current_node = current_node.right_child
                insert_right(current_node)
            else:
                insert_left(current_node)

        if self.root is None:
            self.root = node

        elif node.key <= self.root.key:
            insert_left(self.root)

        else:
            insert_right(self.root)

    def in_order_traversal(self):
        def in_order(x):
            if x is not None:
                in_order(x.left_child)
                print(x.key)
                in_order(x.right_child)

        print(self.root)
        in_order(self.root)

    def pre_order_travsersal(self):
        def pre_order(x):
            if x is not None:
                print(x.key)
                pre_order(x.left_child)
                pre_order(x.right_child)

        pre_order(self.root)

    def post_order_travsersal(self):
        def post_order(x):
            if x is not None:
                post_order(x.left_child)
                post_order(x.right_child)
                print(x.key)

        post_order(self.root)

    def level_order_traversal(self, num_nodes):
        nodes_in_level_order = []
        nodes_in_level_order.append(self.root)

        for i in range(num_nodes):
            if nodes_in_level_order[i].left_child is not None:
                nodes_in_level_order.append(nodes_in_level_order[i].left_child)

            if nodes_in_level_order[i].right_child is not None:
                nodes_in_level_order.append(nodes_in_level_order[i].right_child)

        nodes_level_keys = [x.key for x in nodes_in_level_order]

        return nodes_level_keys


if __name__ == '__main__':
    bst = BST()
    bst.insert(5, 4)
    bst.insert(3, 4)
    bst.insert(79, 4)
    bst.insert(7, 4)
    bst.insert(2, 4)
    bst.insert(9, 4)
    bst.insert(0, 4)
    bst.insert(3, 4)
    bst.insert(8, 4)
    bst.insert(6, 4)
    bst.insert(4, 6)
    k = bst.root.right_child
    print(k.parent)
    print(k.parent.key)
    print(bst.root, bst.root.key, bst.root.right_child.left_child)
    print(bst.root.right_child.left_child.right_child.left_child.key)

    print('Traversals')
    #bst.in_order_traversal()
    #bst.pre_order_travsersal()
    bst.post_order_travsersal()
    level_order_nodes = bst.level_order_traversal(11)
    print(level_order_nodes)
