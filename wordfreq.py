#!/usr/bin/python3
import sys
import string
<<<<<<< HEAD
words = sys.stdin.read().split()
=======

words = open(input("What file to copy from: "))
>>>>>>> parent of 0a05f63 (Revert "task5")
d = dict()
for word in words:
        t = word.translate(str.maketrans('','',string.punctuation)).upper()
        if(len(t) > 0):
                d[t] = d.get(t,0) + 1
l = list()
for key,value in d.items():
        l.append((value,key))
l = sorted(l, reverse=True)
for v,k in l:
        print(k,v)
