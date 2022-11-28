def cntn_link(s, elm):
    if not s:
        return False
    elif s[0] == elm:
        return True

    return cntn_link(s[1], elm)


def link(node, next):
    return [node, next]


print(cntn_link(link(1, link(2, link(3, []))), 2))
print(cntn_link(link(1, link(2, link(3, []))), 4))
