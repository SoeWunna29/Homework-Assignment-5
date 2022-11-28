def rvrs_lnk(s):
    reversed_list = []
    while s:
        if not reversed_list:
            reversed_list = link(s[0], [])
        else:
            reversed_list = link(s[0], reversed_list)
        s = s[1]
    return reversed_list


def link(node, next):
    return [node, next]


print(rvrs_lnk(link(1, link(2, link(3, link(4, []))))))
