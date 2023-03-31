import os
folder = []
with open("list.txt","r") as r:
    folder= [x.split("\n")[0] for x in r.readlines()];

for x in folder:
    if os.path.exists(x)!=True:
        os.mkdir(x)