'''
Using an adjacency list to represent a graph.
'''

class Graph(object):
    def __init__(self, item):
        self.head = item
        self.nodes = {item : []}

    def insert(self, item, pointed_nodes=None):
        '''
        Inserts new nodes based on the structure of an adjacency list.
        Allows for creation of nodes that can have any number of edges to other
            nodes (except for themselves).
        If no argument is given for pointed_nodes, an edge will be created with
            the starting node (self.head) and the inserted node.

        Args:
            item: An object of any type (not necessarily a node object).
            pointed_nodes: Nodes that 'item' should have edges with.

        Returns:
            None
        '''
        if item in self.nodes.keys():
            print('Item already in graph\n')
        else:
            if pointed_nodes is None:
                self.nodes[self.head].append(item)
                self.nodes[item] = []
                self.nodes[item].append(self.head)
            else:
                self.nodes[item] = []
                for node in pointed_nodes:
                    self.nodes[node].append(item)
                    self.nodes[item].append(node)

    def search(self, item):
        '''
        Breadth First search of adjacency list.

        Args:
            item: Item to be found in adjacency list.

        Returns:
            Node with an equivalent value to item if item is found, else None.
        '''
        if item == self.head:
            return self.head
        queue = []
        queue.append(self.head)
        visited = {self.head : True}
        while len(queue) > 0:
            node = queue.pop(0)
            children = self.nodes[node]
            for child in children:
                if child in visited:
                    queue.extend(x for x in self.nodes[child] if x not in visited)
                elif item == child:
                    return child
                else:
                    visited[child] = True
                    queue.extend(x for x in self.nodes[child] if x not in visited)
        return None

