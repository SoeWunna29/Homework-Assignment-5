def sum_lnk(lnk, g):
    new_list = []
    result = 0
    while lnk:
        new_list.append(lnk[0])
        lnk = lnk[1]
    for i in new_list:
        result += g(i)
    print(result)


def link(node, next):
    return [node, next]


sqr = lambda x: x * x
dbl = lambda y: 2 * y
lnk1 = link(1, link(2, link(3, link(4, []))))
sum_lnk(lnk1, sqr)
lnk2 = link(3, link(5, link(4, link(6, []))))
sum_lnk(lnk2, dbl)
