#!/usr/bin/env python
# -*- coding: utf-8 -*-
import MeCab
# read file and spilt to sentence to lines

def docu2line(filename):

    with open(filename) as f:
        lines = list()
        paras = f.readlines()
        for para in paras:
            line = '\n'.join(para.strip('\n').split('。'))
            lines.append(line)

    return lines

# get tag info
def getTags(filename):

    with open(filename) as f:
        m = MeCab.Tagger()
        tagedS = list()
        for line in f.readlines():
            tagedS.append(m.parse(line))
    
    return tagedS


if __name__ == '__main__':
    lines = docu2line("assi1.txt")
    with open("lines.txt", "w") as w:
        w.writelines(lines)

    morphs = getTags("lines.txt")
    with open("morphs.txt", "w") as w:
        w.writelines(morphs)