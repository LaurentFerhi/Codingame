import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

init = int(input())
num_line = int(input())

def next_line(l):
    i = 1
    res = [l[0]]
    while i < len(l):
        if l[i] != l[i-1]:
            res.append(',')
            res.append(l[i])
            i+=1
        else:
            res.append('-')
            res.append(l[i])
            i+=1
    res = ''.join(res).split(',')
    final = []
    for x in res:
        if len(x.split('-')) == 1:
            final.append('1')
            final.append(x)
        else:
            final.append(str(len(x.split('-'))))
            final.append(x[0])
    return final


line = [str(init)]

for _ in range(num_line-1):
    line = next_line(line)

print(' '.join([str(i) for i in line]))
