import os
import sys

lst = list(map(eval,input().split()))
t = lst[0]
c = lst[1]
s = lst[2]

answer = (s-c)*t/c
print(int(answer))