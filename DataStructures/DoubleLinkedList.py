class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            new_node = Node(data)
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def prepend(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def insert_at(self, target, data, before=False):
        if self.head is None:
            raise ValueError
        if self.head.data == target:
            if before:
                self.prepend(data)
            else:
                self.append(data)
        else:
            current = self.head
            while current.next is not None and current.data != target:
                current = current.next
            if current.data != target:
                raise ValueError
            if before:
                new_node = Node(data)
                new_node.prev = current.prev
                new_node.prev.next = new_node
                new_node.next = current
                current.prev = new_node
                self.size += 1
                return
            if current.next is None:
                current.next = Node(data)
                current.next.prev = current.next
                self.tail = current.next
            else:
                new_node = Node(data)
                new_node.prev = current
                new_node.next = current.next
                current.next = new_node
                new_node.next.prev = new_node
            self.size += 1

    def delete(self, target):
        if self.head is None:
            raise ValueError
        if target == self.head.data and self.size == 1:
            del self.head
        else:
            current = self.head
            while current.next is not None and current.data != target:
                current = current.next
            if current.next is None and current.data != target:
                raise ValueError
            elif current.next is None:
                self.tail = current.prev
                self.tail.next = None
                del current
            elif current.next is not None and current != self.head:
                current.prev.next = current.next
                current.next.prev = current.prev
                del current
            elif current == self.head:
                self.head.prev = None
                self.head = self.head.next
                del current
        self.size -= 1

    def reverse(self):
        if self.size > 1:
            temp = None
            current = self.head
            while current is not None:
                temp = current.prev
                current.prev = current.next
                current.next = temp
                current = current.prev
            if temp is not None:
                self.tail = self.head
                self.head = temp.prev

    def remove_dupes(self):
        temp = []
        current = self.head
        while current is not None:
            if current.data in temp:
                self.delete(current.data)
            else:
                temp.append(current.data)
            current = current.next

    def print_list(self):
        result = []
        current = self.head
        while current is not None:
            result.append(current.data)
            current = current.next
        return result

    def __len__(self):
        return self.size

    def __str__(self):
        result = self.print_list()
        return '[{}]'.format(', '.join(result))
