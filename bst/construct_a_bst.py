class BST:
    def __init__(self, value):
        self.value = value
        self.left, self.right = None, None

    def insert(self, value):

        current = self
        while True:
            if value < current.value:
                if current.left is None:
                    # end/leaf node is found add here
                    current.left = BST(value)
                    break
                # keep on going to left
                current = current.left
            else:
                if current.right is None:
                    current.right = BST(value)
                    break
                current = current.right

        return self

    def contains(self, value):
        current = self

        while current:
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                # node found
                return True

        return False


    def remove(self, value):
        parent = None
        current = self

        while current:
            if value < current.value:
                parent = current
                current = current.left
            elif value > current.value:
                parent = current
                current = current.right
            else:
                # node found
                """
                    we need to cover 4 case
                    1. just root and no leaf/child do nothing
                    2. root/ node with just 1 child
                    3. leaf node
                    4. node with two child/ leaf
                """
                if current.left is None or current.right is None:
                    # case 1, 2, 3
                    child = current.left if current.left else current.right

                    if parent is None:
                        # root node
                        if child:
                            # check if not just root node
                            self.value = child.value
                            self.left = child.left
                            self.right = child.right
                            break
                        else:
                            # just root node we cannot set self = None in python but we can do the following but a empty node still exists
                            self.value, self.left, self.right = None, None, None
                            break
                    elif parent.left == current:
                        parent.left = child
                    else:
                        parent.right = child
                    break
                else:
                    # case 4
                    """ 
                        here we need to go to the right of the current node(to be removed node)
                        and then go the left most node if exists and replace the current node's value
                        and the remove the successor node
                    """
                    successor_parent = current
                    successor = current.right

                    while successor.left:
                        successor_parent = successor
                        successor = successor.left

                    current.value = successor.value

                    # now delete the successor node
                    if successor_parent.left == successor:
                        successor_parent.left = successor.right
                    else:
                        successor_parent.right = successor.right

                    break

        return self

