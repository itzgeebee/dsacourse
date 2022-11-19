from BinaryNode import BinaryNode


def walk(curr: BinaryNode | None, path: list[int]) -> list[int]:
    if not curr:
        return path

    path.append(curr.value)
    walk(curr.left, path)
    walk(curr.right, path)

    return path


def pre_order_search(head: BinaryNode) -> list[int]:
    return walk(head, [])


from tree import tree

print(pre_order_search(tree))
