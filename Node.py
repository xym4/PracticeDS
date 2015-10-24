class Node:
    def __init__(self, value=None, next=None, previous=None):
        self.value = value
        self.next = next
        self.previous = previous

    def __str__(self):
        return str(self.value)

# a = Node(1, None, None)
# b = Node(2, None, None)
# c = Node(3, None, None)
#
# a.next = b
# b.previous = a
# b.next = c
# c.previous = b
#
# print(b)



