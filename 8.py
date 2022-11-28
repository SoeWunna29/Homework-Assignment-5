def insrt(l, elm, ind):
    helper = []
    index = 0
    while l:
        if index == ind:
            helper.append(elm)
            helper.append(l[0])
        else:
            helper.append(l[0])
        l = l[1]
        index += 1

    if ind > index:
        helper.append(elm)
    index = len(helper) - 1
    while index >= 0:
        l = link(helper[index], l)
        index -= 1
    return l


def link(node, next):
    return [node, next]


l = link(11, link(12, link(13, [])))
n = insrt(l, 2021, 1)
print(n)

m = insrt(n, 2022, 20)
print(m)
