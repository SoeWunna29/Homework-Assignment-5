def srt(lnk):
    new_list = []
    while lnk:
        new_list.append(lnk[0])
        lnk = lnk[1]

    for i in range(len(new_list) - 1):
        if new_list[i] > new_list[i + 1]:
            return False
    return True


def link(node, next):
    return [node, next]


lnk1 = link(1, link(2, link(3, link(4, []))))
print(srt(lnk1))

lnk2 = link(1, link(3, link(2, link(4, link(5, [])))))
print(srt(lnk2))

lnk3 = link(3, link(3, link(3, [])))
print(srt(lnk3))
