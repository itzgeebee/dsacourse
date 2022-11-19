from BinaryNode import BinaryNode


def walk(curr: BinaryNode | None, path: list[int]) -> list[int]:
    if not curr:
        return path

    walk(curr.left, path)
    walk(curr.right, path)
    path.append(curr.value)

    return path


def post_order_search(head: BinaryNode) -> list[int]:
    return walk(head, [])

from tree import tree

print(post_order_search(tree))
