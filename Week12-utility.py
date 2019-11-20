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


PrintOutput(FindWordCount("Hello World", "or"))
