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


PrintOutput(LoadFile("test.txt"))
