#!/bin/python

import sys


n = int(raw_input().strip())
height = map(int,raw_input().strip().split(' '))
count = 0
m = max (height)
for i in height:
    if i == m:
        count+=1
print count
