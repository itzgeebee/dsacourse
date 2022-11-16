directions = [
    [0, 1],
    [1, 0],
    [0, -1],
    [-1, 0]
]


class Point:
    def __init__(self, y: int, x: int):
        self.x = x
        self.y = y


def walk(maze: list[str], wall: str,
         curr: Point, end: Point, seen: list[list[bool]],
         path: list[Point]) -> bool:
    # Step 1
    # Base case 1 off the map
    if curr.x < 0 or curr.y >= len(maze[0]) or curr.y < 0 or curr.y >= len(maze):
        return False

    # on a wall
    if maze[curr.y][curr.x] == wall:
        return False

    # end
    if curr.x == end.x and curr.y == end.y:
        path.append(end)
        return True

    # seen
    print(curr.x, curr.y)
    if seen[curr.x][curr.y]:
        return False

    seen[curr.x][curr.y] = True
    path.append(curr)
    print(path)

    # recurse
    for direction in directions:
        x, y = direction
        new_curr: Point = Point(curr.x + x, curr.y + y)
        if walk(
                maze, wall,
                new_curr,
                end, seen, path
        ):
            return True

    # Post
    path.pop()

    return False


def solve(maze: list[str], wall: str, start: Point, end: Point) -> list[Point]:
    seen: list[list[bool]] = []
    path: list[Point] = []
    for i in maze:
        new_array: list[bool] = [False] * len(maze[0])
        seen.append(new_array)


    walk(maze, wall, start, end, seen, path)

    return path


maze = [
    "xxxxxxxxxx x",
    "x        x x",
    "x        x x",
    "x xxxxxxxx x",
    "x          x",
    "x xxxxxxxxxx",
]
print(maze[5][10])

result = solve(maze, "x", Point(10, 0), Point(1, 5))
print(result)
