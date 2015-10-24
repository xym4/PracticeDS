from Node import Node

class Stack:
    def __init__(self):
        self.head = Node()
        self.end = Node()
        self.head.next = self.end
        self.end.previous = self.head
        self.size = 0

    def push(self, value):
        new_node = Node(value, None, None)
        new_node.previous = self.end.previous
        new_node.next = self.end
        self.end.previous.next = new_node
        self.end.previous = new_node
        self.size += 1

    def top(self):
        return self.head

    def pop(self):
        if self.end.previous == self.head:
            print("Nothing to pop")
            return None
        else:
            to_be_removed = self.end.previous
            self.end.previous = to_be_removed.previous
            to_be_removed.previous.next = self.end
            to_be_removed.next = None
            to_be_removed.previous = None
            self.size -= 1
            del to_be_removed

    def __str__(self):
        string = ""
        cur = self.head.next
        while cur != self.end:
            string += str(cur.value) + " "
            cur = cur.next

        return string


#
# s = Stack()
# s.push(1)
# s.push(2)
# s.push(3)
# s.pop()
# print(s.size)
# s.push(4)
# s.push(5)
# print(s, s.size)