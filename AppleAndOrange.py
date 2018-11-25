#!/bin/python

import sys


s,t = raw_input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = raw_input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = raw_input().strip().split(' ')
m,n = [int(m),int(n)]
apple = map(int,raw_input().strip().split(' '))
orange = map(int,raw_input().strip().split(' '))
apple = [ a + x for x in apple]
orange = [ b + y for y in orange]
print sum(i>=s and i<=t for i in apple)
print sum(i>=s and i<=t for i in orange)
