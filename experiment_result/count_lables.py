# -*- coding: utf-8 -*-
f=open('C:/Users/PSY/Desktop/api_raw.txt',encoding='UTF-8')
raw=f.readlines()
k=[]
for line in raw:
    d=0
    for b in line:
         if b!=']':
             d+=1
         else:
             break
    s1=line[0:d]
    k.append(s1.count(' ')+1)
print(k)