from Node import Node

class LinkedList:
    def __init__(self, head=None):
        self.head = Node()
        self.end = Node()
        self.head.next = self.end
        self.end.previous = self.head
        self.size = 0

    def insert(self, value):
        new_node = Node(value, None, None)
        cur = self.head
        while cur.next != self.end:
            cur = cur.next
        cur.next = new_node
        new_node.previous = cur
        new_node.next = self.end
        self.end.previous = new_node
        self.size+=1

    def find_node(self, value):
        cur = self.head.next
        while cur != self.end:
            if cur.value == value:
                print("Value found in list")
                return cur
            else:
                cur = cur.next
        print("Error, not found in list")
        return None

    def delete_node(self, value):
        found_node = self.find_node(value)
        if found_node != None:
            found_node.previous.next = found_node.next
            found_node.next.previous = found_node.previous
            self.size -= 1
        else:
            print("Error, cannot delete value. not in list.")

    def get_size(self):
        return self.size

    def __str__(self):
        cur = self.head.next
        string = ""
        while cur != self.end:
            string += str(cur.value) + " "
            cur = cur.next
        return string

# ll = LinkedList()
# print(ll, ll.get_size())
# ll.insert(1)
# print(ll, ll.get_size())
# ll.insert(2)
# print(ll, ll.get_size())
# ll.insert(3)

# ll.find_node(1)
# ll.find_node(2)
# ll.find_node(3)
# ll.find_node(4)
# ll.delete_node(1)
# print(ll, ll.get_size())
# ll.insert(44)
# print(ll, ll.get_size())






