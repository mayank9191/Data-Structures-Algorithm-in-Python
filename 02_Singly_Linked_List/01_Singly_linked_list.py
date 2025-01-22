class Sll:
    def __init__(self, start):
        self.start = start

    def traverse(self):
        pass

    def insertion_at_last(self, item):
        pass

    def insertion_at_start(self, item):
        pass

    def insertion_at_specified(self, item):
        pass


class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next


node1 = Node(1)
start = Sll(id(node1))

node2 = Node(2)
node1.next = id(node2)


print("hello")
