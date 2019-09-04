class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class BST(object):
    def __init__(self):
        self.root = None

    def _insert(self, data, node):
        if data > node.data:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert(data, node.right)
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert(data, node.left)

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _search(self, data, node):
        if data > node.data and node.right:
            return self._search(data, node.right)
        if data < node.data and node.left:
            return self._search(data, node.left)
        if data == node.data:
            return True

    def search(self, data):
        if self.root:
            is_found = self._search(data, self.root)
            return is_found
        return None

    def inorder(self, traversal, start):
        if start:
            traversal = self.inorder(traversal, start.left)
            traversal.append(start.data)
            traversal = self.inorder(traversal, start.right)
        return traversal

    def _has_BST_property(self, traversal, start):
        if start:
            traversal = self._has_BST_property(traversal, start.left)
            traversal.append(start.data)
            traversal = self._has_BST_property(traversal, start.right)
        return traversal

    def has_BST_property(self):
        traversed = self._has_BST_property([], self.root)
        for i in range(len(traversed) - 1):
            if traversed[i] > traversed[i+1]:
                return False
        return True

    def __str__(self):
        result = self.inorder([], self.root)
        return str(",".join(map(str, result)))


def binary_tree_sort(unsorted_list):
    tree = BST()
    for num in unsorted_list:
        tree.insert(num)
    return tree.inorder([], tree.root)

test = [10, 1, 9, 2, 8, 3, 7, 4, 6, 5]
print(binary_tree_sort(test))
