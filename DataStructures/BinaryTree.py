import Stack
import Queue


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            print(self.preorder_print(self.root, []))
        elif traversal_type == "inorder":
            print(self.inorder_print(self.root, []))
        elif traversal_type == "postorder":
            print(self.postorder_print(self.root, []))
        elif traversal_type == "levelorder":
            print(self.levelorder_print(self.root))
        elif traversal_type == "reverse levelorder":
            print(self.reverse_levelorder_print(self.root))
        else:
            print("Traversal type", traversal_type, "is not supported")

    def preorder_print(self, start, traversal):
        if start:
            traversal.append(start.value)
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal.append(start.value)
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal.append(start.value)
        return traversal

    def levelorder_print(self, start):
        if start is None:
            return
        queue = Queue()
        queue.enqueue(start)
        traversal = []
        while len(queue) > 0:
            traversal.append(queue.peek())
            node = queue.dequeue()
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return traversal

    def reverse_levelorder_print(self, start):
        if start is None:
            return
        queue = Queue()
        stack = Stack()
        queue.enqueue(start)
        traversal = []
        while len(queue) > 0:
            node = queue.dequeue()
            stack.push(node)
            if node.right:
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)
        while len(stack) > 0:
            node = stack.pop()
            traversal.append(node.value)
        return traversal

    def height(self, node):
        if node is None:
            return -1
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return 1 + max(left_height, right_height)

    def insert(self, item):
        queue = Queue()
        queue.enqueue(self.root)
        while len(queue) > 0:
            node = queue.dequeue()
            if node.left:
                queue.enqueue(node.left)
            else:
                node.left = Node(item)
                return
            if node.right:
                queue.enqueue(node.right)
            else:
                node.right = Node(item)
                return

    def size(self):
        if self.root is None:
            return 0
        stack = Stack()
        count = 0
        stack.push(self.root)
        while len(stack) > 0:
            node = stack.pop()
            count += 1
            if node.left:
                stack.push(node.left)
            if node.right:
                stack.push(node.right)
        return count

    def __len__(self):
        return self.size()
