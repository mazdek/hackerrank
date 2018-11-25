#!/bin/python

import sys

def solve(grades):
    res = []
    for i in grades:
        if i > 37:
            if i % 5 == 3:
                i += 2
            elif i % 5 == 4:
                i += 1
        res.append(i)
    return res
      
n = int(raw_input().strip())
grades = []
grades_i = 0
for grades_i in xrange(n):
    grades_t = int(raw_input().strip())
    grades.append(grades_t)
result = solve(grades)
for i in result:
    print i
    
