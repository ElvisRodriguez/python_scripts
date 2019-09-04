class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        current_node = self.head
        result = []
        while current_node:
            result.append(current_node.data)
            current_node = current_node.next
        print(result)

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Node does not exist")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        current_node = self.head
        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return
        previous_node = None
        while current_node and current_node.data != key:
            previous_node = current_node
            current_node = current_node.next
        if current_node is None:
            print("Key not in list")
            return
        previous_node.next = current_node.next
        current_node = None

    def delete_node_at_pos(self, pos):
        current_node = self.head
        if current_node and pos == 0:
            self.head = current_node.next
            current_node = None
            return
        previous_node = None
        count = 0
        while current_node and count < pos:
            previous_node = current_node
            current_node = current_node.next
            count += 1
        if current_node is None:
            print("Position out of bounds")
            return
        previous_node.next = current_node.next
        current_node = None

    def len_iterative(self):
        current_node = self.head
        count = 0
        while current_node:
            count += 1
            current_node = current_node.next
        return count

    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)

    def find_node(self, key):
        current_node = self.head
        while current_node and current_node.data != key:
            current_node = current_node.next
        if current_node is None:
            return None
        return current_node

    def swap_nodes(self, key1, key2):
        if key1 == key2:
            return
        previous1 = None
        current1 = self.head
        while current1 and current1.data != key1:
            previous1 = current1
            current1 = current1.next
        previous2 = None
        current2 = self.head
        while current2 and current2.data != key2:
            previous2 = current2
            current2 = current2.next
        if current1 is None or current2 is None:
            return
        if previous1:
            previous1.next = current2
        else:
            self.head = current2
        if previous2:
            previous2.next = current1
        else:
            self.head = current1
        current1.next, current2.next = current2.next, current1.next

    def reverse_iterative(self):
        previous_node = None
        current_node = self.head
        while current_node:
            nxt = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = nxt
        self.head = previous_node

    def reverse_recursive(self):
        def _reverse_recursive(previous_node, current_node):
            if not current_node:
                return previous_node
            nxt = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = nxt
            return _reverse_recursive(previous_node, current_node)
        self.head = _reverse_recursive(previous_node=None,
                                       current_node=self.head)

    def merge_sorted(self, llist): #merge list in place
        p = self.head
        q = llist.head
        s = None
        if not p:
            return q
        if not q:
            return p
        if p and q:
            if p.data < q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
            new_head = s
        while p and q:
            if p.data < q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
        if not p:
            s.next = q
        if not q:
            s.next = p
        return new_head

    def remove_duplicates(self):
        logbook = {}
        current = self.head
        previous = None
        while current:
            if current.data in logbook:
                previous.next = current.next
                current = None
            else:
                logbook[current.data] = 1
                previous = current
            current = previous.next

    def print_nth_from_last(self, n):
        p = self.head
        q = self.head
        count = 0
        while q and count < n:
            q = q.next
            count += 1
        if not q:
            print(n, "is greater than the number of nodes - 1 in the list")
            return
        while q:
            p = p.next
            q = q.next
        print(p.data)

    def count_occurences_iterative(self, data):
        current = self.head
        count = 0
        while current:
            if current.data == data:
                count += 1
            current = current.next
        return count

    def count_occurences_recursive(self, node, data):
        if not node:
            return 0
        if node.data == data:
            return 1 + self.count_occurences_recursive(node.next, data)
        else:
            return self.count_occurences_recursive(node.next, data)

    def rotate(self, k):
        count = 1
        p = self.head
        q = self.head
        while p and count < k:
            p = p.next
            q = p
            count += 1
        if not p:
            return
        while q.next:
            q = q.next
        q.next = self.head
        self.head = p.next
        p.next = None

    def is_palindrome(self):
        if not self.head:
            return
        string = ""
        current = self.head
        while current:
            string += str(current.data)
            current = current.next
        return string == string[::-1]

    def move_tail_to_head(self):
        previous = None
        current = self.head
        while current.next:
            previous = current
            current = current.next
        previous.next = None
        current.next = self.head
        self.head = current

    def sum_two_list(self, llist):
        nums = ["", ""]
        p = self.head
        q = llist.head
        while p and q:
            nums[0] = str(p.data) + nums[0]
            nums[1] = str(q.data) + nums[1]
            if p:
                p = p.next
            if q:
                q = q.next
        return int(nums[0]) + int(nums[1])


def merge_linked_list(llistA, llistB): #return a new, merged, sorted linked list
    result = LinkedList()
    current1 = llistA.head
    current2 = llistB.head
    while current1 and current2:
        if current1.data < current2.data:
            result.append(current1.data)
            current1 = current1.next
        else:
            result.append(current2.data)
            current2 = current2.next
    while current1:
        result.append(current1.data)
        current1 = current1.next
    while current2:
        result.append(current2.data)
        current2 = current2.next
    return result
