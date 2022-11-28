def change(lnk, u, v):
    new_link = []
    helper = []
    while lnk:
        if lnk[0] == u:
            helper.append(v)
        else:
            helper.append(lnk[0])
        lnk = lnk[1]

    index = len(helper) - 1
    counter = index
    while counter >= 0:
        new_link = link(helper[counter], new_link)
        counter -= 1
    return new_link


def link(node, next):
    return [node, next]


l = link(1, link(2, link(3, [])))
n = change(l, 3, 1)
print(n)

m = change(n, 1, 2)
print(m)

change(m, 5, 1)
print(m)
