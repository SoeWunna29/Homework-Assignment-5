def link(node, next):
    return [node, next]


def apnd(lnk, m):
    helper = []
    while lnk:
        helper.append(lnk[0])
        lnk = lnk[1]
    helper.append(m)
    index = len(helper) - 1
    while index >= 0:
        lnk = link(helper[index], lnk)
        index -= 1
    return lnk


def first(lst):
    return lst[0]


def rest(lst):
    return lst[1]


l = link(1, link(2, link(3, [])))
n = apnd(l, 4)

print(first(rest(rest(rest(n)))))
