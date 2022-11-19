class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self):
        self.__head: Node | None = None
        self.__tail: Node | None = None
        self.__length: int = 0

    def prepend(self, item) -> None:
        node: Node = Node(item)

        self.__length += 1

        if not self.__head:
            self.__head = self.__tail = node
            return

        node.next = self.__head
        self.__head.prev = node
        node = self.__head

    def append(self, item) -> None:
        node: Node = Node(item)

        self.__length += 1

        if not self.__head:
            self.__head = self.__tail = node
            return

        node.prev = self.__tail
        self.__tail.next = node
        self.__tail = node

    def insert_at(self, item, idx: int) -> None:
        if idx > self.__length:
            raise IndexError("idx is out of range")
        elif idx == self.__length:
            self.append(item)
            return
        elif idx == 0:
            self.prepend(item)
            return

        curr: Node = self._get_at(idx)
        node: Node = Node(item)

        node.next = curr
        node.prev = curr.prev
        curr.prev.next = node
        curr.prev = node

    def remove(self, item):
        curr = self.__head

        for i in range(self.__length):
            if curr.value == item:
                break

            curr = curr.next

        if not curr:
            return None

        return self._remove_node(curr)

    def get(self, idx: int):
        return self._get_at(idx).value

    def remove_at(self, idx:int):
        node = self._get_at(idx)

        if not node:
            return None

        return self._remove_node(node)

    def _remove_node(self, node: Node):
        self.__length -= 1

        if self.__length == 0:
            out = self.__head.value
            self.__head = self.__tail = None
            return out

        if node.prev:
            node.prev.next = node.next

        if node.next:
            node.next.prev = node.prev

        if node == self.__head:
            self.head = node.next

        if node == self.__tail:
            self.__tail = node.prev

        node.prev = node.next = None
        return node.value

    def _get_at(self, idx) -> Node:
        curr = self.__head

        for i in range(idx):
            curr = curr.next

        return curr

    def __len__(self):
        return self.__length

    def __iter__(self):
        curr = self.__head

        while curr:
            yield curr.value
            curr = curr.next

    def __getitem__(self, idx):
        return self.get(idx)

    def __setitem__(self, idx, value):
        node = self._get_at(idx)
        node.value = value

    def __delitem__(self, idx):
        self.remove_at(idx)

    def __repr__(self):
        return  f"[{', '.join(str(item) for item in self)}]"

if __name__ == "__main__":
    l = DoublyLinkedList()
    for i in range(10):
        l.append(i)

    print(l)
    l.insert_at(10, 0)
    print(l)
    l.insert_at(11, 5)
    print(l)
    l.remove_at(3)
    print(l)
    l.remove(2)
    print(l)

    print(l[5])

