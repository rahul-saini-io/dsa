class BST:
    def __init__(self, value):
        self.value = value
        self.left, self.right = None, None

    def find_closest_val(self, target):
        """ Assume we already have a BST """
        current = self
        closest = current.value
        while current:
            if abs(target-closest) > abs(target-current.value):
                closest = current.value
            if target < current.value:
                current = current.left
            elif target > current.value:
                current = current.right
            else:
                break

        return closest