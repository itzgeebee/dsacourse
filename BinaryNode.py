class BinaryNode:
    def __init__(self, value):
        self.value = value
        self.left: BinaryNode | None = None
        self.right: BinaryNode | None = None