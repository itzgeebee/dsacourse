
class StackNode:
    def __init__(self, data):
        """
        This represents a node in a stack
        :param data:  The value of the node
        """
        self.val = data
        self.next = None

class Stack:
    def __init__(self):
        self._head = None
        self._length = 0

    def push(self, value):
        node = StackNode(value)
        self._length += 1

        if not self._head:
            self._head = node
            return

        node.next = self._head
        self._head = node

    def pop(self):

        self._length = max(0, self._length - 1)

        if not self._head:
            return

        node = self._head
        self._head = node.next

        return node.val

    def peek(self):
        return self._head.val

    def __len__(self):
        return self._length

    def __repr__(self):
        node = self._head
        string_list = []
        while node:
            string_list.append(f"{node.val} -> ")
            node = node.next
        return "".join(string_list)


if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    print(stack)
    print(stack.pop())
    print(stack)
    print(stack.peek())
    print(stack)
    print(len(stack))
