import os
import shutil
import sys
from math import ceil as c
while 1:
    t=0
    d=len(os.listdir(f:=input("path: ")))
    path=input("dPath : ")
    for files in os.listdir(f):
        t+=1
        shutil.move(os.path.join(f,files),os.path.join(path,files))
        print(f"{t}/{d} [{'='*c(t*100/d):100s}] {t*100/d:.4f} %.",end="\r")
        
    print(f"{t}/{d} [{'='*c(t*100/d):100s}] {t*100/d:.4f} %.")