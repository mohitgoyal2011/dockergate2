import json
import os,sys
import subprocess

a = json.loads(open(sys.argv[1],'r').readlines()[0])
b = json.loads(open(sys.argv[2],'r').readlines()[0])
counta = 0
countb = 0
counta = len(a['syscalls'])
for c in b['syscalls']:
    flag = False
    countb = countb+1
    for d in a['syscalls']:
        if d['name'] == c['name']:
            flag = True
            break
    if not flag:
        print c['name']

print sys.argv[1] + ':' + str(counta)
print sys.argv[2] + ':' + str(countb)
