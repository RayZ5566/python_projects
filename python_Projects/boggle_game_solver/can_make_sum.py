def can_make_sum(lst, target):
    current = 0
    found = []
    helper(lst, target, current, found)
    return len(found) > 0


def helper(lst, target, current,found):
    if current == target:
        found.append(current)

    else:
        if len(lst) != 0:
            ele = lst.pop(0)
            current += ele
            helper(lst, target, current,found)
            current -= ele
            helper(lst, target, current,found)
            lst.insert(0, ele)


if __name__ == '__main__':
    print(can_make_sum([2,5,1,1,10],9))
    print(can_make_sum([2,3,3,5],9))
    print(can_make_sum([3,4,4,6,9,10],17))
    print(can_make_sum([2, 1, 3, 4, 9, 10], 7))