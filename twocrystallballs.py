from math import floor, sqrt


def two_crystal_balls(breaks: [bool]) -> int:
    jumpAmount: int = floor(sqrt(len(breaks)))

    i: int = jumpAmount
    while i < len(breaks):
        if breaks[i]:
            break
        i += jumpAmount

    i -= jumpAmount

    for k in range(i, len(breaks)):
        if breaks[k]:

            return k

    return -1

test_list = [False, False, False, False, False, False, False, True, True, True, True]

print(two_crystal_balls(test_list))
