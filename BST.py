class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value > self.value:
            if self.right == None:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)
        else:
            if self.left == None:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)

    def lookup(self, value, parent=None):
        if self.value == value:
            return self, parent
        else:
            if value > self.value:
                if self.right == None:
                    return None, None
                else:
                    return self.right.lookup(value, self)
            else:
                if self.left==None:
                    return None, None
                else:
                    return self.left.lookup(value, self)

    def find_min(self):
        if self.left == None:
            return self
        else:
           return self.left.find_min()

    def remove(self, value):
        node, parent = self.lookup(value)
        if node == None:
            return "Not in tree."
        else:
            if node.left == None and node.right == None:
                print("and")
                if node.value > parent.value:
                    parent.right = None
                else:
                    parent.left = None
                del node
            elif self.left != None and self.right != None:
                min_right_node = node.find_min()
                node.value = min_right_node.value
                node.left = None
                del min_right_node
            else:
                print("XOR")
                child = None
                if node.left == None:
                    child = node.right
                else:
                    child = node.left

                if node.value > parent.value:
                    parent.right = child
                else:
                    parent.left = child

# tree = TreeNode(8)
# tree.insert(3)
# tree.insert(10)
# tree.insert(1)
# tree.insert(6)
# tree.insert(4)
# tree.insert(7)
# tree.insert(14)
# tree.insert(13)

# print(tree.left.value)
# print(tree.left.right.right.value)

# tree.remove(6)
# print(tree.left.value)
# print(tree.left.right.left.value)





# node, parent = tree.lookup(6)
# print(node.find_min().value)
# print(tree.lookup(6))


# print(tree.left.left.right)

#
# flag, node = tree.lookup(13)
#
# print(flag, node.value)
