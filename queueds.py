from singlyLinkedList import LinkNode
class Queue:


    def __init__(self):
        """
        Initializes the queue
        """
        self._head = self._tail = None
        self._length = 0

    def enqueue(self, value):
        """
        Adds a node to the end of the queue
        :param value:  The value of the node
        :return:
        """
        node = LinkNode(value)
        self._length += 1
        if not self._tail:
            self._tail = self._head = node
            return

        self._tail.next = node
        self._tail = node

    def dequeue(self):
        """
        Removes the first node of the queue
        :return:  The value of the node
        """
        if not self._head:
            return

        self._length = max(0, (self._length - 1))
        node = self._head
        self._head = self._head.next

        return node.val

    def peek(self):
        """
        Returns the value of the first node of the queue
        :return:  The value of the node
        """
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
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    queue.enqueue(6)
    print(queue)
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())







