class LinkNode:
    def __init__(self, val: int):
        """
        This represents a single node of a singly linkedlist
        :param val: The value of the node
        """
        self.val: int = val
        self.next: LinkNode | None = None


class LinkedList:
    def __init__(self, value):
        """
        This represents a singly linkedlist class

        :param value: The value of the first node
        """
        if not value:
            self._head = None
            self._tail = None
            self._length = 0

        node: LinkNode = LinkNode(value)
        self._head = node
        self._tail = node
        self._length = 1

    def prepend(self, item) -> None:
        """
        Adds a node to the beginning of the linkedlist
        :param item:  The value of the node
        :return:
        """
        node: LinkNode = LinkNode(item)
        if not self._length:
            self._head = node
            self._tail = node
        else:
            node.next = self._head
            self._head = node
        self._length += 1

    def insertAt(self, idx: int, value) -> None:
        """
        Inserts a node at a specific index
        :param idx:  The index of the node
        :param value: The value of the node
        :return:
        """
        if not self._length:
            return None
        if idx < 0:
            raise IndexError("Please use only positive numbers")

        if idx > self._length:
            raise IndexError("Index is out of range")

        node = LinkNode(value)
        if idx == 0:
            node.next = self._head
            self._head = node

        if idx == self._length:
            self._tail.next = node
            self._tail = node

        start_index = 1
        current_node = self._head
        while start_index < self._length and node:
            if idx == start_index:
                node.next = current_node.next
                current_node.next = node
                self._length += 1
                return

            current_node = current_node.next
            start_index += 1
        self._length += 1

    def append(self, item: int):
        """
        Adds a node to the end of the linkedlist
        :param item:  The value of the node
        :return:
        """
        node: LinkNode = LinkNode(item)
        if not self._length:
            self._head = node
            self._tail = node
        else:
            self._tail.next = node
            self._tail = node
        self._length += 1

    def iterate(self):
        """
        Iterates through the linkedlist
        :return:

        """
        if not self._length:
            return None
        node: LinkNode = self._head
        while node:
            print(node.val)
            node = node.next

    def pop(self):
        """
        Removes the last node of the linkedlist
        :return:
        """
        if not self._length:
            return None

        return_node = self._head
        current_node = self._head

        while return_node.next:
            current_node = return_node
            return_node = return_node.next

        self._tail = current_node
        self._tail.next = None

        self._length -= 1

        if not self._length:
            self._head = None
            self._tail = None

        return return_node.val

    def shift(self):
        """
        Removes the first node of the linkedlist
        :return:
        """
        node = self._head

        self._head = self._head.next

        self._length -= 1

        if not self._length:
            self._tail = None

        return node.val

    def remove(self, item):
        """
        Removes a node from the linkedlist
        :param item: item to be removed
        :return:
        """

        temp_node = self._head
        current_node = self._head

        while temp_node:
            if temp_node.val == item:
                current_node.next = temp_node.next
                if item == self._head.val:
                    self._head = self._head.next
                self._length -= 1
                if not self._length:
                    self._tail = None
                return
            current_node = temp_node
            temp_node = temp_node.next
        raise ValueError('Value not found in list')

    def set(self, idx: int, value):
        """
        set the value of a node by its index
        :param idx: the index of the node
        :param value: the value of the node
        :return:
        """
        if idx >= self._length:
            raise IndexError("Index is out of range")
        if idx == 0:
            self._head.val = value
            return

        if idx == self._length - 1:
            self._tail.val = value
            return

        node = self._head.next
        starting_index = 1

        while starting_index < self._length and node:
            if idx == starting_index:
                node.val = value
                return

            node = node.next
            starting_index += 1

    def get(self, idx: int):
        """
        Gets a node from the linkedlist
        :param idx:  The index of the node
        :return:
        """

        if idx > self._length:
            raise IndexError("index is out of range")

        if idx == 0:
            return self._head.val

        if idx == self._length - 1:
            return self._tail.val

        starting_index = 1
        current_node = self._head.next

        while starting_index < self._length and current_node:
            if idx < 0:
                idx += self._length

            if idx == starting_index:
                return current_node.val

            current_node = current_node.next
            starting_index += 1

    def removeAt(self, idx: int):
        """
        Removes a node from the linkedlist a specific index
        :param idx:index of the item to remove
        :return:
        """
        if 0 > idx < self._length:
            raise IndexError('Index is out of range')

        if idx == 0:
            self._head = self._head.next

        if idx == self._length - 1:
            self._tail = None

        starting_index = 1
        current_node = self._head
        temp = self._head.next

        while starting_index < self._length and temp:

            if idx == starting_index:
                current_node.next = temp.next

                break

            current_node = current_node.next
            temp = temp.next
            starting_index += 1

        self._length -= 1
        if not self._length:
            self._tail = None

    def __len__(self):
        return self._length

    # print linkedlist out as a list
    def __iter__(self):
        node = self._head
        while node:
            yield node.val
            node = node.next

    def __getitem__(self, item: int):
        return self.get(item)

    def __setitem__(self, key: int, value):
        return self.set(key, value)

    def __delitem__(self, key: int):
        return self.removeAt(key)

    # print out linkedliest as a list in square brackets
    def __repr__(self):
        return f"[{', '.join(str(item) for item in self)}]"

    # Add two linkedlists together
    def __add__(self, other):
        if not isinstance(other, LinkedList):
            raise TypeError('Can only add two linkedlists together')

        new_linkedlist = LinkedList()
        for item in self:
            new_linkedlist.append(item)
        for item in other:
            new_linkedlist.append(item)

        return new_linkedlist

if __name__ == '__main__':
    a = LinkNode(1)
    b = LinkNode(2)
    c = LinkNode(3)
    d = LinkNode(5)

    linked_list = LinkedList(0)
    new_linked_list = LinkedList(1)
    new_linked_list.append(2)
    new_linked_list.append(3)
    new_linked_list.append(4)
    new_linked_list.append(5)
    new_linked_list.append(6)
    linked_list.append(2)
    linked_list.insertAt(0, 4)
    linked_list.insertAt(0, 4)
    linked_list.insertAt(1, 3)
    linked_list.insertAt(2, 2)
    linked_list.prepend(2)
    popped = linked_list.pop()
    shifted = linked_list.shift()
    linked_list.remove(4)
    linked_list.insertAt(4, "a")
    linked_list.set(3, 9)
    linked_list.removeAt(4)
    linked_list[2] = 7

    for i in linked_list:
        print(i)

    print("length", (len(linked_list)))
    print("get item", linked_list[1])
    print("popped", popped)
    print("shifted", shifted)
    print(linked_list.get(-1))
    print(linked_list)

    print(new_linked_list)
