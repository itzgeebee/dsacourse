from BinaryNode import BinaryNode


def walk(curr: BinaryNode | None, path: list[int]) -> list[int]:
    if not curr:
        return path

    walk(curr.left, path)
    path.append(curr.value)
    walk(curr.right, path)

    return path


def in_order_search(head: BinaryNode) -> list[int]:
    return walk(head, [])


from tree import tree

print(in_order_search(tree))
