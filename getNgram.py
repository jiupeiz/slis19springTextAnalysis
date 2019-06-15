#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv

def get_wordlist(filename):
    wordlist = list()
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            if not line.startswith("EOS"):
                wordlist.append(line.rstrip().split('\t')[0])
    return wordlist

def get_ngram(filename, n):
    wordlist = get_wordlist(filename)
    ngram_list = list()
    for i in range(0,len(wordlist) - n + 1):
        ngram_list.append(wordlist[i:i + n])
    
    return ngram_list

if __name__ == '__main__':
    ngram = get_ngram("morphs.txt", 2)
    with open("ngram.csv", "w") as w:
        writer = csv.writer(w)
        writer.writerows(ngram)
    w.close()