from BinaryNode import BinaryNode
from queueds import Queue
from tree import tree


def bfs(head: BinaryNode, needle: int) -> bool:
    q: Queue | None = Queue()
    q.enqueue(head)
    print(q)

    # while q:
    #     print(q)
    #     curr: BinaryNode | None = q.dequeue()
    #
    #     if not curr:
    #         continue
    #
    #     if curr.value == needle:
    #         return True
    #
    #     if curr.left:
    #         q.enqueue(curr.left)
    #
    #     if curr.right:
    #         q.enqueue(curr.right)

    return False


print(bfs(tree, 100))
