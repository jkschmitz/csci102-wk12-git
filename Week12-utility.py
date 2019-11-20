# Jake Schmitz
# CSCI 102 Section B
# Week 12 - Part A


def PrintOutput(string):
    print("OUTPUT " + str(string))


def LoadFile(name):
    ret = []
    ret2 = []
    file = open(str(name), "r")
    ret += [file.readlines()]
    for i in ret:
        x = 0
        for f in i:
            ret2.append(f.rstrip())
            x += 1
    return ret2


def UpdateString(s1, s2, num):
    ls = list(s1)
    ls[num] = s2
    temp = ""
    for i in ls:
        temp += str(i)
    return temp


def FindWordCount(lst, st):
    x = 0
    out = 0
    while (len(st)) <= (len(lst) - x + 1):
        if len(st) == 1 and lst[x] == st:
            out += 1
        else:
            if lst[x:(x + len(st))] == st:
                out += 1
        x += 1
    return out


def ScoreFinder(ls1, ls2, st1):
    x = 0
    for (index, value) in enumerate(ls1):
        if str(value).lower() == st1.lower():
            out = str(ls2[index])
            print("OUTPUT " + st1 + " got a score of " + out)
            x = 1
    if x == 0:
        print("OUTPUT player not found")


def Union(lst1, lst2):
    for i in lst2:
        if i not in lst1:
            lst1.append(i)
    return lst1


def Intersection(list1, list2):
    out = []
    temp = []
    for i in list1:
        for j in list2:
            if i == j and i not in out:
                out.append(str(i))
    if out == temp:
        return "No Overlap"
    else:
        return out


def NotIn(list1, list2):
    out = []
    temp = []
    for i in list1:
        if i not in list2 and i not in out:
            out.append(i)
    for i in list2:
        if i not in list1 and i not in out:
            out.append(i)
    if out == temp:
        return "All Overlap"
    else:
        return out


scores1 = [5, 8, 10, 6, 4, "Xai"]
scores2 = [5, 8, 10, 6, 4]
players2 = ["Melvin", "Martian", "Baka", "Xai", "Cody"]
PrintOutput(NotIn(scores1, players2))
PrintOutput(NotIn(scores2, players2))
