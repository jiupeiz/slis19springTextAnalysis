#!/usr/bin/env python
# -*- coding: utf-8 -*-
# get pos-word pair

import csv

def get_PosP(filename):
    words = list()
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith("EOS"):
                continue
            word, info = line.rstrip().split("\t")
            info_list = info.split(",")
            posp = [word, info_list[0]] 
            words.append(posp)
    f.close()
    return words

if __name__ == '__main__':
    data = get_PosP("morphs.txt")
    with open("posp.csv", "w") as w:
        writer = csv.writer(w)
        # writer.writerow(['形態素', '品詞'])
        writer.writerows(data)
    w.close()