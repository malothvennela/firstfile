class Node:
    def__init__(self, data): 
    self.data = data
    self.next = Node
class CircularLinkedList:
    def__init__(self):
        self.head = None
    def append(self,data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            new_node = Node(data)
            cur_node = self.head
        while True:
print(cur_node.data, end=" ")
    cur_node = cur_node.next
        if cur_node == self.head:
        break
print()
        def count_nodes(self):
            cur_node = self.head
            count = 1
            while cur_node.next != self.head:
                cur_node = cur_node.next
                count += 1
                return count
