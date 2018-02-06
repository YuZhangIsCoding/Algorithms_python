#!/Users/yuzhang/programs/anaconda/bin/python
# Description:  this is a script to test how the external functions could also
#               change the attributes of the class.

class BST(object):
    def __init__(self):
        self.left = None
        self.right = None

    def update_height(self):
        BST._update_height(self)

    @staticmethod
    def _height(node):
        if node:
            return node.height
        else:
            return -1
    def _update_height(node):
        node.height = max(BST._height(node.left), BST._height(node.right))+1

node = BST()
## Initially, the BST node does not contain the attribute height
print dir(node)
node.update_height()
## After calling update_height(), the attribute is added to the node externally.
print dir(node)
print node.height
