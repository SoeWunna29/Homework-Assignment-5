def prnt_lnk(s):
    new_list = []
    while s:
        new_list.append(s[0])
        s = s[1]
    print("<", *new_list, ">")


def link(node, next):
    return [node, next]


prnt_lnk(link(1, link(2, link(3, link(4, [])))))
